def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b    

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Example usage
    print("Addition:", add(5, 10))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(5, 10))
    try:
        print("Division:", divide(10, 5))
    except ZeroDivisionError as e:
        print("Error:", e)