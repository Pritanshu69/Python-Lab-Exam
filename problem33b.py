rows = int(input("Enter the number of rows: "))

for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()    

for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")

    # Print decreasing numbers (excluding 1 for the center)
    for l in range(i - 1, 0, -1):
        print(l, end=" ")

    # Move to the next line for the next row
    print()