"""Small calculator utility used in week_2 examples.

Provides basic arithmetic functions. Functions are simple and raise
clear errors for invalid operations (for teaching purposes).
"""

def add(a, b):
    """Return the sum of a and b.

    Args:
        a (int|float): first addend
        b (int|float): second addend

    Returns:
        int|float: a + b
    """
    return a + b

def subtract(a, b):
    """Return the difference a - b."""
    return a - b

def multiply(a, b):
    """Return the product a * b."""
    return a * b

def divide(a, b):
    """Return the quotient a / b.

    Raises ZeroDivisionError when b is zero so students can learn to
    handle exceptions when dividing.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Run a short self-check when executed directly. In teaching use this
    # to demonstrate how to import and use the module versus running it.
    print("Addition:", add(5, 10))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(5, 10))
    try:
        print("Division:", divide(10, 5))
    except ZeroDivisionError as e:
        print("Error:", e)