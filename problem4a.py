def item(num):
    if num < 10:
        cost=120
    elif 10<=num<=99:
        cost=100
    else:
        cost =70
    total_cost = cost*num
    
    return f"Total cost is {total_cost} Rs"

try:
    num=int(input("Enter the number of the items"))
    if  num<0:
        print("Enter a positive number")
    else:
        total_cost=item(num)
        print(f"The total cost of the items is: {total_cost}")
except  ValueError:
    print("Enter a valid number")
    
    