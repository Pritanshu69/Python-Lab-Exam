import numpy as np

# Take user input for the original array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

original_array = []

for i in range(rows):
    row_values = list(map(int, input(f"Enter values for row {i+1} separated by spaces: ").split()))
    original_array.append(row_values)

given_array = np.array(original_array)

print("\nOriginal Array:")
print(given_array)

# Delete the second column
given_array = np.delete(given_array, 1, axis=1)

# Take user input for the new column
new_column = np.array(list(map(int, input("Enter values for the new column separated by spaces: ").split())))

# Insert the new column at the second position
given_array = np.insert(given_array, 1, new_column, axis=1)

print("\nArray after deleting the second column and inserting a new column:")
print(given_array)
