// Frontend Orchestrator: Indian Meal Planner & Cooking To-Do List App

// Global State
window.currentPlan = null;
let costChartInstance = null;

// Tab Management
const tabs = ['meals', 'todo', 'groceries', 'zip', 'subs'];

function initTabNavigation() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');
            switchTab(targetTab);
        });
    });
}

function switchTab(activeTab) {
    tabs.forEach(tab => {
        const btn = document.querySelector(`.tab-btn[data-tab="${tab}"]`);
        const contentDiv = document.getElementById(`tab-${tab}-content`);
        
        if (tab === activeTab) {
            btn.className = "tab-btn pb-3 text-sm font-semibold border-b-2 border-indigo-500 text-indigo-400 transition-all duration-200";
            contentDiv.classList.remove('hidden');
        } else {
            btn.className = "tab-btn pb-3 text-sm font-semibold border-b-2 border-transparent text-slate-400 hover:text-slate-200 transition-all duration-200";
            contentDiv.classList.add('hidden');
        }
    });

    // Special rendering considerations
    if (activeTab === 'zip') {
        renderCostChart();
    }
}

// Generate Meal Plan on Form Submit
async function handleGeneratePlan() {
    const form = document.getElementById('preferences-form');
    const generateBtn = document.getElementById('generate-btn');
    
    // UI elements to show/hide
    const emptyState = document.getElementById('empty-state');
    const loadingState = document.getElementById('loading-state');
    const navTabs = document.getElementById('navigation-tabs');
    
    // Reset views
    emptyState.classList.add('hidden');
    loadingState.classList.remove('hidden');
    navTabs.classList.add('hidden');
    tabs.forEach(t => document.getElementById(`tab-${t}-content`).classList.add('hidden'));
    
    // Gather selections
    const diet = form.querySelector('input[name="diet"]:checked').value;
    const days = form.querySelector('select[name="days"]').value;
    const allergies = [];
    form.querySelectorAll('input[name="allergies"]:checked').forEach(cb => {
        allergies.push(cb.value);
    });
    
    generateBtn.disabled = true;
    generateBtn.innerText = "Analyzing Recipes...";

    try {
        const response = await fetch('/api/plan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ diet, allergies, days })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            window.currentPlan = data;
            
            // Populate sections
            renderMealsTab(data.schedule);
            renderCookingToDoTab(data.cooking_todo);
            renderGroceryListTab(data.grocery_list);
            renderSmartZipTab(data);
            renderSubstitutionsTab(data.substitutions);
            
            // Show tabs and load default view
            loadingState.classList.add('hidden');
            navTabs.classList.remove('hidden');
            switchTab('meals');
        } else {
            alert(data.error || "An error occurred generating the plan.");
            loadingState.classList.add('hidden');
            emptyState.classList.remove('hidden');
        }
    } catch (error) {
        alert("Failed to connect to backend server. Ensure it is running.");
        loadingState.classList.add('hidden');
        emptyState.classList.remove('hidden');
    } finally {
        generateBtn.disabled = false;
        generateBtn.innerText = "Generate Meal Plan";
    }
}

// Render Tab: Meal Plan Schedule
window.toggleCardSubstitution = function(btn) {
    const container = btn.nextElementSibling;
    const svg = btn.querySelector('svg');
    if (container.classList.contains('hidden')) {
        container.classList.remove('hidden');
        svg.classList.add('rotate-180');
    } else {
        container.classList.add('hidden');
        svg.classList.remove('rotate-180');
    }
};

window.toggleAlternateIngredients = function(card) {
    const panel = card.querySelector('.ingredients-panel');
    const isHidden = panel.classList.contains('hidden');
    const svg = card.querySelector('.toggle-label svg');
    const label = card.querySelector('.toggle-label span');
    
    if (isHidden) {
        panel.classList.remove('hidden');
        if (svg) svg.classList.add('rotate-180');
        if (label) label.innerText = "Hide Ingredients";
    } else {
        panel.classList.add('hidden');
        if (svg) svg.classList.remove('rotate-180');
        if (label) label.innerText = "Show Ingredients";
    }
};

