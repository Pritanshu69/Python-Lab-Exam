num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

x , y = num1,num2

while y:
    x,y=y,x%y
hcf = x

lcm = (num1*num2)//hcf

# Print HCF and LCM
print(f"HCF of {num1} and {num2} is {hcf}")
print(f"LCM of {num1} and {num2} is {lcm}")