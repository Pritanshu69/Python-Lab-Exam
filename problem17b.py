decimal_input = int(input("Enter a decimal number: "))
base_input = int(input("Enter a number from 2 to 16: "))
 
if decimal_input<0 or base_input<2 or base_input>16:
    print("Enter a valid input")
else:   
    result = " " 
    while decimal_input > 0:
        rem = decimal_input % base_input
        result = str(rem) + result
        decimal_input //= base_input

    result = result if result else "0"
    print(f"The number {decimal_input} in base {base_input} is: {result}")
    