import cmath

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

delta = cmath.sqrt(b**2 - 4*a*c)

root1 = (-b + delta)/(2*a)
root2 = (-b - delta)/(2*a)

print(f"The roots are: ")
print(f"Root1: {root1}")
print(f"Root2: {root2}")
