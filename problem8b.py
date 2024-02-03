# Initialize variables
total = 0
count = 0

# Take user input for numbers
print("Enter numbers (Enter 'q' to see the average):")

while True:
    input_str = input()
    
    # Check if the user wants to exit
    if input_str.lower() == 'q':
        break
    
    # Check if the input is a valid number
    if input_str.replace('.', '', 1).isdigit():
        # Convert the input to a float and add to the total
        number = float(input_str)
        total += number
        count += 1
    else:
        print("Invalid input. Please enter a valid number or 'q' to see the average.")

# Calculate and print the average
if count > 0:
    average = total / count
    print(f"Average = {average:.2f}")
else:
    print("No valid numbers entered.")
