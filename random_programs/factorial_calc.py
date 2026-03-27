def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"The factorial of {num} is {factorial(num)}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
