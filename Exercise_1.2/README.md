# Exercise 1.2: Data Types in Python

## Learning Goals

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

---

## Practice Tasks Overview

### Task 1: Compound Interest Calculation

- Read values from a text file
- Convert strings to float
- Calculate compounded principal
- Capture screenshots of the shell for each step

### Task 2: Tuples

- Store world population data in a tuple
- Slice one-third of the data
- Find the maximum in the slice

### Task 3: Lists

- Store Ford 2020 vehicles in a list
- Add missing element ("Mustang")
- Sort alphabetically

### Task 4: Strings

- Work out slicing on a concatenated string
- Record results in a text file

### Task 5: Dictionaries

- Create a dictionary of months with names as keys and numbers as values
- Clear the original lists
- Extract keys into a list and sort alphabetically

### Task 6: Recipe App

- Create `recipe_1` dictionary with keys: `name`, `cooking_time`, `ingredients`
- Store all recipes in a sequential outer list `all_recipes`
- Add 5 recipes in total
- Print ingredients of each recipe

---

## Practice Task 6: Recipe App – Data Structure Justification

### Choice of data structure for a single recipe

I chose a dictionary for each recipe because it allows each attribute (name, cooking time, ingredients) to be clearly associated with a key. This makes the data self-explanatory, easily accessible, and flexible enough to add new attributes without changing the overall structure.

### Choice of data structure for all recipes

I chose a list to store all recipes because it maintains the insertion order, allows sequential access, and can be easily modified to add, remove, or update recipes as needed.

---

## Reflection Questions

1. **iPython Shell vs Default Python Shell:**

   - iPython provides syntax highlighting, auto-completion, and better interactive output display.
   - It allows running multiple commands without restarting the session.
   - You can use magic commands (like `%timeit`) and easy history navigation.

2. **Python Data Types:**  
   | Data type | Definition | Scalar or Non-Scalar? |
   |-----------|------------|---------------------|
   | int | Integer numbers | Scalar |
   | float | Decimal numbers | Scalar |
   | list | Ordered collection of items | Non-Scalar |
   | dict | Collection of key-value pairs | Non-Scalar |

3. **Difference between lists and tuples:**

   - Lists are mutable: you can change, add, or remove elements.
   - Tuples are immutable: once created, they cannot be modified.
   - Tuples are typically used when the data should remain constant and hashable, e.g., as dictionary keys.

4. **Data structure choice for a language-learning flashcard app:**
   - Each flashcard can be stored as a dictionary: `{"word": str, "definition": str, "category": str}`.
   - All flashcards can be stored in a list to maintain order and allow additions/removals.
   - This approach provides flexibility for expanding the app with new features, like quizzes or categories.
