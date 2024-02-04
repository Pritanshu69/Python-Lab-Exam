num = int(input("Enter the number: "))

temp = num
sum = 0
num_digits = 0

while temp>0:
    temp//=10
    num_digits+=1

temp = num

while temp>0:
    digit = temp%10
    sum += digit ** num_digits
    temp //= 10
    
if sum == num:
     print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")