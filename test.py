def add(a, b):
    return a + b
# sdfsd
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

# Test the functions
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 4))
print("Multiplication:", multiply(7, 2))
print("Division:", divide(8, 2))
