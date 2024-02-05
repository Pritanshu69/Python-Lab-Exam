import matplotlib.pyplot as plt
import numpy as np
import random

# Generate random CGPA for 10 sections
num_sections = 10
section_names = [f"Section {i+1}" for i in range(num_sections)]
section_cgpa = [random.uniform(2.5, 4.0) for _ in range(num_sections)]

# Plot the bar graph
sections = np.arange(num_sections)
width = 0.7

plt.bar(sections, section_cgpa, width, color='blue', alpha=0.7)

plt.xlabel('Sections')
plt.ylabel('Average CGPA')
plt.title('Average CGPA for 10 Sections')
plt.xticks(sections, section_names)
plt.ylim(2.5, 4.0)

# Show the graph
plt.show()
