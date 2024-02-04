n = int(input("Enter the number of employees: "))

count_26_35 = count_36_45 = count_46_55 = 0

for _ in range(n):
    age = int(input("Enter the employee's age: "))
    if 26 <= age < 35:
        count_26_35 += 1
    if 36 <= age < 45:
        count_36_45 += 1
    if 46 <= age < 55:
        count_46_55 += 1

print(f"\nNumber of persons in the age group 26-35: {count_26_35}")
print(f"Number of persons in the age group 36-45: {count_36_45}")
print(f"Number of persons in the age group 46-55: {count_46_55}")
    