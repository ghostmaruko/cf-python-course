import pickle


def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    return difficulty


def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))

    ingredients = []
    num_ingredients = int(input("How many ingredients? "))

    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)

    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe


# ---------- MAIN PROGRAM ----------

filename = input("Enter the recipe file name: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)

except FileNotFoundError:
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

except:
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

else:
    file.close()

finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


num_recipes = int(input("How many recipes would you like to enter? "))

for i in range(num_recipes):
    print(f"\nEntering recipe {i + 1}")
    recipe = take_recipe()
    recipes_list.append(recipe)

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)


data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

with open(filename, "wb") as file:
    pickle.dump(data, file)

print("\nRecipes saved successfully!")
