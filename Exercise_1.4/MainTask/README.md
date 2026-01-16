Exercise 1.4: File Handling in Python
Learning Goals

Use files to store and retrieve data in Python

Reflection Questions

1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

- File storage is important in Python because it allows data to persist beyond the execution of a script. Without storing data in local files, all information created or modified during runtime would be lost as soon as the program ends. This would make it impossible to build applications that need to remember user input, save progress, or reuse data across multiple runs. File storage enables programs to be more practical, reliable, and closer to real-world applications.

2. In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In - which situations would you choose to use pickles and why?

- Pickles are a way of serializing Python objects into a binary format so they can be saved to a file and later restored to their original state. Using pickle.dump(), complex data structures such as dictionaries, lists, or nested objects can be stored without manually converting them into strings. Pickles are especially useful when working with Python-only applications where performance and ease of storage are important. I would choose to use pickles when I need to quickly save and load structured Python data and when compatibility with other programming languages is not required.

3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

- To find out the current working directory in Python, the function os.getcwd() is used. If I wanted to change the current working directory, I would use os.chdir() and provide the path to the desired directory. These functions are part of the built-in os module, which allows interaction with the operating system.

4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

- To prevent a script from terminating due to an error, I would use try-except blocks to handle potential exceptions gracefully. By wrapping risky code inside a try block and catching specific exceptions in except clauses, the program can continue running even if an error occurs. This approach allows for better error handling, user-friendly messages, and more robust applications. Using else and finally blocks can further improve clarity and control over program flow

5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.

- The course is going well so far, and I feel much more confident with Python fundamentals than when I started. I’m especially proud of being able to structure scripts using functions, handle user input, and work with files to persist data. Building small but complete programs, such as the recipe application, has helped me understand how different concepts fit together.
  One area I still find challenging is designing clean program flow when multiple conditions and exceptions are involved. I would like more practice with error handling, edge cases, and writing more modular code. These are topics I plan to focus on in the next part of the course and during my next mentor call.
