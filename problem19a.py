n = int(input("Enter a number: "))

print(f"The prime factors of n are: ", end = " ")

div = 2
while div <=n:
    if n % div == 0:
        print(div,end = " ")
        n //= div
    else:
        div += 1
        