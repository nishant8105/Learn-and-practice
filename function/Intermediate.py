print("6️⃣ Factorial Calculator")
print("Write a function that takes a number and returns its factorial.")

def fact(x):
    if x == 0 : 
        return 1
    factorial = x * fact(x-1)
    return factorial
print(fact(5))

print("===============================================================")

print("7️⃣ Count Vowels")
print("Create a function that counts the number of vowels in a string.")

def count_vowel( word ):
    count = 0
    for i in range(len(word)) :
        if (word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u" ):
            count += 1
    return count

print(count_vowel("apple"))
print("===============================================================")

print("8️⃣ Simple Interest")
print("Write a function that takes principal, rate, and time and returns simple interest.")


def simple_interest(principal, rate, time ):
    SimpleInterest = (principal * rate * time)/100
    return SimpleInterest

print(simple_interest(1000000, 7, 7))


print("===============================================================")

print("9️⃣ Palindrome Check")
print("Create a function that checks whether a given string is a palindrome.")
def palindrome(word ):
    word = word.lower()
    reverse = word[ : :-1]
    if word == reverse :
        return f"{word} is palindrome"
    else:
        return f"{word} is not palindrome"

print(palindrome("civic"))
print(palindrome("nishant"))


print("===============================================================")
print("🔟 List Sum")
print("Write a function that takes a list of numbers and returns the sum of all elements.")

def SumOfList(x):
    list_to_sum = []
    for i in range(x):
        element = int(input("Enter the element of list : "))
        list_to_sum.append(element)
    print(list_to_sum)
    sum = 0
    for i in list_to_sum :
        sum += i
    return f"The sum of list is {sum}"


print(SumOfList(5))