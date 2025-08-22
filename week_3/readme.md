
# Object-Oriented Programming (OOP) — Theory and Notes

This README is a focused reference for students working through the
Week 3 examples. It explains core OOP concepts used across the
examples and provides short code examples (Python) and guidance for
exercises.

## Quick orientation

Files you will use:
- `clothes.py`        — dataclass example (value object)
- `encapsulation.py`  — shows protected/private attributes and accessors
- `inheritance.py`    — inheritance example (Person / Student)
- `inheritance_project.py` — City subclass examples
- `oop.py`            — constructors and methods (Fruit, Car)
- `polymorphism.py`   — overriding and operator overloading (Point)
- `project/`          — a small Streamlit banking demo (app2.py)

Run a demo from the folder with:

```powershell
python clothes.py
python polymorphism.py
```

## Core terminology

- Class: a blueprint describing fields (attributes) and behavior
  (methods).
- Object (instance): a concrete value created from a class.
- Method: a function defined on a class that operates on instances.
- Attribute: data stored on an object (state).

## The four main OOP principles

### 1) Encapsulation

Encapsulation groups data and behavior and hides internal state. In
Python this is by convention: single underscore `_attr` signals
protected use, double underscore `__attr` triggers name-mangling for
basic privacy.

Example pattern:

```python
class Phone:
	def __init__(self, model, os):
		self.model = model       # public
		self._os = os           # protected (convention)

	def get_os(self):
		return self._os

	def set_os(self, new_os):
		if not isinstance(new_os, str) or not new_os.strip():
			raise ValueError("os must be a non-empty string")
		self._os = new_os
```

Why: it helps maintain invariants and makes code easier to reason
about — callers use the public API rather than touching internals.

### 2) Abstraction

Abstraction means exposing a minimal, meaningful interface and hiding
the rest. Methods that perform higher-level tasks are the abstraction.

Example: a `BankAccount.withdraw()` method validates balance and
updates internal state; callers don't need to know the exact steps.

### 3) Inheritance

Inheritance lets a class reuse behavior from a base class and extend
it. Use `super()` to initialize or call base behavior.

Example:

```python
class Person:
	def __init__(self, name):
		self.name = name

class Student(Person):
	def __init__(self, name, student_id):
		super().__init__(name)
		self.student_id = student_id
```

Best practice: use inheritance when there is a true "is-a" relationship
(Student is a Person). Avoid deep inheritance trees; prefer composition
when appropriate.

### 4) Polymorphism

Polymorphism lets objects of different types be used through a common
interface. Python uses duck typing: "if it walks like a duck and quacks
like a duck...".

Example (method overriding):

```python
class Animal:
	def speak(self):
		return "..."

class Dog(Animal):
	def speak(self):
		return "Woof!"

class Cat(Animal):
	def speak(self):
		return "Meow!"

for a in (Dog(), Cat()):
	print(a.speak())
```

## Operator overloading (special methods)

Python classes can implement special methods like `__add__`, `__sub__`,
`__str__` to integrate with language features.

Example: a simple `Point` supporting addition:

```python
from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int

	def __add__(self, other: "Point") -> "Point":
		return Point(self.x + other.x, self.y + other.y)
```

Operator overloading improves readability when the operation has a
natural meaning for the type.

## Composition vs Inheritance

- Composition: a class *has* other objects as attributes (e.g. a
  `Garage` has `Car` instances). Use composition to assemble behavior
  from components.
- Inheritance: use when there is a subtype relationship and you want to
  reuse or specialize behavior.

Example composition:

```python
class Garage:
	def __init__(self):
		self.cars = []

	def add_car(self, car):
		self.cars.append(car)

	def list_cars(self):
		return [c.name for c in self.cars]
```

## Best practices (short)

- Keep classes focused (single responsibility).
- Validate inputs in constructors or setters.
- Keep side effects out of import time; use `if __name__ == "__main__"`
  for demos.
- Document the public API of the class with docstrings.
- Prefer composition over inheritance when appropriate.

## How to use these examples in class

1. Read the example file and run it. Observe output.
2. Modify a small piece of code (e.g., add a method) and re-run.
3. Try the exercises in `exercises.md` and then run the `tests/run_tests.py`
   smoke checks.

