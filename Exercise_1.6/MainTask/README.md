## 📝 Exercise 1.6: Connecting to Databases in Python

### Learning Goals
- Create a MySQL database for the Recipe app  
- Connect Python to a database using `mysql-connector-python`  
- Perform basic database operations (create database, tables, insert, update, delete data)

---

## Reflection Questions

### 1. What are databases and what are the advantages of using them?

A database is a structured way to store and manage data so it can be easily accessed, updated, and reused. Instead of keeping data only in memory or in simple files, databases allow data to persist even after a program stops running.

The main advantages of using databases are:
- **Data persistence**: data is saved permanently  
- **Organization**: data is stored in tables with clear structure  
- **Scalability**: databases can handle large amounts of data efficiently  
- **Security**: access to data can be controlled with users and permissions  
- **Efficiency**: databases allow fast searching, filtering, and updating of data  

Using a database makes an application more reliable and closer to real-world software.

---

### 2. List 3 data types that can be used in MySQL and describe them briefly:

| Data type | Definition |
|----------|------------|
| `VARCHAR(n)` | Stores text strings with a maximum length of `n` characters |
| `INT` | Stores whole numbers (integers) |
| `FLOAT` | Stores decimal numbers, useful for prices or measurements |

---

### 3. In what situations would SQLite be a better choice than MySQL?

SQLite is a better choice when working on small projects, prototypes, or applications that do not need a dedicated database server. It is lightweight, easy to set up, and stores the database in a single file.

SQLite is especially useful for:
- Small desktop applications  
- Learning and testing  
- Projects with low concurrency  
- Applications that do not require multiple users accessing the database at the same time  

MySQL, on the other hand, is more suitable for larger, multi-user applications.

---

### 4. Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?

JavaScript and Python are both high-level languages, but they are designed with different goals in mind. JavaScript is mainly used for web development and is event-driven, while Python focuses on readability and simplicity.

Compared to JavaScript, Python:
- Has a cleaner and more readable syntax  
- Requires less boilerplate code  
- Is easier to learn for beginners  
- Is commonly used for scripting, automation, data analysis, and backend development  

JavaScript is more tightly integrated with the browser, while Python is more versatile across different domains.

---

### 5. Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?

One limitation of Python is that it is generally slower than compiled languages because it is interpreted. This can be an issue for performance-critical applications.

Another limitation is that Python is not ideal for mobile app development and low-level system programming. Also, managing dependencies and environments can sometimes be challenging for beginners.

Despite these limitations, Python is a very powerful language due to its simplicity, large ecosystem of libraries, and strong community support.
