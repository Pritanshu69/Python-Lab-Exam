input_string = input("Enter a string: ")

has_letter = any(char.isalpha() for char in input_string)
has_number = any(char.isdigit() for char in input_string)

result = has_letter and has_number

print(result)