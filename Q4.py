import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def area_of_circle(radius):
    return math.pi * radius * radius

def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num = int(input("Enter a number for factorial: "))
print(f"Factorial of {num} = {factorial(num)}")

radius = float(input("\nEnter radius of circle: "))
print(f"Area of circle with radius {radius} = {area_of_circle(radius):.2f}")

terms = int(input("\nEnter number of terms for Fibonacci series: "))
print(f"Fibonacci series with {terms} terms: {fibonacci(terms)}")
