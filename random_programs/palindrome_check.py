def is_palindrome(s):
    # Remove whitespace and convert to lowercase for uniform comparison
    clean_s = "".join(s.split()).lower()
    return clean_s == clean_s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word or phrase to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
