import random

def guess_the_number():
    target = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed {target} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guess_the_number()
