# Exercise 1.1 – Python Base Setup

## Overview

In this exercise, I set up a Python development environment and created a basic Python script to practice working with virtual environments, user input, and package management. This was the first step towards building my Student Project for the CareerFoundry Python course.

---

## Steps Completed

1. **Installed Python 3.13.1**

   - Verified installation with `python --version`.

2. **Created a base virtual environment**

   - Environment name: `cf-python-base`
   - Activated the environment and installed `ipython`.

3. **Created a Python script (`add.py`)**

   - Script prompts the user to input two numbers.
   - Adds the numbers and prints the result.
   - Verified functionality by running the script in the terminal.

4. **Set up IPython shell**

   - Installed IPython in the virtual environment.
   - Verified installation with the `ipython` command.

5. **Generated `requirements.txt`**

   - Used `pip freeze > requirements.txt` to export all installed packages.

6. **Created a copy of the environment**

   - Environment name: `cf-python-copy`
   - Installed all packages from `requirements.txt`.
   - Verified with `pip list` and `ipython`.

7. **Organized deliverables for GitHub**
   - Folder: `Exercise 1.1`
   - Files included:
     - `add.py`
     - `requirements.txt`
     - `README.md`
     - Learning journal (`python-for-web-developers-learning-journal.docx`)
     - Screenshots of each step

---

## How to Run the Script

1. Activate the virtual environment:

```powershell
.\cf-python-base\Scripts\Activate.ps1
```
2. Run th escript
    python add.py

3. Follow the prompts to enter two numbers; the sum will be displayed.

---

## Learning Reflection

Learned how to set up virtual environments and manage dependencies in Python.

Practiced writing a simple Python script that interacts with user input.

Learned how to export packages and replicate environments using requirements.txt.

Gained familiarity with IPython and its enhanced interactive shell features.

Learned how to organize files and folders for a GitHub repository.