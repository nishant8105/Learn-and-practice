# 1. Write and Read a File

with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("Learning File I/O in Python.")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)