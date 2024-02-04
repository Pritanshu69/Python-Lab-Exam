n = int(input("Enter the range: "))

sum = 0
numerator = 2
denominator = 9

for _ in range(n):
    print(f"{numerator}/{denominator}", end="  ")
    numerator += 3
    denominator += 4
