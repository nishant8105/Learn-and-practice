# 3. Copy Content from One File to Another

with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as dest:
    dest.write(content)

print("File copied successfully!")