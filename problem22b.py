L = input("Enter the first list: ")
M = input("Enter the second list: ")

#input string to list of integers

L = [int(num.strip()) for num in L.split(',')]
M = [int(num.strip()) for num in M.split(',')]

if len(L) != len(M):
    print("Please enter same size: ")
else:
    N = [L[i] + M[i] for i in range(len(L))]
    print(f"sum: {N}")