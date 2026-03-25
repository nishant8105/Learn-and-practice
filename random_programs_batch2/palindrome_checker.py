"""
Palindrome Checker

Checks whether a given string is a palindrome (ignores case and non-alphanumeric characters).
"""

import re
import sys


def is_palindrome(text: str) -> bool:
    # Keep only letters/numbers, and compare case-insensitively.
    normalized = re.sub(r"[^A-Za-z0-9]+", "", text).lower()
    return normalized == normalized[::-1]


def main() -> None:
    if len(sys.argv) > 1:
        s = " ".join(sys.argv[1:])
    else:
        s = input("Enter text: ")

    print("Palindrome" if is_palindrome(s) else "Not a palindrome")


if __name__ == "__main__":
    main()
