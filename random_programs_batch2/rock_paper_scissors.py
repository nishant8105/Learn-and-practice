"""
Rock Paper Scissors

Command-line game against the computer.
"""

import random

CHOICES = ("r", "p", "s")  # rock, paper, scissors


def winner(user: str, cpu: str) -> str:
    if user == cpu:
        return "draw"
    if (user, cpu) in {("r", "s"), ("s", "p"), ("p", "r")}:
        return "user"
    return "cpu"


def main() -> None:
    print("Rock (r), Paper (p), Scissors (s). Type q to quit.")
    while True:
        user = input("Your choice: ").strip().lower()
        if user == "q":
            break
        if user not in CHOICES:
            print("Invalid choice. Try again.")
            continue

        cpu = random.choice(CHOICES)
        result = winner(user, cpu)

        choice_map = {"r": "Rock", "p": "Paper", "s": "Scissors"}
        print(f"CPU: {choice_map[cpu]} | You: {choice_map[user]} -> {result.upper()}")


if __name__ == "__main__":
    main()
