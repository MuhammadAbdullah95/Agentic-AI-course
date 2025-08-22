"""Inheritance examples for teaching (correctly spelled filename).

This module mirrors the previous `inheritence.py` content but uses the
correct spelling for the filename. It demonstrates simple subclassing
with dataclasses.
"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    role: str

    def info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}"


@dataclass
class Student(Person):
    student_id: str
    class_name: str

    def student_info(self) -> str:
        return f"{self.info()}, Student ID: {self.student_id}, Class: {self.class_name}"


if __name__ == "__main__":
    s = Student("John Doe", 20, "Student", "S12345", "Physics 101")
    print(s.student_info())
