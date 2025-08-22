"""Basic OOP examples: constructors, methods and small demos.

This module is written for classroom use. Each class contains a short
docstring and the file uses a ``__main__`` demo guard to avoid printing
when imported in tests.
"""
from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    color: str

    def describe(self) -> str:
        """Return a sentence describing the fruit."""
        return f"{self.name.capitalize()} is {self.color}."


@dataclass
class Car:
    name: str
    brand: str
    model: str
    color: str
    engine: str

    def start(self) -> str:
        return f"{self.name} ({self.brand} {self.model}) starts with {self.engine}."

    def accelerate(self) -> str:
        return f"{self.name} is accelerating."


if __name__ == "__main__":
    # Small demonstration
    apple = Fruit("apple", "red")
    print(apple.describe())

    car1 = Car("Mercedes", "Mercedes-Benz", "A-class", "Black", "2.0L Turbo")
    print(car1.start())