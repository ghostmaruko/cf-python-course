class Recipe:
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0  # in minutes
        self.difficulty = None

    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for cooking time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, time):
        self.cooking_time = time
        self.difficulty = None  # reset difficulty

    # Add ingredients using variable-length arguments
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    # Update class variable all_ingredients
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    # Getter for ingredients
    def get_ingredients(self):
        return self.ingredients

    # Calculate difficulty based on rules
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    # Getter for difficulty (lazy evaluation)
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    # Search for an ingredient in the recipe
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # String representation of the recipe
    def __str__(self):
        return (
            f"Recipe: {self.name}\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.get_difficulty()}"
        )


# Function to search recipes by ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            print("-" * 40)


# ---- MAIN CODE ----

tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients(
    "Sugar", "Butter", "Eggs", "Vanilla Essence",
    "Flour", "Baking Powder", "Milk"
)
cake.set_cooking_time(50)
print(cake)

smoothie = Recipe("Banana Smoothie")
smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
)
smoothie.set_cooking_time(5)
print(smoothie)

recipes_list = [tea, coffee, cake, smoothie]

for ingredient in ["Water", "Sugar", "Bananas"]:
    print(f"\nRecipes with {ingredient}:")
    recipe_search(recipes_list, ingredient)
