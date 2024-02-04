# Get user input for a list
original_list = input("Enter a list (comma-separated values): ").split(',')

# Convert the input to integers
original_list = [int(x) for x in original_list]

# Reverse the list using slicing
reversed_list = original_list[::-1]

# Print the reversed list
print("Original List:", original_list)
print("Reversed List:", reversed_list)
