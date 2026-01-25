print("1️⃣1️⃣ Prime Number Checker")
print("Write a function that checks whether a number is prime.")
def prime(x):
    if x == 1:
        return f"{x} is a prime number"
    elif x < 0:
        return f'''{x} is negative 
Therefore {x} is not prime number '''
    elif x == 0:
        return f'''{x} is 0
Therefore {x} is not prime number '''
    else:
        for i in range(2 , x):
            if (x % i == 0):
                return f"{x} is not a prime number"
        else :
            return f"{x} is a prime number"
print(prime(-0))
print(" ")
print("===============================================================")
print("1️⃣2️⃣ Fibonacci Series")
print("Create a function that returns the first n Fibonacci numbers.")
def fibonacci(x):
    if x == 0 :
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)

num = int(input("Enter the number : "))
for i in range(num):
    print(f"fibonacci of {i} is {fibonacci(i)}")
print("===============================================================")
print("1️⃣3️⃣ Find Minimum in List")
print("Write a function that finds the smallest number in a list without using min().")


def Minimum(x):
    lst = []
    for i in range(x):
        num = int(input("Enter the number in list: "))
        lst.append(num)
    print(lst)
    min = lst[0]
    for i in lst :
        if min > i :
            min = i
    
    return min

length = int(input("Enter the length of list: "))
print(f"The minimum value in list is {Minimum(length)}")
print("===============================================================")
print("1️⃣4️⃣ Temperature Converter")
print("Write a function to convert Celsius to Fahrenheit and vice versa.")


def  TemperatureConverter(x) :
    convert = int(input('''Enter to which unit you want to convert
1 for Celsius
2 for Fahrenheit : 
'''))
    if (convert == 1 ) :
        celsius = (x -32)/1.8 ;
        return celsius
    elif (convert == 2 ) :
        fehrenheit = (x * 1.8) + 32 
        return fehrenheit
    else :
        print("Enter vaild choice")

print(TemperatureConverter(0))
print("================================================================")
print("1️⃣5️⃣ Character Frequency")
print("Create a function that returns how many times each character appears in a string.")
word = input("Enter the string: ")
def charfreq(word):
    dictt = {}
    for i in word.lower():
        if i not in dictt :
            dictt[i] = 1
        else :
            dictt[i] += 1
    
    return dictt

print(charfreq(word))
