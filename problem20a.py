input_string = input("Enter the string: ")
if all(char in '01' for char in input_string):
    print("Binary String")
else:
    print("Not a binary string")