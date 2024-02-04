values = input("Enter a list of separated values using spaces: ").split()

original_list = [int(value) for value in values]

unique_element = []

duplicate = []

for value in original_list:
    if value not in unique_element:
        unique_element.append(value)
    else:
        duplicate.append(value)
new_list = unique_element + duplicate

print(f"The list is: {new_list}")