# Take user input for a string
input_string = input("Enter the string: ")

# Split the input string into a list of elements
input_list = input_string.split()

# Convert the elements to integers
input_list = [int(element) for element in input_list]

if len(input_list) >= 5:
    # Remove the element at index 4
    removed_element = input_list.pop(4)

    # Add the removed element to the 2nd position
    input_list.insert(1, removed_element)

    # Append the removed element to the end of the list
    input_list.append(removed_element)

    # Print the modified list
    print("Modified List:", input_list)
else:
    print("Use more than 4 elements in the input.")

