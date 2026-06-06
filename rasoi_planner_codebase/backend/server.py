# Backend Server: Indian Meal Planner & Cooking To-Do List App
import os
import io
import json
import zipfile
from starlette.applications import Starlette
from starlette.responses import JSONResponse, StreamingResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from backend.meals_data import MEALS_DATABASE

# Helper to deep copy structures
def deep_copy_meal(meal):
    return {
        "id": meal["id"],
        "name": meal["name"],
        "type": meal["type"],
        "category": meal["category"],
        "allergens": list(meal["allergens"]),
        "ingredients": [dict(ing) for ing in meal["ingredients"]],
        "prep_steps": list(meal["prep_steps"]),
        "cook_steps": list(meal["cook_steps"]),
        "substitutions": dict(meal["substitutions"]),
        "image": meal.get("image", ""),
        "nutrition": dict(meal.get("nutrition", {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}))
    }

# Meal planning logic
async def generate_plan(request):
    try:
        body = await request.json()
    except Exception:
        body = {}
        
    user_diet = body.get("diet", "Veg")  # "Vegan", "Veg", "Non-Veg"
    user_allergies = body.get("allergies", [])  # list of strings e.g., ["dairy", "gluten"]
    days = int(body.get("days", 3))  # 1, 3, 5, or 7
    
    # Pool of validated meals
    available_meals = []
    
    for meal in MEALS_DATABASE:
        # 1. Diet Filter
        if user_diet == "Vegan" and meal["category"] != "Vegan":
            continue
        if user_diet == "Veg" and meal["category"] == "Non-Veg":
            continue
            
        # 2. Allergy Filter with dynamic substitutions
        disqualified = False
        copied_meal = deep_copy_meal(meal)
        applied_subs = []
        
        for allergy in user_allergies:
            if allergy in copied_meal["allergens"]:
                sub_info = copied_meal["substitutions"].get(allergy)
                if not sub_info:
                    # No substitution available for this critical allergen; exclude meal
                    disqualified = True
                    break
                else:
                    # Apply substitution (handle single or list of substitutions)
                    subs_list = sub_info if isinstance(sub_info, list) else [sub_info]
                    for sub in subs_list:
                        target = sub["replace"]
                        replacement = sub["with"]
                        cost_diff = sub["cost_diff"]
                        
                        # Find and replace ingredient
                        for ing in copied_meal["ingredients"]:
                            if ing["name"].lower() == target.lower():
                                ing["name"] = f"{replacement} (Substituted)"
                                ing["cost"] += cost_diff
                                if ing["cost"] < 0:
                                    ing["cost"] = 0
                                applied_subs.append({
                                    "meal_name": copied_meal["name"],
                                    "original": target,
                                    "substituted": replacement,
                                    "reason": f"Allergy: {allergy}"
                                })
                                
        if not disqualified:
            copied_meal["applied_substitutions"] = applied_subs
            copied_meal["is_modified"] = len(applied_subs) > 0
            available_meals.append(copied_meal)
            
    # Split available meals into breakfast, lunch, and dinner pools
    breakfasts = [m for m in available_meals if m["type"] == "breakfast"]
    lunches = [m for m in available_meals if m["type"] == "lunch"]
    dinners = [m for m in available_meals if m["type"] == "dinner"]
    
    # Edge case: if pools are empty, fallback to simple safe options
    if not breakfasts or not lunches or not dinners:
        return JSONResponse({
            "error": "No meals matching your criteria were found. Try relaxing allergy filters."
        }, status_code=400)
        
    # Generate schedule
    schedule = []
    for day in range(1, days + 1):
        breakfast = breakfasts[(day - 1) % len(breakfasts)]
        lunch = lunches[(day - 1) % len(lunches)]
        dinner = dinners[(day - 1) % len(dinners)]
        
        # Pick a unique alternate meal matching preferences
        active_ids = {breakfast["id"], lunch["id"], dinner["id"]}
        alternates_pool = [m for m in available_meals if m["id"] not in active_ids]
        if not alternates_pool:
            alternates_pool = available_meals
        alternate = alternates_pool[(day - 1) % len(alternates_pool)]
        
        schedule.append({
            "day": day,
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner,
            "alternate": alternate
        })
        
    # 3. Grocery Zipping Logic
    zipped_grocery = {}
    total_raw_cost = 0
    
    for day_plan in schedule:
        for meal_key in ["breakfast", "lunch", "dinner"]:
            meal = day_plan[meal_key]
            for ing in meal["ingredients"]:
                name = ing["name"]
                amount = ing["amount"]
                unit = ing["unit"]
                cat = ing["category"]
                cost = ing["cost"]
                
                total_raw_cost += cost
                
                if name not in zipped_grocery:
                    zipped_grocery[name] = {
                        "name": name,
                        "amount": amount,
                        "unit": unit,
                        "category": cat,
                        "cost": cost,
                        "count": 1
                    }
                else:
                    zipped_grocery[name]["amount"] += amount
                    zipped_grocery[name]["cost"] += cost
                    zipped_grocery[name]["count"] += 1

    # 4. Budget Optimization (Zipping overlap savings)
    optimized_grocery = []
    total_optimized_cost = 0
    total_savings = 0
    batch_prep_hacks = []
    
    for item in zipped_grocery.values():
        name = item["name"]
        amount = item["amount"]
        unit = item["unit"]
        cost = item["cost"]
        count = item["count"]
        
        # Apply bulk purchase cost discount for zipped ingredients
        # If an item appears in 3 or more meals, apply a 20% discount (simulating buying in bulk)
        # If it appears in 2 meals, apply 10% discount
        final_cost = cost
        if count >= 3:
            final_cost = int(cost * 0.8)
            total_savings += (cost - final_cost)
        elif count == 2:
            final_cost = int(cost * 0.9)
            total_savings += (cost - final_cost)
            
        total_optimized_cost += final_cost
        
        optimized_grocery.append({
            "name": name,
            "amount": round(amount, 2),
            "unit": unit,
            "category": item["category"],
            "original_cost": cost,
            "optimized_cost": final_cost,
            "meals_count": count
        })
        
        # Add a batch prep suggestion if the ingredient appears multiple times
        if count >= 2:
            prep_action = "Chop"
            if "flour" in name.lower() or "batter" in name.lower() or "rice" in name.lower():
                prep_action = "Measure/Prep"
            batch_prep_hacks.append(
                f"{prep_action} {name} in bulk. You need it for {count} different meals this week. Doing this together saves 15 mins."
            )

    # 5. Extract all substitutions applied across the plan
    all_applied_subs = []
    for day_plan in schedule:
        for meal_key in ["breakfast", "lunch", "dinner"]:
            meal = day_plan[meal_key]
            if "applied_substitutions" in meal:
                for sub in meal["applied_substitutions"]:
                    if sub not in all_applied_subs:
                        all_applied_subs.append(sub)
                        
    # 6. Generate interactive cooking checklist
    cooking_checklist = []
    for day_plan in schedule:
        day = day_plan["day"]
        for meal_key in ["breakfast", "lunch", "dinner"]:
            meal = day_plan[meal_key]
            
            # Combine steps
            steps = []
            for step in meal["prep_steps"]:
                steps.append({"type": "Prep", "text": step})
            for step in meal["cook_steps"]:
                steps.append({"type": "Cook", "text": step})
                
            cooking_checklist.append({
                "day": day,
                "meal": meal_key.capitalize(),
                "meal_name": meal["name"],
                "steps": steps
            })

    return JSONResponse({
        "diet": user_diet,
        "allergies": user_allergies,
        "days": days,
        "schedule": schedule,
        "grocery_list": optimized_grocery,
        "pricing": {
            "raw_cost": total_raw_cost,
            "optimized_cost": total_optimized_cost,
            "savings": total_savings
        },
        "batch_prep_hacks": batch_prep_hacks,
        "substitutions": all_applied_subs,
        "cooking_todo": cooking_checklist
    })

