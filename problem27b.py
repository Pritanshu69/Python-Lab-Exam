# Get user input for the size of the matrices
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

# Input the first matrix
print("Enter elements for the first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(rows)]

# Input the second matrix
print("Enter elements for the second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

# Add the matrices
result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Print the result matrix
print("\nResultant Matrix (Sum of Matrices):")
for row in result_matrix:
    print(row)

# Save matrices and result to files
with open('matrix1.txt', 'w') as file:
    for row in matrix1:
        file.write(' '.join(map(str, row)) + '\n')

with open('matrix2.txt', 'w') as file:
    for row in matrix2:
        file.write(' '.join(map(str, row)) + '\n')

with open('result_matrix.txt', 'w') as file:
    for row in result_matrix:
        file.write(' '.join(map(str, row)) + '\n')

print("Matrices and result have been stored in 'matrix1.txt', 'matrix2.txt', and 'result_matrix.txt' files.")
