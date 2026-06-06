# Recipe Database, Nutritional Profiles, and Photo Assets for Indian Meals

MEALS_DATABASE = [
    # --- BREAKFASTS ---
    {
        "id": "poha",
        "name": "Kanda Poha",
        "type": "breakfast",
        "category": "Vegan",
        "allergens": ["nuts", "mustard"],
        "image": "assets/poha.png",
        "nutrition": {"calories": 310, "protein": 6, "carbs": 55, "fat": 8},
        "ingredients": [
            {"name": "Flattened Rice (Poha)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 15},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Potato", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Peanuts", "amount": 30, "unit": "g", "category": "Nuts & Seeds", "cost": 10},
            {"name": "Mustard Seeds", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Curry Leaves", "amount": 5, "unit": "g", "category": "Vegetables", "cost": 1},
            {"name": "Green Chillies", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 2},
            {"name": "Turmeric Powder", "amount": 3, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Lemon", "amount": 0.5, "unit": "pc", "category": "Vegetables", "cost": 3},
            {"name": "Cooking Oil", "amount": 15, "unit": "ml", "category": "Grains & Spices", "cost": 3}
        ],
        "prep_steps": [
            "Rinse flattened rice (poha) in a colander under running water, drain, and set aside to soften.",
            "Finely chop the onion and dice the potato into small cubes.",
            "Chop the green chillies."
        ],
        "cook_steps": [
            "Heat oil in a pan, add peanuts, and fry until crunchy. Remove and set aside.",
            "In the same oil, temper mustard seeds, green chillies, and curry leaves.",
            "Add chopped onions and sauté until translucent. Add diced potatoes and cook until soft.",
            "Stir in turmeric powder and salt.",
            "Add the softened poha and fried peanuts. Toss gently on low heat for 3-4 minutes.",
            "Turn off the heat, squeeze fresh lemon juice, and garnish with fresh coriander."
        ],
        "substitutions": {
            "nuts": {"replace": "Peanuts", "with": "Roasted Green Peas", "cost_diff": -2},
            "mustard": {"replace": "Mustard Seeds", "with": "Cumin Seeds", "cost_diff": 0}
        }
    },
    {
        "id": "masala_dosa",
        "name": "Masala Dosa",
        "type": "breakfast",
        "category": "Vegan",
        "allergens": ["mustard"],
        "image": "assets/dosa.png",
        "nutrition": {"calories": 387, "protein": 7, "carbs": 62, "fat": 13},
        "ingredients": [
            {"name": "Dosa Batter (Rice & Urad Dal)", "amount": 250, "unit": "ml", "category": "Grains & Spices", "cost": 30},
            {"name": "Potato", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 10},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Mustard Seeds", "amount": 3, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Ginger-Garlic Paste", "amount": 10, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Green Chillies", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 2},
            {"name": "Turmeric Powder", "amount": 2, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Cooking Oil", "amount": 20, "unit": "ml", "category": "Grains & Spices", "cost": 4}
        ],
        "prep_steps": [
            "Bring fermented dosa batter to room temperature.",
            "Boil the potatoes, peel, and mash them coarsely.",
            "Finely slice the onion and chop the green chillies."
        ],
        "cook_steps": [
            "Heat oil in a pan, add mustard seeds and green chillies. Sauté for 30 seconds.",
            "Add sliced onions and ginger-garlic paste. Cook until translucent.",
            "Stir in turmeric and mashed potatoes. Add water to make a moist potato masala. Cook for 5 minutes.",
            "Heat a non-stick tawa, ladle dosa batter in the center, and spread in a thin circle.",
            "Drizzle oil around the edges, cook until golden and crispy.",
            "Place potato masala in the center, fold the dosa, and serve hot."
        ],
        "substitutions": {
            "mustard": {"replace": "Mustard Seeds", "with": "Cumin Seeds", "cost_diff": 0}
        }
    },
    {
        "id": "aloo_paratha",
        "name": "Aloo Paratha",
        "type": "breakfast",
        "category": "Veg",
        "allergens": ["gluten", "dairy"],
        "image": "assets/paratha.png",
        "nutrition": {"calories": 420, "protein": 9, "carbs": 58, "fat": 16},
        "ingredients": [
            {"name": "Whole Wheat Flour (Atta)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 10},
            {"name": "Potato", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 10},
            {"name": "Ghee", "amount": 20, "unit": "ml", "category": "Dairy & Alternatives", "cost": 15},
            {"name": "Yogurt (Dahi)", "amount": 100, "unit": "g", "category": "Dairy & Alternatives", "cost": 12},
            {"name": "Garam Masala", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Chilli Powder", "amount": 3, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Coriander Leaves", "amount": 10, "unit": "g", "category": "Vegetables", "cost": 2}
        ],
        "prep_steps": [
            "Knead wheat flour with water into a soft dough. Let it rest for 15 minutes.",
            "Boil, peel, and mash potatoes thoroughly (no lumps).",
            "Finely chop coriander leaves. Mix mashed potatoes with garam masala, chilli powder, coriander, and salt."
        ],
        "cook_steps": [
            "Pinch a medium ball from the dough. Roll it into a 3-inch circle.",
            "Place a portion of potato stuffing in the center. Fold the edges to seal the ball.",
            "Roll the stuffed ball gently into a 6-inch flatbread.",
            "Heat a tawa, cook the paratha on both sides, applying ghee until golden spots appear.",
            "Serve hot with a dollop of fresh yogurt."
        ],
        "substitutions": {
            "gluten": {"replace": "Whole Wheat Flour (Atta)", "with": "Gluten-Free Flour (Rice/Ragi)", "cost_diff": 12},
            "dairy": [
                {"replace": "Ghee", "with": "Cooking Oil", "cost_diff": -10},
                {"replace": "Yogurt (Dahi)", "with": "Vegan Coconut Yogurt", "cost_diff": 25}
            ]
        }
    },
    {
        "id": "besan_chilla",
        "name": "Besan Chilla",
        "type": "breakfast",
        "category": "Vegan",
        "allergens": [],
        "image": "assets/chilla.png",
        "nutrition": {"calories": 280, "protein": 11, "carbs": 38, "fat": 9},
        "ingredients": [
            {"name": "Gram Flour (Besan)", "amount": 120, "unit": "g", "category": "Grains & Spices", "cost": 12},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Tomato", "amount": 0.5, "unit": "pc", "category": "Vegetables", "cost": 3},
            {"name": "Carrot", "amount": 0.5, "unit": "pc", "category": "Vegetables", "cost": 4},
            {"name": "Ajwain (Carom Seeds)", "amount": 2, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Green Chillies", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 1},
            {"name": "Coriander Leaves", "amount": 10, "unit": "g", "category": "Vegetables", "cost": 2},
            {"name": "Cooking Oil", "amount": 15, "unit": "ml", "category": "Grains & Spices", "cost": 3}
        ],
        "prep_steps": [
            "Whisk gram flour with water to make a smooth, pouring-consistency batter.",
            "Finely chop onions, tomatoes, green chillies, and coriander. Grate the carrot.",
            "Mix all vegetables and ajwain into the batter with salt."
        ],
        "cook_steps": [
            "Heat a seasoned tawa, drizzle a few drops of oil.",
            "Pour a ladle of batter and spread it gently from the center outwards.",
            "Drizzle oil around the edges and cook on medium flame until golden brown.",
            "Flip and cook the other side for 2 minutes. Serve hot with green chutney."
        ],
        "substitutions": {}
    },

    # --- LUNCHES ---
    {
        "id": "dal_tadka",
        "name": "Yellow Dal Tadka & Rice",
        "type": "lunch",
        "category": "Vegan",
        "allergens": ["mustard"],
        "image": "assets/dal_rice.png",
        "nutrition": {"calories": 480, "protein": 14, "carbs": 76, "fat": 12},
        "ingredients": [
            {"name": "Toor Dal (Pigeon Peas)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 18},
            {"name": "Basmati Rice", "amount": 200, "unit": "g", "category": "Grains & Spices", "cost": 22},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Tomato", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 6},
            {"name": "Cumin Seeds (Jeera)", "amount": 10, "unit": "g", "category": "Grains & Spices", "cost": 3},
            {"name": "Garlic", "amount": 15, "unit": "g", "category": "Vegetables", "cost": 4},
            {"name": "Ginger", "amount": 10, "unit": "g", "category": "Vegetables", "cost": 3},
            {"name": "Mustard Seeds", "amount": 3, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Turmeric Powder", "amount": 3, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Cooking Oil", "amount": 20, "unit": "ml", "category": "Grains & Spices", "cost": 4}
        ],
        "prep_steps": [
            "Wash and soak Toor dal for 20 minutes.",
            "Wash Basmati rice and soak for 15 minutes.",
            "Chop onion, tomato, garlic, and ginger."
        ],
        "cook_steps": [
            "Pressure cook dal with water, turmeric, and salt for 3-4 whistles.",
            "Boil Basmati rice with cumin seeds and a splash of oil until fluffy.",
            "Heat oil in a pan, add cumin and mustard seeds. Let them crackle.",
            "Add chopped garlic, ginger, and onions. Sauté until golden.",
            "Add tomatoes and turmeric, cook until mushy. Pour in cooked, mashed dal.",
            "Simmer for 5 minutes, adjust salt, and garnish with fresh coriander."
        ],
        "substitutions": {
            "mustard": {"replace": "Mustard Seeds", "with": "Cumin Seeds", "cost_diff": 0}
        }
    },
    {
        "id": "paneer_butter_masala",
        "name": "Paneer Butter Masala & Roti",
        "type": "lunch",
        "category": "Veg",
        "allergens": ["dairy", "gluten", "nuts"],
        "image": "assets/paneer.png",
        "nutrition": {"calories": 620, "protein": 22, "carbs": 65, "fat": 31},
        "ingredients": [
            {"name": "Paneer (Cottage Cheese)", "amount": 200, "unit": "g", "category": "Dairy & Alternatives", "cost": 90},
            {"name": "Whole Wheat Flour (Atta)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 10},
            {"name": "Butter", "amount": 25, "unit": "g", "category": "Dairy & Alternatives", "cost": 15},
            {"name": "Fresh Cream", "amount": 40, "unit": "ml", "category": "Dairy & Alternatives", "cost": 18},
            {"name": "Tomato", "amount": 3, "unit": "pc", "category": "Vegetables", "cost": 18},
            {"name": "Cashews", "amount": 30, "unit": "g", "category": "Nuts & Seeds", "cost": 25},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Ginger-Garlic Paste", "amount": 15, "unit": "g", "category": "Grains & Spices", "cost": 3},
            {"name": "Kasuri Methi", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2}
        ],
        "prep_steps": [
            "Cut paneer into cubes.",
            "Knead wheat flour into dough for Rotis.",
            "Soak cashews in hot water for 15 minutes, then blend with tomatoes to a smooth paste."
        ],
        "cook_steps": [
            "Heat butter in a pan, add chopped onions and ginger-garlic paste. Sauté until light brown.",
            "Add the tomato-cashew purée and cook until oil separates.",
            "Add chilli powder, garam masala, salt, and water. Simmer.",
            "Add paneer cubes and fresh cream. Cook on low heat for 5 minutes.",
            "Finish with crushed kasuri methi.",
            "Roll out rotis and toast on a hot tawa. Serve hot with the gravy."
        ],
        "substitutions": {
            "dairy": [
                {"replace": "Paneer (Cottage Cheese)", "with": "Organic Tofu", "cost_diff": -10},
                {"replace": "Butter", "with": "Vegan Butter / Oil", "cost_diff": 5},
                {"replace": "Fresh Cream", "with": "Coconut Cream", "cost_diff": 10}
            ],
            "gluten": {"replace": "Whole Wheat Flour (Atta)", "with": "Basmati Rice (Steamed)", "cost_diff": 5},
            "nuts": {"replace": "Cashews", "with": "Melon Seeds (Magaz)", "cost_diff": -15}
        }
    },
    {
        "id": "chole_rice",
        "name": "Pindi Chole & Basmati Rice",
        "type": "lunch",
        "category": "Vegan",
        "allergens": [],
        "image": "assets/chole.png",
        "nutrition": {"calories": 540, "protein": 15, "carbs": 85, "fat": 14},
        "ingredients": [
            {"name": "Chickpeas (Kabuli Chana)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 15},
            {"name": "Basmati Rice", "amount": 200, "unit": "g", "category": "Grains & Spices", "cost": 22},
            {"name": "Onion", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 10},
            {"name": "Tomato", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 12},
            {"name": "Ginger-Garlic Paste", "amount": 15, "unit": "g", "category": "Grains & Spices", "cost": 3},
            {"name": "Chole Masala Spice", "amount": 15, "unit": "g", "category": "Grains & Spices", "cost": 5},
            {"name": "Tea Bag (for dark color)", "amount": 1, "unit": "pc", "category": "Grains & Spices", "cost": 2},
            {"name": "Cooking Oil", "amount": 25, "unit": "ml", "category": "Grains & Spices", "cost": 5}
        ],
        "prep_steps": [
            "Soak chickpeas overnight (8 hours) in water.",
            "Wash and soak Basmati rice for 20 minutes.",
            "Chop onions and purée the tomatoes."
        ],
        "cook_steps": [
            "Boil chickpeas in a pressure cooker with salt, water, and a black tea bag for 6-7 whistles until completely soft.",
            "Cook Basmati rice in a separate pot and set aside.",
            "Heat oil in a heavy pot, sauté chopped onions until deep golden brown.",
            "Add ginger-garlic paste and sauté for 1 minute.",
            "Stir in tomato purée, chole masala, turmeric, and chilli powder. Cook until oil separates.",
            "Add boiled chickpeas (discard tea bag, keep water) and simmer for 15-20 minutes until the gravy thickens.",
            "Garnish with ginger juliennes and serve with hot rice."
        ],
        "substitutions": {}
    },
    {
        "id": "rajma_rice",
        "name": "Rajma Masala & Rice",
        "type": "lunch",
        "category": "Vegan",
        "allergens": [],
        "image": "assets/rajma.png",
        "nutrition": {"calories": 520, "protein": 16, "carbs": 82, "fat": 13},
        "ingredients": [
            {"name": "Kidney Beans (Rajma)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 20},
            {"name": "Basmati Rice", "amount": 200, "unit": "g", "category": "Grains & Spices", "cost": 22},
            {"name": "Onion", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 10},
            {"name": "Tomato", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 12},
            {"name": "Coriander Powder", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Ginger-Garlic Paste", "amount": 15, "unit": "g", "category": "Grains & Spices", "cost": 3},
            {"name": "Cooking Oil", "amount": 20, "unit": "ml", "category": "Grains & Spices", "cost": 4}
        ],
        "prep_steps": [
            "Soak kidney beans overnight (8 hours).",
            "Soak Basmati rice for 15 minutes.",
            "Chop onions and tomatoes finely."
        ],
        "cook_steps": [
            "Pressure cook rajma with salt and water for 6 whistles until soft.",
            "Cook Basmati rice in boiling water, drain, and set aside.",
            "Heat oil in a pan, sauté onions until golden.",
            "Add ginger-garlic paste, then tomatoes. Cook until mushy.",
            "Stir in coriander powder, turmeric, and red chilli powder. Add boiled rajma with its stock.",
            "Simmer on medium-low for 15 minutes, mashing a few beans to thicken the gravy.",
            "Serve hot with steamed Basmati rice."
        ],
        "substitutions": {}
    },

    # --- DINNERS ---
    {
        "id": "chicken_tikka_naan",
        "name": "Chicken Tikka Masala & Naan",
        "type": "dinner",
        "category": "Non-Veg",
        "allergens": ["dairy", "gluten", "nuts"],
        "image": "assets/chicken.png",
        "nutrition": {"calories": 710, "protein": 38, "carbs": 72, "fat": 28},
        "ingredients": [
            {"name": "Boneless Chicken", "amount": 250, "unit": "g", "category": "Meat & Seafood", "cost": 100},
            {"name": "Yogurt (Dahi)", "amount": 80, "unit": "g", "category": "Dairy & Alternatives", "cost": 10},
            {"name": "Butter", "amount": 20, "unit": "g", "category": "Dairy & Alternatives", "cost": 12},
            {"name": "Fresh Cream", "amount": 30, "unit": "ml", "category": "Dairy & Alternatives", "cost": 15},
            {"name": "Cashews", "amount": 25, "unit": "g", "category": "Nuts & Seeds", "cost": 20},
            {"name": "Refined Flour (Maida)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 10},
            {"name": "Tomato Purée", "amount": 100, "unit": "ml", "category": "Vegetables", "cost": 15},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Kashmiri Mirch Spice", "amount": 10, "unit": "g", "category": "Grains & Spices", "cost": 3}
        ],
        "prep_steps": [
            "Cut chicken into bite-sized pieces and marinate with yogurt, ginger-garlic, spice mix, and oil.",
            "Knead flour with yogurt and a pinch of baking powder. Rest for 1 hour to rise.",
            "Soak cashews in hot water."
        ],
        "cook_steps": [
            "Pan-sear marinated chicken on high heat for 6-8 minutes until charred. Set aside.",
            "Blend cashews and tomato purée to a fine cream.",
            "Heat butter in a pan, cook onions, then pour in the tomato-cashew mix and spices.",
            "Add chicken pieces and simmer for 8 minutes. Stir in fresh cream.",
            "Roll naan dough and bake on a hot tawa, flipping to cook directly on flame.",
            "Brush naan with butter and serve immediately with chicken tikka masala."
        ],
        "substitutions": {
            "dairy": [
                {"replace": "Yogurt (Dahi)", "with": "Vegan Coconut Yogurt", "cost_diff": 20},
                {"replace": "Butter", "with": "Cooking Oil", "cost_diff": -8},
                {"replace": "Fresh Cream", "with": "Cashew/Coconut Cream", "cost_diff": 10}
            ],
            "gluten": {"replace": "Refined Flour (Maida)", "with": "Basmati Rice (Steamed)", "cost_diff": 5},
            "nuts": {"replace": "Cashews", "with": "Pumpkin Seeds", "cost_diff": -12}
        }
    },
    {
        "id": "bhindi_roti",
        "name": "Bhindi Masala & Roti",
        "type": "dinner",
        "category": "Vegan",
        "allergens": ["gluten"],
        "image": "assets/bhindi.png",
        "nutrition": {"calories": 360, "protein": 8, "carbs": 52, "fat": 12},
        "ingredients": [
            {"name": "Okra (Bhindi)", "amount": 250, "unit": "g", "category": "Vegetables", "cost": 25},
            {"name": "Whole Wheat Flour (Atta)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 10},
            {"name": "Onion", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 10},
            {"name": "Tomato", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 6},
            {"name": "Cumin Seeds", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Amchur (Mango Powder)", "amount": 4, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Cooking Oil", "amount": 20, "unit": "ml", "category": "Grains & Spices", "cost": 4}
        ],
        "prep_steps": [
            "Wash okra and wipe dry with a towel (prevents sliminess). Chop into 1-inch pieces.",
            "Knead wheat flour into a soft dough.",
            "Slice onions and chop the tomato."
        ],
        "cook_steps": [
            "Heat oil in a pan, fry okra on medium heat until slightly crisp. Set aside.",
            "In the same pan, add cumin seeds and sliced onions. Cook until light brown.",
            "Add chopped tomatoes, turmeric, chilli powder, and salt. Cook until soft.",
            "Add fried bhindi and amchur powder. Stir and cook uncovered for 8 minutes.",
            "Roll and roast rotis on the tawa. Serve hot with okra."
        ],
        "substitutions": {
            "gluten": {"replace": "Whole Wheat Flour (Atta)", "with": "Basmati Rice (Steamed)", "cost_diff": 5}
        }
    },
    {
        "id": "palak_paneer_roti",
        "name": "Palak Paneer & Roti",
        "type": "dinner",
        "category": "Veg",
        "allergens": ["dairy", "gluten"],
        "image": "assets/palak_paneer.png",
        "nutrition": {"calories": 530, "protein": 21, "carbs": 56, "fat": 23},
        "ingredients": [
            {"name": "Spinach (Palak)", "amount": 250, "unit": "g", "category": "Vegetables", "cost": 20},
            {"name": "Paneer (Cottage Cheese)", "amount": 200, "unit": "g", "category": "Dairy & Alternatives", "cost": 90},
            {"name": "Whole Wheat Flour (Atta)", "amount": 150, "unit": "g", "category": "Grains & Spices", "cost": 10},
            {"name": "Ghee", "amount": 15, "unit": "ml", "category": "Dairy & Alternatives", "cost": 10},
            {"name": "Fresh Cream", "amount": 20, "unit": "ml", "category": "Dairy & Alternatives", "cost": 10},
            {"name": "Garlic", "amount": 15, "unit": "g", "category": "Vegetables", "cost": 4},
            {"name": "Green Chillies", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 2}
        ],
        "prep_steps": [
            "Blanch spinach leaves in boiling water for 2 minutes, shock in ice water, and blend into a green purée.",
            "Cut paneer into cubes.",
            "Knead wheat dough for rotis.",
            "Finely mince the garlic."
        ],
        "cook_steps": [
            "Heat ghee in a pan, sauté minced garlic and green chillies.",
            "Pour in the palak purée, add salt, and simmer for 5 minutes.",
            "Add paneer cubes. Simmer on low for 3 minutes (do not overcook paneer).",
            "Swirl in fresh cream and turn off the flame.",
            "Prepare rotis on the tawa. Serve hot with palak paneer."
        ],
        "substitutions": {
            "dairy": [
                {"replace": "Paneer (Cottage Cheese)", "with": "Organic Tofu", "cost_diff": -10},
                {"replace": "Ghee", "with": "Cooking Oil", "cost_diff": -7},
                {"replace": "Fresh Cream", "with": "Coconut Cream", "cost_diff": 8}
            ],
            "gluten": {"replace": "Whole Wheat Flour (Atta)", "with": "Basmati Rice (Steamed)", "cost_diff": 5}
        }
    },
    {
        "id": "egg_curry_rice",
        "name": "Egg Curry & Rice",
        "type": "dinner",
        "category": "Non-Veg",
        "allergens": ["mustard"],
        "image": "assets/egg_curry.png",
        "nutrition": {"calories": 510, "protein": 20, "carbs": 72, "fat": 15},
        "ingredients": [
            {"name": "Egg", "amount": 3, "unit": "pc", "category": "Meat & Seafood", "cost": 21},
            {"name": "Basmati Rice", "amount": 200, "unit": "g", "category": "Grains & Spices", "cost": 22},
            {"name": "Onion", "amount": 2, "unit": "pc", "category": "Vegetables", "cost": 10},
            {"name": "Tomato Purée", "amount": 80, "unit": "ml", "category": "Vegetables", "cost": 12},
            {"name": "Mustard Oil", "amount": 20, "unit": "ml", "category": "Grains & Spices", "cost": 5},
            {"name": "Ginger-Garlic Paste", "amount": 10, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Garam Masala", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2}
        ],
        "prep_steps": [
            "Boil, peel, and prick eggs with a fork.",
            "Wash and soak Basmati rice for 15 minutes.",
            "Finely chop onions."
        ],
        "cook_steps": [
            "Cook Basmati rice in boiling water, drain and set aside.",
            "Heat mustard oil, fry boiled eggs with a punch of turmeric until blistered. Remove.",
            "In the same oil, fry onions until brown. Add ginger-garlic paste and sauté.",
            "Add tomato purée, chilli powder, coriander, and turmeric. Cook until oil floats.",
            "Add water to form a gravy, simmer, then add fried eggs.",
            "Simmer for 8 minutes. Sprinkle garam masala and serve with hot rice."
        ],
        "substitutions": {
            "mustard": {"replace": "Mustard Oil", "with": "Cooking Oil", "cost_diff": 0}
        }
    },
    {
        "id": "khichdi",
        "name": "Moong Dal Khichdi",
        "type": "dinner",
        "category": "Vegan",
        "allergens": [],
        "image": "assets/khichdi.png",
        "nutrition": {"calories": 340, "protein": 12, "carbs": 54, "fat": 8},
        "ingredients": [
            {"name": "Basmati Rice", "amount": 100, "unit": "g", "category": "Grains & Spices", "cost": 11},
            {"name": "Moong Dal (Yellow Split Lentils)", "amount": 100, "unit": "g", "category": "Grains & Spices", "cost": 12},
            {"name": "Onion", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 5},
            {"name": "Tomato", "amount": 1, "unit": "pc", "category": "Vegetables", "cost": 6},
            {"name": "Ginger", "amount": 10, "unit": "g", "category": "Vegetables", "cost": 3},
            {"name": "Cumin Seeds", "amount": 5, "unit": "g", "category": "Grains & Spices", "cost": 2},
            {"name": "Turmeric Powder", "amount": 2, "unit": "g", "category": "Grains & Spices", "cost": 1},
            {"name": "Cooking Oil", "amount": 15, "unit": "ml", "category": "Grains & Spices", "cost": 3}
        ],
        "prep_steps": [
            "Wash rice and moong dal together. Soak for 15 minutes.",
            "Chop onion, tomato, and mince the ginger."
        ],
        "cook_steps": [
            "Heat oil in a pressure cooker. Add cumin seeds and let them crackle.",
            "Sauté onions and ginger. Add tomatoes and turmeric, cook until soft.",
            "Add the soaked rice and dal. Sauté for 1 minute.",
            "Add water (3.5 times the quantity of rice+dal mix) and salt.",
            "Pressure cook for 4 whistles until mushy and blended.",
            "Serve hot with a drizzle of oil or ghee (optional)."
        ],
        "substitutions": {}
    }
]
