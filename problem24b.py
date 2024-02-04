str_list = input("Enter a list of strings using spaces: ")

max_length = max(len(s) for s in str_list)

print(f"{max_length} is the longest string")