text = input("Enter some text:\n")

words = len(text.split())
characters = len(text)
lines = text.count("\n") + 1

print("Words:", words)
print("Characters:", characters)
print("Lines:", lines)