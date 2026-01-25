print("1️⃣ Add Two Numbers")
print("Write a function that takes two numbers and returns their sum.")

def add (x, y) :
    return f"{x+y} is addition of {x, y}"

print(add(2, 3))
print("===============================================================")
print("2️⃣ Even or Odd")
print("Create a function that takes a number and returns whether it is even or odd.")

def Check_number(x):
    if (x & 1 == 0):
        return f"{x} is Even"
    else:
        return f"{x} is Odd"

print(Check_number(5))
print(Check_number(6))
print("===============================================================")

print("3️⃣ Square of a Number")
print("Write a function that returns the square of a given number.")

def sq(x):
    return f"{x**2} is square of {x}"


print(sq(5))
print(sq(6))
print("===============================================================")


print("4️⃣ Greeting Function")
print("Create a function that takes a name as input and returns")
print("Hello, <name>!")

def greet():
    name = input("Enter your name : ")
    return f"Hello {name}"

print(greet())
print("===============================================================")

print("5️⃣ Maximum of Two Numbers")
print("Write a function that returns the larger of two numbers.")

def max(x, y):
    if (x > y):
        return f"{x} is greter than {y}"
    else :
        return f"{y} is greter than {x}"

print(max(2, 3))
print(max(5, 3))
print("===============================================================")