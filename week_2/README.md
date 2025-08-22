# Week 2 — Lists, Tuples, Control Flow, Functions, Exceptions & File I/O

This folder is a compact learning module for beginners. It collects short exercises, reference code, and worked solutions to help students understand core Python concepts used in small programs.

Contents (important files)
- `calculate.py` — tiny utility module with basic arithmetic functions (well-documented).
- `main.py` — example script that imports and uses the functions from `calculate.py`.
- `user_information.py`, `user_information.txt` — simple example data and how to structure data in Python.
- `assignment_1.md` — conditional logic (if/else) assignment and sample code.
- `assignment_2.md` — lists & tuples assignment with four problems.
- `assignment_2_solutions.py` — fully commented solutions for `assignment_2.md` (run to see expected outputs).

How to use this folder
- Read the theory sections below to understand the concepts.
- Try the exercises in `assignment_1.md` and `assignment_2.md` yourself.
- Run `assignment_2_solutions.py` to compare your answers with the reference output:

```powershell
python "week_2\assignment_2_solutions.py"
```

Learning objectives
- Understand Python lists and tuples and common operations.
- Practice conditional logic and control flow (`if`, `for`, `while`).
- Write simple functions and handle exceptions.
- Read and write simple files and organize code into modules.

## Theory — Lists

What is a list?
- A list is an ordered, mutable collection of values. Lists can hold different data types simultaneously.

Common operations
- Create: `lst = [1, 2, 3]`
- Access: `lst[0]` (first element), `lst[-1]` (last element)
- Append: `lst.append(4)` — add an element to the end
- Insert: `lst.insert(1, 9)` — insert at a position
- Remove by value: `lst.remove(2)` — removes first matching value (raises ValueError if not found)
- Pop by index: `lst.pop()` or `lst.pop(0)` — returns and removes element
- Slice: `lst[1:4]` — get a sublist; `lst[::2]` every 2nd element
- Length: `len(lst)`
- Iteration: `for x in lst: ...`
- Comprehensions: `[x*2 for x in lst if x > 1]` — concise transform + filter

When to use lists
- Use lists when you need an ordered, changeable collection.

Edge cases & tips
- Removing while iterating can be tricky — iterate over a copy or build a new list.
- Use `sorted(lst)` to get a sorted copy; `lst.sort()` sorts in place.

## Theory — Tuples

What is a tuple?
- A tuple is an ordered, immutable collection. Syntax uses parentheses: `t = (1, 2, 3)`.

Key differences from lists
- Immutable: you cannot change elements or assign to `t[0]` — doing so raises a `TypeError`.
- Use tuples for fixed records (e.g., coordinates) or when immutability is desired.
- Tuples are slightly more memory-efficient than lists.

Common tuple operations
- Access elements with indexing and slicing similar to lists.
- Convert between types: `list(t)` and `tuple(lst)`.

Teaching note
- Demonstrate immutability by attempting an assignment inside a `try/except` and explaining the error.

## Theory — Control Flow (if / for / while)

Conditional statements
- `if`, `elif`, `else` are used to choose execution paths.
- Conditions evaluate to `True` or `False`; use logical operators `and`, `or`, `not`.

Example
```python
if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
else:
	grade = 'F'
```

Loops
- `for` loop: iterate over sequences (lists, tuples, strings, ranges)
  - `for x in items:` is the idiomatic form
- `while` loop: repeat until a condition becomes false

Loop control
- `break` stops the loop early
- `continue` skips to the next iteration

Edge cases
- Infinite loops with `while` are a common beginner bug — ensure the loop variable changes.

## Theory — Functions

Why use functions?
- Encapsulate logic, reuse code, improve readability and testability.

Function basics
- Define: `def add(a, b):`
- Docstrings: Describe purpose, args, return value — visible via `help()`.
- Return values: `return` exits the function with a value.

Best practices
- Use descriptive parameter names.
- Keep functions small and single-purpose.

Example
```python
def multiply(x, y):
	"""Return x * y."""
	return x * y
```

## Theory — Exceptions & Error Handling

What are exceptions?
- Exceptions are runtime errors that interrupt normal execution.

Handling exceptions
- Use `try`, `except`, `finally` to handle errors gracefully.

Example
```python
try:
	result = divide(a, b)
except ZeroDivisionError:
	print("Cannot divide by zero")
	result = None
```

When to raise errors
- A function should raise clear exceptions for invalid inputs so callers can handle them.

## Theory — File I/O (Basics)

Reading and writing text files
- Open a file for reading: `with open('file.txt', 'r', encoding='utf-8') as f:`
- Read all text: `data = f.read()`
- Iterate lines: `for line in f:`
- Write to file: `with open('out.txt', 'w', encoding='utf-8') as f: f.write('text')`

Best practices
- Use `with` to ensure files are closed automatically.
- Always specify encoding for portability.

Security note
- Never trust file contents — validate inputs when parsing structured data (CSV, JSON).

## Theory — Modules and Imports

Organising code
- Keep reusable code in modules (Python files) and import them where needed.
- Example: `from calculate import add` imports the `add` function from `calculate.py`.

Python import rules
- Python searches directories on `sys.path` (current directory, virtualenv site-packages, etc.).
- Use packages (folders with `__init__.py`) to group modules.

## Quick debugging & testing tips

- Use `print()` for quick exploration but prefer proper tests for validation.
- Create small unit tests (e.g., using `unittest` or `pytest`) for critical functions.
- For exercises, add assertions to verify outputs match expected values.

## Teaching tips & suggested exercises

- Ask students to modify `assignment_2_solutions.py` for edge cases (empty lists, single-element lists).
- Encourage writing small tests that assert expected outputs.
- Demonstrate refactoring: extract repeated logic into functions and document them.

## Further reading
- Official Python tutorial: https://docs.python.org/3/tutorial/
- Learn more about data structures and algorithms with small, practical tasks.

---


