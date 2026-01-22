# Exercise 1.5: Object-Oriented Programming in Python  
## Learning Journal

- Apply object-oriented programming concepts to the Recipe app

---

## Reflection Questions

### 1. In your own words, what is object-oriented programming? What are the benefits of OOP?

Object-oriented programming (OOP) is a programming paradigm that organizes code around **objects** instead of only functions or variables. Objects combine **data (attributes)** and **behavior (methods)** into a single structure. This makes programs easier to understand because they are modeled in a way that is similar to real-world concepts.

One of the main benefits of OOP is **code reusability**. By using classes, we can create templates that can be reused multiple times. OOP also improves **maintainability**, because code is more modular and changes in one part are less likely to affect others. Another important benefit is **scalability**: as an application grows, OOP helps keep the code organized and readable. Overall, OOP helps developers write cleaner, more structured, and easier-to-manage code.

---

### 2. What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.

In Python, a **class** is like a blueprint or template that defines what an object should look like. It describes the attributes and methods that the objects created from it will have. An **object** is an instance of a class, meaning a concrete version created from that blueprint.

For example, we can think of a class called `Recipe`. This class defines properties such as `name`, `ingredients`, and `cooking_time`. Each individual recipe (for example, “Pasta Carbonara” or “Vegetable Soup”) is an object created from the `Recipe` class. While all recipes share the same structure, each object contains its own specific data. This makes it easy to manage multiple recipes using the same class definition.

---

### 3. OOP Concepts

#### Inheritance

Inheritance is an OOP concept that allows one class to **inherit attributes and methods from another class**. The original class is called the **parent (or base) class**, and the new class is called the **child (or derived) class**. This helps reduce code duplication and promotes reuse.

For example, if we have a base class called `Recipe`, we could create a child class called `VegetarianRecipe`. The child class automatically has all the attributes and methods of `Recipe`, but it can also add new ones or modify existing behavior. Inheritance makes code more organized and easier to extend without rewriting existing logic.

---

#### Polymorphism

Polymorphism means that **different objects can respond to the same method name in different ways**. In Python, this often happens when multiple classes implement the same method but with different behavior.

For example, both `Recipe` and `BakingRecipe` might have a method called `calculate_time()`. Even though the method name is the same, the logic inside can be different depending on the class. Polymorphism makes code more flexible and allows developers to work with objects in a more generic way, without needing to know their exact type.

---

#### Operator Overloading

Operator overloading allows developers to **define custom behavior for operators** like `+`, `-`, or `==` when they are used with objects. In Python, this is done by implementing special methods such as `__add__()` or `__sub__()` inside a class.

For example, when working with a custom `Height` class, operator overloading can allow two height objects to be added or subtracted using the `+` or `-` operators. This makes the code more readable and intuitive, because objects behave in a way that feels natural. Operator overloading is especially useful when creating classes that represent real-world measurements or values.

---
