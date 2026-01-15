# Exercise 1.3: Functions and Other Operations in Python

## Reflection Questions

---

### 1. Simple travel app using if-elif-else

Below is a simple Python script that asks the user for a travel destination and responds based on predefined options:


destination = input("Where would you like to travel? ").lower()

if destination == "paris":
    print("Enjoy your stay in Paris!")
elif destination == "rome":
    print("Enjoy your stay in Rome!")
elif destination == "berlin":
    print("Enjoy your stay in Berlin!")
else:
    print("Oops, that destination is not currently available.")


This script uses an if-elif-else statement to control the program flow based on user input..

---

2. Explaining logical operators in Python

Logical operators in Python are used to combine conditional statements and evaluate multiple conditions at once.

The three main logical operators are:

- and → returns True if both conditions are true

- or → returns True if at least one condition is true

- not → reverses the result of a condition

For example:

if age >= 18 and has_ticket:
    print("You are allowed to enter.")


Logical operators are useful when making decisions that depend on more than one condition.

---

3. What are functions in Python? When and why are they useful?

Functions in Python are reusable blocks of code designed to perform a specific task.
They help organize code, reduce repetition, and improve readability.

Functions are useful when:

The same logic needs to be reused multiple times

Code becomes complex and needs better structure

A program should be easier to debug and maintain

Using functions makes programs more modular and easier to scale.

4. Progress towards my learning goals

During Exercise 1.3, I made significant progress toward my learning goals.
I improved my understanding of conditional statements, loops, and functions by applying them in practical tasks such as building a recipe management program.

I also practiced debugging real Python errors, which helped me better understand data types and program flow.
Overall, I feel more confident writing structured Python scripts and breaking down problems into smaller, manageable parts.
These skills will be valuable as I continue working on more complex projects in the course.