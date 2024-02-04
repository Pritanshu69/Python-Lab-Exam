def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

while True:
    # Display menu
    print("\nSimple Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    # Get user choice
    choice = input("Enter your choice (1-5): ")

    # Check if the user wants to quit
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    # Get user input for operands
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue

    # Print the result
    print("Result:", result)
