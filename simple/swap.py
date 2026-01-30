num1 = int (input (" Enter first number"))
num2 = int (input ( "Enter second number"))

print("Before swaping")
print (f"First number is {num1}")
print (f"Second number is {num2}")

print("After swaping")
num1 , num2 = num2 , num1
print (f"First number is {num1}")
print (f"Second number is {num2}")