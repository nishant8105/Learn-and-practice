"""Fibonacci Sequence Generator - Generates the Fibonacci sequence up to n terms."""


def fibonacci(n):
    """Return list of first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


if __name__ == "__main__":
    result = fibonacci(15)
    print("First 15 Fibonacci numbers:", result)
