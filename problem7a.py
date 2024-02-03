#Write a program to input 3 sides of a triangle and print whether it is an equilateral,scalene or isosceles triangle.

side1 = float(input("Enter the size of the first side: "))
side2 = float(input("Enter the size of the second side: "))
side3 = float(input("Enter the size of the third side: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")