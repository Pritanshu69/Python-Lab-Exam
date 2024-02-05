input_string = input("Enter a string: ")
result_string = ""

for char in input_string:
    if char not in result_string:
        result_string += char

print("String after removing duplicates:", result_string)


