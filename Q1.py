import math

def arithmetic_operations(a, b):
    print("Arithmetic Operations:")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Division: {a} / {b} = {a / b}")
    else:
        print("Division: Cannot divide by zero")

def solve_quadratic(a, b, c):
    print("\nQuadratic Equation Solver:")
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Roots are real and different: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"Roots are real and same: {root}")
    else:
        realPart = -b / (2*a)
        imagPart = math.sqrt(-discriminant) / (2*a)
        print(f"Roots are complex: {realPart}+{imagPart}i and {realPart}-{imagPart}i")

a = float(input("Enter first number for arithmetic: "))
b = float(input("Enter second number for arithmetic: "))
arithmetic_operations(a, b)

print("\n--- Quadratic Equation ---")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
solve_quadratic(a, b, c)