// Render Tab: Meal Plan Schedule
function renderMealsTab(schedule) {
    const container = document.getElementById('tab-meals-content');
    container.innerHTML = '';
    
    schedule.forEach(dayPlan => {
        const dayDiv = document.createElement('div');
        // Apply day-specific gradient borders/backgrounds dynamically
        dayDiv.className = `day-grad-${dayPlan.day} p-5 rounded-2xl border border-amber-900/10 space-y-4 animate-fade-in`;
        
        let dayHtml = `
            <div class="flex items-center space-x-3 pb-2 border-b border-amber-900/10">
                <span class="text-sm font-bold font-mono text-amber-700 bg-amber-500/10 px-3 py-1 rounded-md border border-amber-500/20">DAY ${dayPlan.day}</span>
                <h3 class="text-base font-semibold text-slate-800">Daily Eating Schedule</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        `;
        
        const meals = [
            { 
                key: 'breakfast', 
                label: 'Breakfast', 
                borderGlow: 'border-amber-500/10 hover:border-amber-500/30', 
                badge: 'bg-amber-500/10 text-amber-700 border-amber-500/25',
                shadeClass: 'breakfast-shade',
                plateImg: 'assets/breakfast_plate.png'
            },
            { 
                key: 'lunch', 
                label: 'Lunch', 
                borderGlow: 'border-orange-500/10 hover:border-orange-500/30', 
                badge: 'bg-orange-500/10 text-orange-700 border-orange-500/25',
                shadeClass: 'lunch-shade',
                plateImg: 'assets/lunch_plate.png'
            },
            { 
                key: 'dinner', 
                label: 'Dinner', 
                borderGlow: 'border-violet-500/10 hover:border-violet-500/30', 
                badge: 'bg-indigo-500/10 text-indigo-700 border-indigo-500/25',
                shadeClass: 'dinner-shade',
                plateImg: 'assets/dinner_plate.png'
            }
        ];
        
        meals.forEach(mealCfg => {
            const mealData = dayPlan[mealCfg.key];
            const isMod = mealData.is_modified;
            const mealCost = mealData.ingredients.reduce((acc, ing) => acc + ing.cost, 0);
            
            dayHtml += `
                <div class="interactive-card rounded-2xl border ${mealCfg.borderGlow} ${mealCfg.shadeClass} p-5 shadow-lg flex flex-col justify-between h-full">
                    <div>
                        <!-- Timezone Shaded Plate Illustration -->
                        <div class="h-28 w-full rounded-xl overflow-hidden border border-amber-950/10 bg-white mb-1.5 relative shadow-inner">
                            <img src="${mealData.image || mealCfg.plateImg}" alt="${mealCfg.label} plate reference" class="w-full h-full object-cover">
                        </div>
                        <div class="text-[9px] font-bold text-slate-600 uppercase tracking-widest mb-3.5 text-right">
                            Plate Reference
                        </div>
                        
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-xs font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full border ${mealCfg.badge}">${mealCfg.label}</span>
                            <span class="text-xs font-mono text-slate-600">${mealData.category}</span>
                        </div>
                        <h4 class="text-base font-bold text-slate-900 mb-2">${mealData.name}</h4>
                        
                        <!-- Nutritional Info (Vertical List) -->
                        <div class="space-y-1.5 mt-3.5 mb-3.5 bg-white/60 p-3 rounded-lg border border-amber-900/10 text-xs">
                            <div class="flex justify-between border-b border-amber-900/5 pb-1">
                                <span class="font-bold text-slate-500 uppercase tracking-wider text-[10px]">Calories</span>
                                <span class="font-bold font-mono text-slate-850">${mealData.nutrition.calories} kcal</span>
                            </div>
                            <div class="flex justify-between border-b border-amber-900/5 pb-1">
                                <span class="font-bold text-slate-500 uppercase tracking-wider text-[10px]">Protein</span>
                                <span class="font-bold font-mono text-slate-850">${mealData.nutrition.protein}g</span>
                            </div>
                            <div class="flex justify-between border-b border-amber-900/5 pb-1">
                                <span class="font-bold text-slate-500 uppercase tracking-wider text-[10px]">Carbohydrates</span>
                                <span class="font-bold font-mono text-slate-850">${mealData.nutrition.carbs}g</span>
                            </div>
                            <div class="flex justify-between">
                                <span class="font-bold text-slate-500 uppercase tracking-wider text-[10px]">Fat</span>
                                <span class="font-bold font-mono text-slate-850">${mealData.nutrition.fat}g</span>
                            </div>
                        </div>
                        
                        <!-- Cost Badge -->
                        <div class="flex items-center justify-between text-xs mt-3 bg-amber-500/10 border border-amber-500/20 px-2.5 py-1.5 rounded-lg mb-3">
                            <span class="font-bold text-amber-800">Estimated Cost:</span>
                            <span class="font-bold font-mono text-amber-900">Rs. ${mealCost}</span>
                        </div>
                        
                        <!-- Ingredient Quick View -->
                        <div class="space-y-1 mt-4">
                            <div class="text-xs font-semibold text-slate-700 mb-1">Key Ingredients:</div>
                            <ul class="text-xs text-slate-600 list-disc list-inside space-y-0.5">
                                ${mealData.ingredients.slice(0, 5).map(ing => `<li>${ing.name}</li>`).join('')}
                                ${mealData.ingredients.length > 5 ? '<li>+ more items</li>' : ''}
                            </ul>
                        </div>
                    </div>
                    
                    ${isMod ? `
                        <div class="mt-4 border-t border-amber-900/10 pt-3">
                            <button class="text-xs font-semibold text-amber-700 hover:text-amber-800 underline focus:outline-none flex items-center space-x-1" onclick="window.toggleCardSubstitution(this)">
                                <span>Need Substitution?</span>
                                <svg class="h-3 w-3 transform transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
                                </svg>
                            </button>
                            <div class="hidden mt-2 p-2 rounded-lg bg-amber-500/5 border border-amber-500/15 space-y-1.5">
                                ${mealData.applied_substitutions.map(sub => `
                                    <div class="text-[10px] text-slate-700">
                                        Swapped <span class="line-through text-slate-400 font-mono">${sub.original}</span> &rarr; <span class="font-bold text-amber-800">${sub.substituted}</span>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    ` : ''}
                </div>
            `;
        });
        
        dayHtml += `</div>`;
        
        // Add Daily Alternate Suggestion
        if (dayPlan.alternate) {
            const altCost = dayPlan.alternate.ingredients.reduce((acc, ing) => acc + ing.cost, 0);
            dayHtml += `
                <div class="mt-6 border-t border-amber-900/10 pt-4">
                    <div class="bg-amber-50/60 hover:bg-amber-50/95 transition-all duration-200 rounded-xl border border-amber-900/10 p-4 cursor-pointer" onclick="window.toggleAlternateIngredients(this)">
                        <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
                            <div class="flex items-center space-x-4">
                                <div class="h-16 w-16 rounded-lg overflow-hidden flex-shrink-0 border border-amber-900/10 bg-white shadow-sm">
                                    <img src="${dayPlan.alternate.image || 'assets/lunch_plate.png'}" alt="Alternate meal reference" class="w-full h-full object-cover">
                                </div>
                                <div>
                                    <span class="inline-block text-[9px] font-bold uppercase tracking-wider text-amber-700 bg-amber-500/15 px-2 py-0.5 rounded border border-amber-500/20 mb-1">Alternate Suggestion</span>
                                    <h4 class="text-sm font-bold text-slate-800">${dayPlan.alternate.name}</h4>
                                    <p class="text-xs text-slate-600 mt-0.5">Category: ${dayPlan.alternate.category} &bull; Type: ${dayPlan.alternate.type.toUpperCase()}</p>
                                </div>
                            </div>
                            
                            <div class="flex flex-wrap items-center gap-2 text-right">
                                <div class="text-[10px] text-slate-700 bg-white px-2 py-1 rounded border border-amber-900/5 font-medium">
                                    ${dayPlan.alternate.nutrition.calories} kcal &bull; P: ${dayPlan.alternate.nutrition.protein}g &bull; C: ${dayPlan.alternate.nutrition.carbs}g &bull; F: ${dayPlan.alternate.nutrition.fat}g
                                </div>
                                <div class="text-xs font-bold font-mono text-amber-800 bg-amber-500/10 border border-amber-500/20 px-2 py-1 rounded">
                                    Rs. ${altCost}
                                </div>
                                <div class="text-[10px] font-semibold text-amber-700 underline flex items-center space-x-0.5 toggle-label">
                                    <span>Show Ingredients</span>
                                    <svg class="h-3 w-3 transform transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Hidden Ingredients Panel -->
                        <div class="hidden ingredients-panel mt-4 pt-3 border-t border-amber-900/10 text-xs text-slate-700 animate-fade-in" onclick="event.stopPropagation()">
                            <div class="font-bold text-amber-800 mb-1.5 uppercase tracking-wider text-[9px]">Required Ingredients</div>
                            <div class="grid grid-cols-2 gap-x-6 gap-y-1">
                                ${dayPlan.alternate.ingredients.map(ing => `
                                    <div class="flex justify-between border-b border-amber-900/5 py-0.5 font-medium">
                                        <span>${ing.name}</span>
                                        <span class="font-mono text-slate-500">${ing.amount} ${ing.unit}</span>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }
        
        dayDiv.innerHTML = dayHtml;
        container.appendChild(dayDiv);
    });
    
    // Add Substitutions Quick-Reference Box at the bottom of the meals tab
    const hasSubs = schedule.some(day => 
        day.breakfast.is_modified || day.lunch.is_modified || day.dinner.is_modified
    );
    
    if (hasSubs) {
        const subsSummaryDiv = document.createElement('div');
        subsSummaryDiv.className = "mt-8 p-6 rounded-2xl border border-dashed border-amber-900/20 bg-amber-50/40 animate-fade-in";
        subsSummaryDiv.innerHTML = `
            <div class="flex flex-col space-y-1">
                <h4 class="text-sm font-bold text-slate-800">Substitution Reference Guide</h4>
                <p class="text-xs text-slate-600">You have active allergen substitutions in this plan. Click below to view the swap guide.</p>
            </div>
            <div class="mt-4">
                <button id="toggle-meals-subs-btn" class="text-xs font-bold text-amber-700 hover:text-amber-800 underline focus:outline-none flex items-center space-x-1">
                    <span>Show Substitution Details</span>
                    <svg class="h-3.5 w-3.5 transform transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
                    </svg>
                </button>
                <div id="meals-subs-container" class="hidden mt-4 grid grid-cols-1 sm:grid-cols-2 gap-4">
                    ${schedule.map(day => {
                        const daySubs = [];
                        ['breakfast', 'lunch', 'dinner'].forEach(mKey => {
                            const meal = day[mKey];
                            if (meal.is_modified && meal.applied_substitutions) {
                                meal.applied_substitutions.forEach(sub => {
                                    daySubs.push({
                                        mealName: meal.name,
                                        original: sub.original,
                                        substituted: sub.substituted,
                                        reason: sub.reason
                                    });
                                });
                            }
                        });
                        return daySubs.map(sub => `
                            <div class="p-3.5 rounded-xl border border-amber-900/10 bg-white shadow-sm flex items-center justify-between text-xs">
                                <div>
                                    <div class="font-bold text-slate-800">${sub.mealName}</div>
                                    <div class="text-slate-600 mt-1">
                                        Swap <span class="line-through text-slate-400 font-mono">${sub.original}</span> &rarr; <span class="text-amber-700 font-bold font-mono">${sub.substituted}</span>
                                    </div>
                                </div>
                                <span class="text-[9px] font-bold text-amber-700 bg-amber-500/10 border border-amber-500/20 px-1.5 py-0.5 rounded font-mono">${sub.reason}</span>
                            </div>
                        `).join('');
                    }).join('')}
                </div>
            </div>
        `;
        container.appendChild(subsSummaryDiv);
        
        subsSummaryDiv.querySelector('#toggle-meals-subs-btn').addEventListener('click', (e) => {
            const content = subsSummaryDiv.querySelector('#meals-subs-container');
            const svg = subsSummaryDiv.querySelector('svg');
            const span = subsSummaryDiv.querySelector('span');
            if (content.classList.contains('hidden')) {
                content.classList.remove('hidden');
                svg.classList.add('rotate-180');
                span.innerText = "Hide Substitution Details";
            } else {
                content.classList.add('hidden');
                svg.classList.remove('rotate-180');
                span.innerText = "Show Substitution Details";
            }
        });
    }
}

// Render Tab: Cooking To-Do Checklist
function renderCookingToDoTab(cookingTodo) {
    const container = document.getElementById('tab-todo-content');
    container.innerHTML = '';
    
    cookingTodo.forEach((item, mealIdx) => {
        const sectionDiv = document.createElement('div');
        sectionDiv.className = "rounded-2xl border border-amber-900/10 bg-white p-6 space-y-4 animate-fade-in shadow-sm";
        
        let sectionHtml = `
            <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                <div>
                    <h3 class="text-base font-bold text-slate-800">${item.meal_name}</h3>
                    <p class="text-xs text-slate-500">Day ${item.day} &bull; ${item.meal}</p>
                </div>
                <div class="text-[10px] font-mono text-slate-700 bg-slate-100 border border-slate-200 px-2 py-0.5 rounded">
                    ${item.steps.length} Steps
                </div>
            </div>
            <div class="space-y-3">
        `;
        
        item.steps.forEach((step, stepIdx) => {
            const uniqueId = `todo-${mealIdx}-${stepIdx}`;
            sectionHtml += `
                <div class="stepper-item flex items-start">
                    <label class="checkbox-container w-full">
                        <input type="checkbox" id="${uniqueId}" class="todo-item-check">
                        <div class="checkbox-visual">
                            <svg class="h-3 w-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                            </svg>
                        </div>
                        <div class="todo-text flex-grow">
                            <span class="inline-block px-1.5 py-0.2 rounded text-[10px] font-bold mr-1.5 uppercase ${step.type === 'Prep' ? 'bg-indigo-500/10 text-indigo-700 border border-indigo-500/25' : 'bg-pink-500/10 text-pink-700 border border-pink-500/25'}">${step.type}</span>
                            ${step.text}
                        </div>
                    </label>
                </div>
            `;
        });
        
        sectionHtml += `</div>`;
        sectionDiv.innerHTML = sectionHtml;
        container.appendChild(sectionDiv);
    });
}

// Render Tab: Grocery Checklist
function renderGroceryListTab(groceryList) {
    const container = document.getElementById('tab-groceries-content');
    container.innerHTML = '';
    
    // Group by category
    const categories = {};
    groceryList.forEach(item => {
        const cat = item.category;
        if (!categories[cat]) categories[cat] = [];
        categories[cat].push(item);
    });
    
    // Header controls
    const controlsDiv = document.createElement('div');
    controlsDiv.className = "flex items-center justify-between pb-2 border-b border-amber-900/10";
    controlsDiv.innerHTML = `
        <h3 class="text-base font-semibold text-slate-800">Categorized Shopping Items</h3>
        <button id="toggle-all-groceries-btn" class="text-xs text-amber-700 hover:text-amber-800 font-medium">Check All</button>
    `;
    container.appendChild(controlsDiv);
    
    // Render categories
    Object.keys(categories).forEach((cat, catIdx) => {
        const catDiv = document.createElement('div');
        catDiv.className = "space-y-3 animate-fade-in";
        
        let catHtml = `
            <div class="text-xs font-bold uppercase tracking-wider text-slate-600 mt-4">${cat}</div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        `;
        
        categories[cat].forEach((item, itemIdx) => {
            const uniqueId = `groc-${catIdx}-${itemIdx}`;
            const savingPercent = item.meals_count >= 3 ? '20% Zipped Savings' : item.meals_count === 2 ? '10% Zipped Savings' : '';
            
            catHtml += `
                <label class="checkbox-container">
                    <input type="checkbox" id="${uniqueId}" class="grocery-item-check">
                    <div class="checkbox-visual">
                        <svg class="h-3 w-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                        </svg>
                    </div>
                    <div class="todo-text flex-grow flex items-center justify-between pr-1">
                        <div>
                            <span class="font-medium text-slate-800">${item.name}</span>
                            <div class="text-[10px] text-slate-500">${item.amount} ${item.unit} &bull; Used in ${item.meals_count} meals</div>
                        </div>
                        <div class="text-right">
                            <span class="text-xs font-mono text-amber-800 font-bold">Rs. ${item.optimized_cost}</span>
                            ${savingPercent ? `<div class="text-[8px] text-emerald-600 font-bold">${savingPercent}</div>` : ''}
                        </div>
                    </div>
                </label>
            `;
        });
        
        catHtml += `</div>`;
        catDiv.innerHTML = catHtml;
        container.appendChild(catDiv);
    });
    
    // Toggle all button logic
    let checkAllState = true;
    document.getElementById('toggle-all-groceries-btn').addEventListener('click', (e) => {
        const checkboxes = document.querySelectorAll('.grocery-item-check');
        checkboxes.forEach(cb => cb.checked = checkAllState);
        e.target.innerText = checkAllState ? "Uncheck All" : "Check All";
        checkAllState = !checkAllState;
    });
}

// Render Tab: Smart Zip Logic & Budget Optimization
function renderSmartZipTab(data) {
    const container = document.getElementById('tab-zip-content');
    container.innerHTML = '';
    
    const zipDiv = document.createElement('div');
    zipDiv.className = "space-y-6 animate-fade-in";
    
    const pricing = data.pricing;
    const hacks = data.batch_prep_hacks;
    
    let zipHtml = `
        <!-- Pricing Metrics -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
            <div class="p-5 rounded-2xl border border-amber-900/10 bg-white flex flex-col justify-between">
                <span class="text-xs text-slate-500 font-semibold uppercase tracking-wider">Un-Optimized Raw Cost</span>
                <span class="text-2xl font-black text-slate-800 mt-2 font-mono">Rs. ${pricing.raw_cost}</span>
            </div>
            <div class="p-5 rounded-2xl border border-amber-500/20 bg-amber-500/5 flex flex-col justify-between shadow shadow-amber-500/5">
                <span class="text-xs text-amber-800 font-semibold uppercase tracking-wider">Budget-Zip Final Cost</span>
                <span class="text-2xl font-black text-amber-800 mt-2 font-mono">Rs. ${pricing.optimized_cost}</span>
            </div>
            <div class="p-5 rounded-2xl border border-emerald-500/20 bg-emerald-500/5 flex flex-col justify-between shadow shadow-emerald-500/5">
                <span class="text-xs text-emerald-800 font-semibold uppercase tracking-wider">Estimated Zip Savings</span>
                <span class="text-2xl font-black text-emerald-800 mt-2 font-mono">Rs. ${pricing.savings}</span>
            </div>
        </div>

        <!-- Cost Comparison Chart -->
        <div class="p-6 rounded-2xl border border-amber-900/15 bg-white shadow-sm">
            <h4 class="text-sm font-bold text-slate-800 mb-4">Cost Comparison by Ingredient Category</h4>
            <div class="h-60 relative w-full flex items-center justify-center">
                <canvas id="costComparisonChart" class="w-full h-full"></canvas>
            </div>
        </div>

        <!-- Smart Batch Prep Hacks -->
        <div class="p-6 rounded-2xl border border-amber-900/15 bg-white shadow-sm space-y-4">
            <h4 class="text-sm font-bold text-slate-800 flex items-center">
                <svg class="h-5 w-5 mr-2 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
                Budget-Free Zip Prep Hacks
            </h4>
            <p class="text-xs text-slate-500">
                Our "Zip" logic groups ingredient counts. Perform these prep shortcuts together to minimize cooking time.
            </p>
            <ul class="space-y-2.5 text-xs text-slate-700 pl-4 list-disc">
                ${hacks.map(hack => `<li>${hack}</li>`).join('')}
                ${hacks.length === 0 ? '<li class="text-slate-500 list-none">No overlapping batch-prep ingredients detected.</li>' : ''}
            </ul>
        </div>

        <!-- Export ZIP Download -->
        <div class="p-6 rounded-2xl border border-amber-900/15 bg-white flex flex-col sm:flex-row items-center justify-between gap-4 shadow-sm">
            <div>
                <h4 class="text-sm font-bold text-slate-800">Export Offline Package</h4>
                <p class="text-xs text-slate-500">Download a consolidated ZIP packet containing text versions of this meal plan.</p>
            </div>
            <button id="download-zip-btn" class="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold transition-all shadow shadow-amber-600/10 active:scale-95">
                <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
                <span>Download Meal Plan ZIP</span>
            </button>
        </div>
    `;
    
    zipDiv.innerHTML = zipHtml;
    container.appendChild(zipDiv);
    
    // Add ZIP click event
    document.getElementById('download-zip-btn').addEventListener('click', handleDownloadZip);
}

// Render Tab: Cost Chart (Chart.js)
function renderCostChart() {
    const ctx = document.getElementById('costComparisonChart');
    if (!ctx || !window.currentPlan) return;
    
    // Aggregate original and optimized costs per category
    const catOriginals = {};
    const catOptimizeds = {};
    
    window.currentPlan.grocery_list.forEach(item => {
        const cat = item.category;
        catOriginals[cat] = (catOriginals[cat] || 0) + item.original_cost;
        catOptimizeds[cat] = (catOptimizeds[cat] || 0) + item.optimized_cost;
    });
    
    const labels = Object.keys(catOriginals);
    const dataOriginal = labels.map(l => catOriginals[l]);
    const dataOptimized = labels.map(l => catOptimizeds[l]);
    
    if (costChartInstance) {
        costChartInstance.destroy();
    }
    
    costChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Raw Cost (Rs)',
                    data: dataOriginal,
                    backgroundColor: 'rgba(217, 119, 6, 0.35)', // Warm golden amber
                    borderColor: 'rgb(217, 119, 6)',
                    borderWidth: 1.5
                },
                {
                    label: 'Zip-Optimized Cost (Rs)',
                    data: dataOptimized,
                    backgroundColor: 'rgba(194, 65, 12, 0.6)',  // Warm contrast orange-brown
                    borderColor: 'rgb(194, 65, 12)',
                    borderWidth: 1.5
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: '#201a15', // Deep chocolate brown
                        font: { size: 11, weight: '600' }
                    }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(120, 53, 15, 0.08)' }, // Subtle warm border grids
                    ticks: { color: '#5c534c', font: { size: 10, weight: '500' } }
                },
                y: {
                    grid: { color: 'rgba(120, 53, 15, 0.08)' },
                    ticks: { color: '#5c534c', font: { size: 10, weight: '500' } }
                }
            }
        }
    });
}

// Render Tab: Substitutions Log
function renderSubstitutionsTab(substitutions) {
    const container = document.getElementById('tab-subs-content');
    container.innerHTML = '';
    
    const subsDiv = document.createElement('div');
    subsDiv.className = "space-y-4 animate-fade-in";
    
    let subsHtml = `
        <div class="flex flex-col space-y-1.5 pb-2 border-b border-amber-900/10">
            <h3 class="text-base font-semibold text-slate-800">Diet & Allergy Replacements</h3>
            <p class="text-xs text-slate-500 font-medium">Dynamic swaps executed automatically during recipe selection</p>
        </div>
    `;
    
    if (substitutions.length === 0) {
        subsHtml += `
            <div class="text-center py-12 text-xs text-slate-500 border border-dashed border-amber-900/20 rounded-2xl bg-white">
                No allergen allergen substitutions were required for this plan.
            </div>
        `;
    } else {
        subsHtml += `<div class="grid grid-cols-1 md:grid-cols-2 gap-4">`;
        substitutions.forEach(sub => {
            subsHtml += `
                <div class="p-4 rounded-xl border border-amber-900/10 bg-white flex items-center justify-between shadow-sm">
                    <div>
                        <div class="text-xs font-bold text-slate-700">${sub.meal_name}</div>
                        <div class="text-sm mt-1.5 text-slate-800 font-medium">
                            Swapped <span class="line-through text-slate-400 font-mono">${sub.original}</span> 
                            &rarr; <span class="text-amber-700 font-semibold font-mono">${sub.substituted}</span>
                        </div>
                    </div>
                    <span class="text-[10px] px-2 py-0.5 bg-amber-500/10 text-amber-700 border border-amber-500/25 rounded-md font-mono">${sub.reason}</span>
                </div>
            `;
        });
        subsHtml += `</div>`;
    }
    
    subsDiv.innerHTML = subsHtml;
    container.appendChild(subsDiv);
}

// Trigger in-memory ZIP package download
async function handleDownloadZip() {
    if (!window.currentPlan) return;
    
    const downloadBtn = document.getElementById('download-zip-btn');
    const originalText = downloadBtn.innerHTML;
    
    downloadBtn.disabled = true;
    downloadBtn.innerHTML = `
        <svg class="h-4.5 w-4.5 animate-spin mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 1121.21 7.89M9 11l3 3m0 0l3-3m-3 3V3" />
        </svg>
        <span>Packaging ZIP...</span>
    `;
    
    try {
        const response = await fetch('/api/export-zip', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(window.currentPlan)
        });
        
        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Rasoi_Meal_Plan_And_Cooking_List.zip';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        } else {
            alert("Failed to export ZIP file.");
        }
    } catch (error) {
        alert("Network error exporting ZIP file.");
    } finally {
        downloadBtn.disabled = false;
        downloadBtn.innerHTML = originalText;
    }
}

// Startup
document.addEventListener('DOMContentLoaded', () => {
    initTabNavigation();
    
    // Bind form submit
    const generateBtn = document.getElementById('generate-btn');
    generateBtn.addEventListener('click', handleGeneratePlan);

    // Dynamic Diet Preview Image Switcher
    const dietRadios = document.querySelectorAll('input[name="diet"]');
    const img = document.getElementById('diet-preview-img');
    const label = document.getElementById('diet-preview-label');

    function updateDietPreview(val) {
        if (!img || !label) return;
        
        img.style.opacity = '0';
        
        setTimeout(() => {
            if (val === 'Veg') {
                img.src = 'assets/veg_diet.png';
                img.alt = 'Vegetarian Platter';
                label.textContent = 'Vegetarian Plan Active';
            } else if (val === 'Vegan') {
                img.src = 'assets/vegan_diet.png';
                img.alt = 'Vegan Platter';
                label.textContent = 'Vegan Plan Active';
            } else {
                img.src = 'assets/non_veg_diet.png';
                img.alt = 'Non-Vegetarian Platter';
                label.textContent = 'Non-Vegetarian Plan Active';
            }
            img.style.opacity = '1';
        }, 180);
    }

    // Set initial preview state based on checked option
    const activeRadio = document.querySelector('input[name="diet"]:checked');
    if (activeRadio) {
        updateDietPreview(activeRadio.value);
    }

    // Bind selection changes
    dietRadios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            updateDietPreview(e.target.value);
        });
    });
});
