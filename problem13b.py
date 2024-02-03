# Take user input for N (N > 20)
N = int(input("Enter a number (N > 20): "))

# Print numbers from 11 to N with conditions
for num in range(11, N + 1):
    if num % 3 == 0 and num % 7 == 0:
        print("TipsyTopsy")
    elif num % 3 == 0:
        print("Tipsy")
    elif num % 7 == 0:
        print("Topsy")
    else:
        print(num)
