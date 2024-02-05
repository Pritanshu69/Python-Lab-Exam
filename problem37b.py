import matplotlib.pyplot as plt
import numpy as np
import random

# Generate random marks for two students in 6 unit tests
student1_marks = [random.randint(60, 100) for _ in range(6)]
student2_marks = [random.randint(60, 100) for _ in range(6)]

# Plot the bar graph
unit_tests = np.arange(1, 7)
width = 0.35

plt.bar(unit_tests - width/2, student1_marks, width, label='Student 1')
plt.bar(unit_tests + width/2, student2_marks, width, label='Student 2')

plt.xlabel('Unit Tests')
plt.ylabel('Marks')
plt.title('Comparison of Marks for Two Students')
plt.xticks(unit_tests)
plt.legend()

# Show the graph
plt.show()
