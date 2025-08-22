"""Simple test runner for basic smoke checks of the examples.

Run with: python tests/run_tests.py from the `week_3` folder.
This script avoids importing Streamlit-based app modules.
"""

import sys
from pathlib import Path

# Ensure the repository week_3 directory is on sys.path so imports like
# `import clothes` work when this script is executed from tests/.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def fail(msg: str):
    print("FAIL:", msg)
    sys.exit(1)


def main():
    # Import example modules
    # Import modules individually so we can report which import failed
    try:
        import clothes
    except ImportError as e:
        fail(f"Import error clothes: {e}")

    try:
        import polymorphism
    except ImportError as e:
        fail(f"Import error polymorphism: {e}")

    try:
        import oop
    except ImportError as e:
        fail(f"Import error oop: {e}")

    try:
        import inheritance
    except ImportError as e:
        fail(f"Import error inheritance: {e}")

    # clothes
    try:
        items = clothes.example_clothes()
    except AttributeError:
        fail("clothes.example_clothes() is missing")
    except Exception as e:
        fail(f"clothes.example_clothes() error: {e}")
    else:
        if not (isinstance(items, list) and len(items) >= 1):
            fail("clothes.example_clothes() returned unexpected result")

    # polymorphism
    try:
        d = polymorphism.Dog()
        c = polymorphism.Cat()
    except AttributeError:
        fail("polymorphism Dog/Cat classes missing")
    else:
        if d.speak() != "Woof!" or c.speak() != "Meow!":
            fail("polymorphism speak() returned unexpected values")

    try:
        p1 = polymorphism.Point(1, 2)
        p2 = polymorphism.Point(3, 4)
        p3 = p1 + p2
    except Exception as e:
        fail(f"polymorphism Point operations failed: {e}")
    else:
        if (p3.x, p3.y) != (4, 6):
            fail("polymorphism Point addition incorrect")

    # oop
    try:
        f = oop.Fruit("apple", "red")
        desc = f.describe()
    except AttributeError:
        fail("oop Fruit class missing or describe() missing")
    except Exception as e:
        fail(f"oop error: {e}")
    else:
        if not desc.lower().startswith("apple"):
            fail("oop Fruit.describe() returned unexpected text")

    # inheritance
    try:
        s = inheritance.Student("A", 10, "Student", "S1", "C1")
        info = s.student_info()
    except AttributeError:
        fail("inheritance Student class missing or student_info() missing")
    except Exception as e:
        fail(f"inheritance error: {e}")
    else:
        if "Student ID" not in info:
            fail("inheritance Student.student_info() returned unexpected text")

    print("All smoke checks passed.")


if __name__ == "__main__":
    main()
