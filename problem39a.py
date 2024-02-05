# Accept a string from the user
input_str = input("Enter a string: ")

# Define a set of vowels
vowels = set("aeiouAEIOU")

# Check if the input string contains all vowels
if set(input_str) >= vowels:
    print("The entered string contains all vowels.")
else:
    print("The entered string does not contain all vowels.")
