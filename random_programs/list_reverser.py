def reverse_list(lst):
    return lst[::-1]

if __name__ == "__main__":
    user_input = input("Enter a list of elements separated by spaces: ").split()
    print(f"Original list: {user_input}")
    print(f"Reversed list: {reverse_list(user_input)}")
