# Step 1: Create an empty Recipe structure to show the expected format

recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

# Step 2: Create a list to hold multiple recipes and add the first recipe to it
all_recipes = []
all_recipes.append(recipe_1)
all_recipes

# Step 3: Create another recipe and add it to the list
recipe_2 = {
    "name": "Pancakes",
    "cooking_time": 15,
    "ingredients": ["Flour", "Milk", "Eggs", "Sugar", "Butter"]
}

recipe_3 = {
    "name": "Salad",
    "cooking_time": 10,
    "ingredients": ["Lettuce", "Tomato", "Cucumber", "Olive oil", "Salt"]
}

recipe_4 = {
    "name": "Spaghetti",
    "cooking_time": 20,
    "ingredients": ["Spaghetti", "Tomato sauce", "Olive oil", "Parmesan"]
}

recipe_5 = {
    "name": "Smoothie",
    "cooking_time": 5,
    "ingredients": ["Banana", "Strawberries", "Yogurt", "Honey"]
}

# Step 4: Add the new recipes to the list
all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])
all_recipes

for i, recipe in enumerate(all_recipes, start=1):
    print(f"Recipe {i} ingredients: {recipe['ingredients']}")


