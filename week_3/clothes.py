"""Simple demonstration of a Cloth data object.

This module shows a small, well-documented class suitable for teaching
basic OOP, dataclasses and a small example usage guard.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Cloth:
    """A small value object that describes a cloth item.

    Attributes:
        size: human readable size (e.g. 'M', 'L')
        color: color name
        price: numeric price in the project's currency
        quality: descriptive quality string
    """

    size: str
    color: str
    price: float
    quality: str

    def get_details(self) -> str:
        """Return a human-readable summary of the cloth."""
        return f"Size: {self.size}, Color: {self.color}, Price: {self.price}, Quality: {self.quality}"


def example_clothes() -> List[Cloth]:
    """Build some example Cloth objects for demonstrations or tests."""
    return [
        Cloth("M", "Red", 20.56, "High"),
        Cloth("L", "Blue", 15.99, "Medium"),
        Cloth("S", "Green", 10.00, "Low"),
        Cloth("XL", "Black", 25.00, "High"),
    ]


if __name__ == "__main__":
    # Small demo that prints details for each example cloth.
    for c in example_clothes():
        print(c.get_details())