# Take user input for list elements
input_list = input("Enter a list of numbers separated by commas: ")
my_list = [int(num) for num in input_list.split(',')]

# Take user input for index range
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Check if the indexes are within the valid range
if start_index < 0 or end_index >= len(my_list) or start_index > end_index:
    print("Invalid index range.")
else:
    # Get the sublist within the specified range
    sublist = my_list[start_index:end_index + 1]

    # Find and display the maximum and minimum values
    max_value = max(sublist)
    min_value = min(sublist)

    print(f"Maximum value in the range [{start_index}:{end_index}] is: {max_value}")
    print(f"Minimum value in the range [{start_index}:{end_index}] is: {min_value}")
