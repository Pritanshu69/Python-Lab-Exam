def kth_largest_factor(N,k):
    factors = []
    for i in range(1,N+1):
        if N%i ==0:
            factors.append(i)
    if k <=len(factors):
        return factors[-k]
    else:
        return None
    
N = int(input("Enter a positive integer N: "))
k = int(input("Enter a positive integer k: "))

result = kth_largest_factor(N,k)

if result is not None:
    print(f"The {k}th largest factor of {N} is: {result}")
else:
    print(f"Error: {k} is greater than the number of factors of {N}.")
