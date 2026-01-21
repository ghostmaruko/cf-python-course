# Import principali
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connessione al database MySQL
username = "cf_python"
password = "Python123!"
host = "localhost"
database = "task_database"

# Engine e session
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Base dichiarativa
Base = declarative_base()

# Modello Recipe
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')>"

    def __str__(self):
        return (
            f"Recipe ID:\t{self.id}\n"
            f"Name:\t\t{self.name}\n"
            f"Ingredients:\t{self.ingredients}\n"
            f"Cooking Time:\t{self.cooking_time} minutes\n"
            f"Difficulty:\t{self.difficulty}\n"
            + "-"*40
        )

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10:
            self.difficulty = "Medium"
        elif len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# Creazione tabella
Base.metadata.create_all(engine)

# Inserimento ricetta di esempio se il DB è vuoto
if session.query(Recipe).count() == 0:
    sample = Recipe(
        name="Pasta al Pomodoro",
        ingredients="Pasta, Tomato Sauce, Olive Oil, Salt",
        cooking_time=15
    )
    sample.calculate_difficulty()
    session.add(sample)
    session.commit()

# Funzioni principali
def create_recipe():
    name = input("Enter the recipe name: ").strip()
    if len(name) > 50:
        print("Name too long! Max 50 characters.")
        return

    cooking_time = input("Enter cooking time in minutes: ").strip()
    if not cooking_time.isnumeric():
        print("Cooking time must be a number.")
        return
    cooking_time = int(cooking_time)

    ingredients_list = []
    num_ingredients = input("How many ingredients? ").strip()
    if not num_ingredients.isnumeric():
        print("Number of ingredients must be a number.")
        return
    num_ingredients = int(num_ingredients)

    for i in range(num_ingredients):
        ingredient = input(f"Ingredient {i+1}: ").strip()
        ingredients_list.append(ingredient)

    ingredients_str = ", ".join(ingredients_list)

    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!\n")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found in the database.\n")
        return
    print("\nAll Recipes:\n" + "-"*40)
    for recipe in recipes:
        print(recipe)
    print("-"*40 + "\n")

def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes to search.\n")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for row in results:
        for ingredient in row[0].split(", "):
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    if not all_ingredients:
        print("No ingredients found.\n")
        return

    print("Available ingredients:")
    for i, ing in enumerate(all_ingredients, 1):
        print(f"{i}: {ing}")
    selection = input("Select ingredients by numbers (space-separated): ").strip().split()

    try:
        selected_indices = [int(num)-1 for num in selection]
        search_ingredients = [all_ingredients[i] for i in selected_indices]
    except:
        print("Invalid input!")
        return

    from sqlalchemy import or_
    conditions = [Recipe.ingredients.like(f"%{ing}%") for ing in search_ingredients]
    recipes = session.query(Recipe).filter(or_(*conditions)).all()

    if recipes:
        print("\nRecipes found:\n" + "-"*40)
        for recipe in recipes:
            print(recipe)
        print("-"*40 + "\n")
    else:
        print("No recipes match your selection.\n")

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes to edit.\n")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for r in results:
        print(f"{r[0]}: {r[1]}")
    recipe_id = input("Select recipe by ID to edit: ").strip()
    if not recipe_id.isnumeric():
        print("Invalid input.")
        return
    recipe_id = int(recipe_id)

    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_edit:
        print("Recipe not found.")
        return

    print("\nEditing Recipe:")
    print(f"1: Name -> {recipe_to_edit.name}")
    print(f"2: Ingredients -> {recipe_to_edit.ingredients}")
    print(f"3: Cooking Time -> {recipe_to_edit.cooking_time}")

    choice = input("Select attribute to edit (1-3): ").strip()
    if choice == "1":
        new_name = input("New name: ").strip()
        if len(new_name) > 50:
            print("Name too long!")
            return
        recipe_to_edit.name = new_name
    elif choice == "2":
        new_ingredients = input("New ingredients (comma-separated): ").strip()
        recipe_to_edit.ingredients = new_ingredients
    elif choice == "3":
        new_time = input("New cooking time: ").strip()
        if not new_time.isnumeric():
            print("Invalid cooking time!")
            return
        recipe_to_edit.cooking_time = int(new_time)
    else:
        print("Invalid choice!")
        return

    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!\n")

def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes to delete.\n")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for r in results:
        print(f"{r[0]}: {r[1]}")
    recipe_id = input("Select recipe by ID to delete: ").strip()
    if not recipe_id.isnumeric():
        print("Invalid input.")
        return
    recipe_id = int(recipe_id)

    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_delete:
        print("Recipe not found.")
        return

    confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!\n")
    else:
        print("Deletion cancelled.\n")

# Menu principale
def main_menu():
    while True:
        print("\n--- Recipe App Menu ---")
        print("1: Create a new recipe")
        print("2: View all recipes")
        print("3: Search recipes by ingredients")
        print("4: Edit a recipe")
        print("5: Delete a recipe")
        print("Type 'quit' to exit")

        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("Exiting application...")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid option! Try again.")

# Avvio app
if __name__ == "__main__":
    main_menu()
