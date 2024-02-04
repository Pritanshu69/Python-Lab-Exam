import matplotlib.pyplot as plt
import random

# Generate 30 random 2D points
random_points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(30)]

# Unpack the coordinates
x, y = zip(*random_points)

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of 30 Random 2D Points')

# Display the plot
plt.show()
