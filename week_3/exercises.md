Student Exercises (Week 3) - OOP Concepts

This file contains short exercises for students with suggested solutions.
Use the code in the repository as starting points.

Exercise 1 — Encapsulation (encapsulation.py)
- Task: Add validation to `Phone.set_os()` so it only accepts strings and
  rejects empty values.
- Hint: raise a ValueError for invalid inputs.

Solution (brief):
```
def set_os(self, new_os):
    if not isinstance(new_os, str) or not new_os.strip():
        raise ValueError("os must be a non-empty string")
    self._os = new_os
```

Exercise 2 — Inheritance (inheritance.py)
- Task: Add a new subclass `Teacher` that extends `Person` and includes a
  `subject` field and `teacher_info()` method that returns subject and name.

Solution (brief):
```
@dataclass
class Teacher(Person):
    subject: str

    def teacher_info(self):
        return f"{self.name} teaches {self.subject}"
```

Exercise 3 — Polymorphism and Operator Overloading (polymorphism.py)
- Task: Add a `__mul__` method to `Point` that scales both x and y by
  an integer factor and returns a new Point.

Solution (brief):
```
def __mul__(self, factor: int) -> "Point":
    return Point(self.x * factor, self.y * factor)
```

Exercise 4 — Composition vs Inheritance
- Task: Create a `Garage` class that contains `Car` objects (composition).
  Add `add_car()` and `list_cars()` methods.

Solution (brief):
```
class Garage:
    def __init__(self):
        self.cars = []
    def add_car(self, car: Car):
        self.cars.append(car)
    def list_cars(self):
        return [c.name for c in self.cars]
```

Exercise 5 — Small project task
- Add unit tests for `Point` (addition/subtraction) and for `Student.student_info()`.

Solution hint:
- Use a small pytest file and assert expected results.


"
