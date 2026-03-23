"""Random Password Generator - Creates secure passwords with customizable length and character sets."""

import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random password with specified criteria."""
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*"
    
    return "".join(random.choices(chars, k=length))


if __name__ == "__main__":
    print("Generated password:", generate_password(16))
