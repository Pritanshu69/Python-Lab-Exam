import math
x  = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum = 0
series_str = f"{x}"
for i in range(1,n+1):
    term = ((-1)**(i-1)*(x**i)/math.factorial(i))
    sum += term

print(f"The series is: {sum}")