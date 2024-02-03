start_range = int(input("Enter the  starting range: "))
end_range = int(input("Enter the ending range: ")) 

twin_primes = []

for num in range(start_range,end_range-1):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and all((num + 2) % i != 0 for i in range(2, int((num + 2)**0.5) + 1)):
        twin_primes.append((num,num+2))

if twin_primes:
    print(f"Twin prime numbers between {start_range} and {end_range}: {twin_primes}")
else:
    print(f"No twin prime numbers found between {start_range} and {end_range}.")