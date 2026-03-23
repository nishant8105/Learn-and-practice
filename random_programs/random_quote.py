"""Random Quote Picker - Returns a random inspirational quote."""

import random

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Churchill",
]


def get_random_quote():
    return random.choice(QUOTES)


if __name__ == "__main__":
    print(get_random_quote())
