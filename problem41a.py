import numpy as np

# Create a matrix randomly
matrix = np.random.randint(1, 100, size=(3, 4))
print("Original Matrix:")
print(matrix)

# Sort the matrix with respect to the second row
sorted_matrix = matrix[:, matrix[1, :].argsort()]
print("\nMatrix sorted with respect to the second row:")
print(sorted_matrix)