# In-memory ZIP package creation and download
async def export_zip(request):
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"error": "Invalid request payload"}, status_code=400)
        
    schedule = body.get("schedule", [])
    grocery_list = body.get("grocery_list", [])
    cooking_todo = body.get("cooking_todo", [])
    substitutions = body.get("substitutions", [])
    pricing = body.get("pricing", {})
    
    # 1. Format Meal Plan text
    meal_plan_text = "=== INDIAN MEAL PLAN ===\n\n"
    for day in schedule:
        meal_plan_text += f"DAY {day['day']}\n"
        day_cal = 0
        day_prot = 0
        day_carbs = 0
        day_fat = 0
        day_cost = 0
        
        for meal_key in ["breakfast", "lunch", "dinner"]:
            meal = day[meal_key]
            meal_cost = sum(ing.get("cost", 0) for ing in meal.get("ingredients", []))
            nut = meal.get("nutrition", {"calories": 0, "protein": 0, "carbs": 0, "fat": 0})
            
            day_cal += nut.get("calories", 0)
            day_prot += nut.get("protein", 0)
            day_carbs += nut.get("carbs", 0)
            day_fat += nut.get("fat", 0)
            day_cost += meal_cost
            
            meal_plan_text += f"  {meal_key.capitalize()}: {meal['name']} (Est. Cost: Rs. {meal_cost}, Calories: {nut.get('calories', 0)} kcal, Protein: {nut.get('protein', 0)}g, Carbs: {nut.get('carbs', 0)}g, Fat: {nut.get('fat', 0)}g)\n"
            
        if "alternate" in day:
            alt = day["alternate"]
            alt_cost = sum(ing.get("cost", 0) for ing in alt.get("ingredients", []))
            alt_nut = alt.get("nutrition", {"calories": 0, "protein": 0, "carbs": 0, "fat": 0})
            meal_plan_text += f"  Alternate Suggestion: {alt['name']} (Est. Cost: Rs. {alt_cost}, Calories: {alt_nut.get('calories', 0)} kcal, Protein: {alt_nut.get('protein', 0)}g, Carbs: {alt_nut.get('carbs', 0)}g, Fat: {alt_nut.get('fat', 0)}g)\n"
            
        meal_plan_text += f"  >> DAILY TOTALS - Calories: {day_cal} kcal, Protein: {day_prot}g, Carbs: {day_carbs}g, Fat: {day_fat}g, Est. Cost: Rs. {day_cost}\n\n"
        
    # 2. Format Grocery List text
    grocery_text = "=== SMART GROCERY LIST ===\n"
    grocery_text += "Aggregated and optimized using Budget-Free Zip Logic\n\n"
    
    categories = {}
    for item in grocery_list:
        cat = item["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
        
    for cat, items in categories.items():
        grocery_text += f"[{cat}]\n"
        for item in items:
            grocery_text += f"  [ ] {item['name']}: {item['amount']} {item['unit']} (Est: Rs. {item['optimized_cost']})\n"
        grocery_text += "\n"
        
    grocery_text += f"Total Raw Cost: Rs. {pricing.get('raw_cost', 0)}\n"
    grocery_text += f"Total Optimized Cost: Rs. {pricing.get('optimized_cost', 0)}\n"
    grocery_text += f"Total Budget-Zip Savings: Rs. {pricing.get('savings', 0)}\n"

    # 3. Format Cooking Checklist text
    todo_text = "=== COOKING TO-DO LIST ===\n\n"
    for item in cooking_todo:
        todo_text += f"DAY {item['day']} - {item['meal']} ({item['meal_name']})\n"
        for i, step in enumerate(item["steps"], 1):
            todo_text += f"  [ ] Step {i} [{step['type']}]: {step['text']}\n"
        todo_text += "\n"
        
    # 4. Format Substitutions text
    sub_text = "=== ALLERGY & DIET SUBSTITUTIONS MAPPINGS ===\n\n"
    if not substitutions:
        sub_text += "No ingredient substitutions were required for this plan.\n"
    else:
        for sub in substitutions:
            sub_text += f"In {sub['meal_name']}:\n"
            sub_text += f"  Swapped '{sub['original']}' with '{sub['substituted']}' due to {sub['reason']}\n\n"

    # Create memory buffer for ZIP
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr("Meal_Plan.txt", meal_plan_text)
        zip_file.writestr("Grocery_List.txt", grocery_text)
        zip_file.writestr("Cooking_ToDo.txt", todo_text)
        zip_file.writestr("Substitutions.txt", sub_text)
        
    zip_buffer.seek(0)
    
    return StreamingResponse(
        zip_buffer, 
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=Indian_Cooking_To_Do_List.zip"}
    )

# Compute absolute path to 'frontend' relative to server.py
current_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(current_dir)
frontend_dir = os.path.join(workspace_dir, "frontend")

# Define routing. Note: API endpoints must be declared before Mount("/")
routes = [
    Route("/api/ping", endpoint=lambda r: JSONResponse({"status": "ok"}), methods=["GET"]),
    Route("/api/plan", endpoint=generate_plan, methods=["POST"]),
    Route("/api/export-zip", endpoint=export_zip, methods=["POST"]),
    Mount("/", app=StaticFiles(directory=frontend_dir, html=True), name="static")
]

# Configure CORS explicitly
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
]

# Initialize Starlette Application
app = Starlette(
    debug=True,
    routes=routes,
    middleware=middleware
)

if __name__ == "__main__":
    import uvicorn
    print("Starting Starlette backend on http://127.0.0.1:8000...")
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
