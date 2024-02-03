n = int(input("Enter the value of n: "))

if n<2:
    print("There are no prime numbers in this range")
else:
    print(f"prime number between 1 and {n} are: ")
    for num in range(2, n+1):
        is_prime = True
        for i in range (2, int(num**0.5) + 1):
            if num%i == 0:
                is_prime = False
                break;
            if is_prime:
                print(num, end=' ')