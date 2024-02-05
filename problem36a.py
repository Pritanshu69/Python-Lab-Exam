def find_max_min_indices_from_input():
    # Take user input for the list
    input_str = input("Enter elements of the list separated by spaces: ")
    input_list = list(map(int, input_str.split()))

    if not input_list:
        return None

    max_value = max(input_list)
    min_value = min(input_list)

    max_index = input_list.index(max_value)
    min_index = input_list.index(min_value)

    result = {
        'max_value': max_value,
        'min_value': min_value,
        'max_index': max_index,
        'min_index': min_index
    }

    return result

# Example usage:
result_dict = find_max_min_indices_from_input()

if result_dict:
    print("Maximum Value:", result_dict['max_value'])
    print("Minimum Value:", result_dict['min_value'])
    print("Index of Maximum Value:", result_dict['max_index'])
    print("Index of Minimum Value:", result_dict['min_index'])
