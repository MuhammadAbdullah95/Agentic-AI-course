# Practice Problems (With `raise`)

## 1. Modular Programming
1. Create a module `math_utils.py` that contains:
   - A function `add(a, b)` to return the sum of two numbers.
   - A function `is_prime(n)` that:
     - Raises a `ValueError` if `n` is less than 2.
     - Otherwise checks if the number is prime.
2. In another file `main.py`, import the module and:
   - Ask the user for two numbers, print their sum.
   - Ask the user for a number, check if it’s prime, and handle the `ValueError`.

---

## 2. File Handling (Without `with` Statement)
1. Write a program that:
   - Opens (or creates) a file called `students.txt` in write mode.
   - Takes student names from the user (stop when they type `"exit"`).
   - If the name is less than 3 characters, **raise** a `ValueError` saying `"Name too short"`.
   - Writes valid names to the file.
   - Closes the file manually.
2. Reopen the file in read mode and display all names.
3. Handle exceptions for:
   - File not found
   - Short names (raised exception)
   - Input/output errors

---

## 3. Combined Problem – Modular + File + Exception Handling + Raise
1. Create a module `student_utils.py` that contains:
   - `save_students(filename, students_list)`:
     - Raises a `ValueError` if `students_list` is empty.
     - Saves student names to a file.
   - `load_students(filename)`:
     - Raises a `FileNotFoundError` if the file does not exist.
     - Reads and returns all names from the file.
2. In `main.py`:
   - Take student names from the user (until `"exit"`).
   - Save them using `save_students()`.
   - Load and print them using `load_students()`.
   - Use `try-except` to handle:
     - File not found
     - Empty file (raised error)
     - Any unexpected errors
