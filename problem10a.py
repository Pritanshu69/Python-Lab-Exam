m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for i in range(1, n+1):
    if i%m == 0:
        if i%2 == 0:
            print(f"{i} is divisible by {m}, and it's even")
        else:
            print(f"{i} is divisible by {m} and is odd.")
            
    