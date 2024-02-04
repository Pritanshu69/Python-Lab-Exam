def case_count(input_string):
    uppercase_count = 0
    lowercase_count = 0
    
    for char in input_string:
        if char.isupper():
            uppercase_count +=  1
        if char.islower():
            lowercase_count +=  1
            
    return uppercase_count , lowercase_count
    
user_input = input("Ente a string: ")
    
uppercase_count,lowercase_count=case_count(user_input)

# Display the results
print(f"No. Of Uppercase characters: {uppercase_count}")
print(f"No. Of Lowercase Characters: {lowercase_count}")
    