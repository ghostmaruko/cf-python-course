recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))

    ingredients = []
    n = int(input("How many ingredients does the recipe have? "))

    for i in range(n):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)  # ← QUI la fix

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe


n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)


for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    ingredients_count = len(recipe["ingredients"])

    if cooking_time < 10 and ingredients_count < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and ingredients_count >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and ingredients_count < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    print("\nRecipe:", recipe["name"])
    print("Cooking Time:", cooking_time, "minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print("-", ingredient)
    print("Difficulty:", difficulty)


ingredients_list.sort()

print("\nAll ingredients used:")
for ingredient in ingredients_list:
    print("-", ingredient)