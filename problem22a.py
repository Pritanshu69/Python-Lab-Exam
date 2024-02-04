age = int(input("Enter the age: "))

if age<2:
    print("in born")
elif age>=2 and age<=10:
    print("chile")
elif age>=11 and age<=17:
    print("young")
elif age>=18 and age<=49:
    print("adult")
elif age>=50 and age<=79:
    print("old")
else:
    print("very old")
