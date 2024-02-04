n = int(input("Enter the range: "))

sum = 0

for i in range(1,n+1):
    sum += 1/i

print(f"The sum is: {sum}")