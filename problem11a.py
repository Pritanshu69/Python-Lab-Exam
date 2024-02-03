def is_prime(number):
    if number<2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
def is_palindrome(number):
    return str(number) == str(number)[::-1]

start_range = int(input("Enter the starting range: "))
last_range = int(input("Enter the last range: "))

prime_palinfrome_numbers = []

for num in range(start_range, last_range+1):
    if  is_prime(num) and is_palindrome(num):
        prime_palinfrome_numbers.append(num)

if prime_palinfrome_numbers:
    print(f"Palindromic prime numbers between {start_range} and {last_range}: {prime_palinfrome_numbers}")
else:
    print(f"No palindromic prime numbers found between {start_range} and {last_range}.")