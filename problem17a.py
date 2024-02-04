num = int(input("Enter the number: "))

a , b = 0 , 1

print("Fibonacci series up to {} terms:".format(num), end=" ")

for _ in range(num):
    print(a, end= " ")
    a,b=b,a+b
