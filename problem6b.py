input_string = input("Enter the string: ")

last_position = input_string.rfind("emma")
if last_position != -1:
    print(f"The last postition of the string is: {last_position}")
else:
    print("The word 'emma' does not exist in the given string.")