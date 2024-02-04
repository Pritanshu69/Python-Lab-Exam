# Take user input for a number
num = int(input("Enter a positive number to check if it's an ugly number: "))

# Check if the given number is an ugly number
if num <= 0:
    print("Please enter a positive number.")
else:
    # Check if the number is an ugly number
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5

    # If num becomes 1 after dividing by 2, 3, and 5, it's an ugly number
    if num == 1:
        print(f"{num} is an ugly number.")
    else:
        print(f"{num} is not an ugly number.")
