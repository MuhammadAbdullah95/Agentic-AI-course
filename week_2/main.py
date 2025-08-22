
"""Example script that uses the `calculate` utility module.

This file demonstrates importing functions, using descriptive variable
names, and handling exceptions (division by zero).
"""

from calculate import add, subtract, multiply, divide


def main():
    # Use descriptive names instead of overriding builtin names like `sum`.
    addition_result = add(5, 10)
    subtraction_result = subtract(10, 5)

    print("Addition:", addition_result)
    print("Subtraction:", subtraction_result)

    # Demonstrate exception handling for division
    try:
        division_result = divide(10, 0)
    except ZeroDivisionError as e:
        # For teaching, show the error and set result to None
        print("Division error handled:", e)
        division_result = None

    product_result = multiply(5, 10)

    print("Multiplication:", product_result)
    print("Division:", division_result)


if __name__ == "__main__":
    main()
