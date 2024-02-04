import matplotlib.pyplot as plt

# Get user input for five marks
marks = [float(input(f"Enter mark {i + 1}: ")) for i in range(5)]

# Create a bar chart
plt.bar(range(1, 6), marks, color='blue')
plt.xlabel('Exam Number')
plt.ylabel('Marks')
plt.title('Student Marks for a Subject')
plt.xticks(range(1, 6))

# Save the plot as an image
plt.savefig('student_marks_plot.png')

# Close the plot
plt.close()

print("Plot saved as 'student_marks_plot.png'. Open the file to view the plot.")
