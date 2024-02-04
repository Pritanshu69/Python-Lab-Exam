import random

# Create a 3x3 matrix with random values
matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

# Print the matrix
print("Random 3x3 Matrix:")
for row in matrix:
    print(row)

# Calculate the sum of diagonal elements
diagonal_sum = sum(matrix[i][i] for i in range(3))

# Print the sum of diagonal elements
print("\nSum of Diagonal Elements:", diagonal_sum)
