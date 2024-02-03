input_str = input("Enter a string: ")

stack = []
for char in input_str:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
    
result = ' '.join(stack)
output = result if result else "Empty String"

print(f"Input: {input_str}, Output: {output}")