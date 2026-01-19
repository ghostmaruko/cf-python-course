import mysql.connector


# =========================
# Database connection
# =========================
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS recipes_db")
cursor.execute("USE recipes_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)
""")

conn.commit()


# =========================
# Utility functions
# =========================
def calculate_difficulty(cooking_time, ingredients):
    """
    Calculates recipe difficulty based on cooking time and number of ingredients.
    """
    num_ingredients = len(ingredients)

    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"


# =========================
# CRUD functions
# =========================
def create_recipe(conn, cursor):
    """
    Creates a new recipe and stores it in the database.
    """
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients_list = input(
        "Enter ingredients separated by comma: "
    ).split(", ")

    difficulty = calculate_difficulty(cooking_time, ingredients_list)
    ingredients_str = ", ".join(ingredients_list)

    cursor.execute(
        """
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
        """,
        (name, ingredients_str, cooking_time, difficulty)
    )
    conn.commit()

    print(f"Recipe '{name}' added successfully!")


def search_recipe(conn, cursor):
    """
    Searches for recipes by ingredient.
    """
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = []

    for row in results:
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    choice = int(input("Select an ingredient by number: "))
    search_ingredient = all_ingredients[choice - 1]

    cursor.execute(
        """
        SELECT * FROM Recipes
        WHERE ingredients LIKE %s
        """,
        (f"%{search_ingredient}%",)
    )

    recipes = cursor.fetchall()

    print("\nRecipes found:")
    for recipe in recipes:
        print(recipe)


def update_recipe(conn, cursor):
    """
    Updates an existing recipe.
    """
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("No recipes found.")
        return

    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    recipe_id = int(input("\nEnter the ID of the recipe to update: "))

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_name = input("Enter new recipe name: ")
        cursor.execute(
            "UPDATE Recipes SET name = %s WHERE id = %s",
            (new_name, recipe_id)
        )

    elif choice == "2":
        new_time = int(input("Enter new cooking time: "))

        cursor.execute(
            "SELECT ingredients FROM Recipes WHERE id = %s",
            (recipe_id,)
        )
        ingredients = cursor.fetchone()[0].split(", ")

        difficulty = calculate_difficulty(new_time, ingredients)

        cursor.execute(
            """
            UPDATE Recipes
            SET cooking_time = %s, difficulty = %s
            WHERE id = %s
            """,
            (new_time, difficulty, recipe_id)
        )

    elif choice == "3":
        new_ingredients = input(
            "Enter new ingredients separated by comma: "
        ).split(", ")

        ingredients_str = ", ".join(new_ingredients)

        cursor.execute(
            "SELECT cooking_time FROM Recipes WHERE id = %s",
            (recipe_id,)
        )
        cooking_time = cursor.fetchone()[0]

        difficulty = calculate_difficulty(cooking_time, new_ingredients)

        cursor.execute(
            """
            UPDATE Recipes
            SET ingredients = %s, difficulty = %s
            WHERE id = %s
            """,
            (ingredients_str, difficulty, recipe_id)
        )

    else:
        print("Invalid choice.")
        return

    conn.commit()
    print("Recipe updated successfully!")


def delete_recipe(conn, cursor):
    """
    Deletes a recipe from the database.
    """
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("No recipes found.")
        return

    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    recipe_id = int(input("\nEnter the ID of the recipe to delete: "))

    cursor.execute(
        "DELETE FROM Recipes WHERE id = %s",
        (recipe_id,)
    )
    conn.commit()

    print("Recipe deleted successfully!")


# =========================
# Main menu
# =========================
def main_menu(conn, cursor):
    """
    Displays the main menu.
    """
    while True:
        print("\n--- Recipe App Menu ---")
        print("1. Create a Recipe")
        print("2. Search a Recipe by Ingredient")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    cursor.close()
    conn.close()


# =========================
# Program start
# =========================
if __name__ == "__main__":
    main_menu(conn, cursor)
