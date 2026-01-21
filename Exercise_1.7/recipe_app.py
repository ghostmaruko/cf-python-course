# ===== IMPORTS ======
from sqlalchemy import create_engine, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
# =====================

# ===== DB SETUP ======
engine = create_engine('mysql://recipe_user:RecipePass123@localhost/my_database', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# ===== MODEL DEFINITION =====
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255))
    instructions = Column(String(255))

    def __repr__(self):
        return f"<Recipe(name='{self.name}')>"

# ===== CREATE TABLES =====
Base.metadata.create_all(engine)

# ===== UTILITY FUNCTIONS =====
def show_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
    for r in recipes:
        print(f"ID: {r.id} | Name: {r.name} | Ingredients: {r.ingredients} | Instructions: {r.instructions}")

def add_test_recipe():
    test_recipe = Recipe(
        name="Pasta al Pomodoro",
        ingredients="Pasta, Pomodoro, Olio, Sale, Basilico",
        instructions="Cuocere la pasta, preparare il sugo di pomodoro e condire."
    )
    session.add(test_recipe)
    session.commit()
    print(f"Recipe '{test_recipe.name}' added successfully!")

def add_second_recipe():
    second_recipe = Recipe(
        name="Tiramisù",
        ingredients="Savoiardi, Mascarpone, Caffè, Zucchero, Uova, Cacao",
        instructions="Inzuppare i savoiardi nel caffè, alternare strati con crema di mascarpone, spolverare con cacao e refrigerare."
    )
    session.add(second_recipe)
    session.commit()
    print(f"Recipe '{second_recipe.name}' added successfully!")

# ===== INTERACTIVE MENU =====
def menu():
    while True:
        print("\n=== Recipe App Menu ===")
        print("1. Add a new recipe")
        print("2. Show all recipes")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            name = input("Recipe name: ")
            ingredients = input("Ingredients (comma separated): ")
            instructions = input("Instructions: ")
            new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
            session.add(new_recipe)
            session.commit()
            print(f"Recipe '{name}' added successfully!")
        elif choice == "2":
            show_recipes()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

# ===== MAIN =====
if __name__ == "__main__":
    print("Connection and ORM setup successful.")
    print("Tables created successfully.")

    # Add test recipes
    add_test_recipe()
    add_second_recipe()
    show_recipes()

    # Start interactive menu
    menu()
