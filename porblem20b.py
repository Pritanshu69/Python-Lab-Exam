input_list = input("Enter the string: ").split()
integer_list = [int(num) for num in input_list]

palindrome = [num for num in integer_list if str(num) == str(num)[::-1]]

if palindrome:
    print(f"Palindrome list is: ",palindrome)
else:
    print(f"No palindrome")