def factorial(x):
    total = 0
    while x > 0:
        total = total * x
        x -= 1
        return total