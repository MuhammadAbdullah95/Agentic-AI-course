"""Practical examples for exception handling.

This file demonstrates common patterns:
- catching specific exceptions
- using multiple except clauses
- creating and raising custom exceptions
- using finally and else blocks
"""


class ValidationError(Exception):
    """Custom exception used to signal validation problems."""
    pass


def divide_with_handling(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Handled ZeroDivisionError:", e)
        return None
    except TypeError as e:
        print("Type error (non-numeric input):", e)
        return None
    else:
        # Executed only if no exception occurred
        return result
    finally:
        # Good place for cleanup actions (this runs always)
        print(f"divide_with_handling called with a={a}, b={b}")


def validate_positive_integer(n):
    if not isinstance(n, int):
        raise ValidationError("Value must be an integer")
    if n <= 0:
        raise ValidationError("Value must be positive")
    return True


def example_multiple_excepts():
    inputs = [(10, 2), (5, 0), ("x", 2)]
    for a, b in inputs:
        print("---")
        res = divide_with_handling(a, b)
        print("Result:", res)


def example_validation():
    tests = [5, -1, 3.14, "10"]
    for t in tests:
        try:
            print(f"Validating {t} ->", validate_positive_integer(t))
        except ValidationError as e:
            print("ValidationError:", e)


def main():
    print("Multiple except examples:")
    example_multiple_excepts()
    print("\nValidation examples:")
    example_validation()


if __name__ == "__main__":
    main()
