# Take user input for the number of elements
N = int(input("How many numbers do you want to enter? "))

# Initialize variables for the largest and second-largest numbers
largest = None
second_largest = None

# Input N numbers and find the largest and second-largest
for i in range(N):
    num = float(input(f"Enter number {i + 1}: "))

    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or num > second_largest:
        second_largest = num

# Check if there are at least two distinct numbers
if second_largest is None:
    print("Please enter at least two distinct numbers.")
else:
    print(f"The biggest number is: {largest}")
    print(f"The second biggest number is: {second_largest}")
