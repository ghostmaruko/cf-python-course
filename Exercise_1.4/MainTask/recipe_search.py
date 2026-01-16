import pickle


def display_recipe(recipe):
    print("\n📖 Recipe")
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")


def search_ingredient(data):
    print("\nAvailable ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(f"{index}: {ingredient}")

    try:
        choice = int(input("\nSelect ingredient number: "))
        ingredient_searched = data["all_ingredients"][choice]

    except:
        print("Invalid input. Please enter a valid number.")

    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)


# ---------- MAIN PROGRAM ----------

filename = input("Enter the recipe file name: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)

except FileNotFoundError:
    print("File not found.")

else:
    search_ingredient(data)
