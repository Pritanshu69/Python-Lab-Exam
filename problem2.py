import matplotlib.pyplot as plt
import numpy as np

# Generate data
n = np.arange(1, 11)  # Assuming n from 1 to 10 for illustration
O_n = n
O_n_squared = n**2

# Plotting the curves
plt.plot(n, O_n, label='O(n)')
plt.plot(n, O_n_squared, label='O(n^2)')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Operations')
plt.title('O(n) vs O(n^2)')

# Adding legend
plt.legend()

# Display the plot
plt.show()

