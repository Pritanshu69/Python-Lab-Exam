import math
n = int(input("Enter the range: "))

sum = 0

for i in range(n+1):
    print(f"1/{math.factorial(i)}",end = " ")
