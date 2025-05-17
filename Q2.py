def solve_linear_equation(a, b):
    print("\nSolving Linear Equation: ax + b = 0")
    if a == 0:
        if b == 0:
            print("Infinite solutions (every x satisfies the equation).")
        else:
            print("No solution (this is a contradiction).")
    else:
        x = -b / a
        print(f"Solution: x = {-b} / {a} = {x}")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
solve_linear_equation(a, b)
