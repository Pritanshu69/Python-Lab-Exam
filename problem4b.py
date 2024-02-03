def remove_duplicate(input_str):
    unique_chars = set()
    result = []
    
    for char in input_str:
        if char not in unique_chars:
            unique_chars.add(char)
            result.append(char)
            
    return''.join(result)

try:
    input_string = input("Enter a string: ")
    
    output_string = remove_duplicate(input_string)
    
    print(f"Output: {output_string}")
except ValueError:
    print("Error")