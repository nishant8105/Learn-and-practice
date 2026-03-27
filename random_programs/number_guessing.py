low = 1
high = 100
feedback = ""

print("Think of a number between 1 and 100!")

while feedback != "c":
    guess = (low + high) // 2
    print(f"My guess is {guess}")
    feedback = input("Is it High (h), Low (l), or Correct (c)? ").lower()

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1

print("Yay! I guessed your number!")