# Simple calculator: addition and subtraction

# Get user inputs
a = input("Enter the first number: ")
b = input("Enter the second number: ")
operator = input("Enter an operator (+ or -): ")

# Convert inputs to numbers
a = float(a)
b = float(b)

# Decide which operation to perform
if operator == "+":
    result = a + b
    print("Result:", result)

elif operator == "-":
    result = a - b
    print("Result:", result)

else:
    print("Unknown operator")
