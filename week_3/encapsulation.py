"""Small demonstration showing encapsulation conventions in Python.

This module illustrates public, protected and private attributes and
accessor methods. It is intentionally simple for teaching.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Phone:
    """A tiny example class for teaching encapsulation.

    Note: Python's access controls are by convention only. Attributes
    prefixed with an underscore are considered protected; double-underscore
    name-mangled attributes are private to the class.
    """

    model: str
    _os: str

    def get_os(self) -> str:
        """Return the operating system string (reader)."""
        return self._os

    def set_os(self, new_os: str) -> None:
        """Set the operating system (writer).

        A real class would validate the value; this demo keeps it simple.
        """
        self._os = new_os


if __name__ == "__main__":
    p = Phone("iPhone 14", "iOS 18")
    print("Before:", p.get_os())
    p.set_os("iOS 19")
    print("After:", p.get_os())