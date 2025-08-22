"""Small polymorphism and operator overloading examples.

Shows method overriding and operator overloading in a concise form.
"""
from dataclasses import dataclass


class Animal:
    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    # Polymorphism demo
    for a in (Dog(), Cat()):
        print(a.speak())

    # Operator overloading demo
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    p3 = p1 + p2
    print(f"p3.x = {p3.x}, p3.y = {p3.y}")
    p4 = p1 - p2
    print(f"p4.x = {p4.x}, p4.y = {p4.y}")
# print(len("Hello, World!"))  # Output: 13

# print(len([1, 2, 3, 4, 5]))  # Output: 5

# print(len((1, 2, 3)))        # Output: 3

# print(len({1: 'one', 2: 'two'}))  # Output: 2
