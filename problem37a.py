import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_square_area(side_length):
    return side_length**2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

while True:
    print("\nMenu:")
    print("1. Calculate Area of Circle")
    print("2. Calculate Area of Square")
    print("3. Calculate Area of Rectangle")
    print("4. Calculate Area of Triangle")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area:.2f}")
    elif choice == '2':
        side_length = float(input("Enter the side length of the square: "))
        area = calculate_square_area(side_length)
        print(f"The area of the square is: {area:.2f}")
    elif choice == '3':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area:.2f}")
    elif choice == '4':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area:.2f}")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
