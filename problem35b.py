import random

# Initialize an empty list to store student marks
student_marks = []

# Generate random marks for 5 students in 6 subjects
for _ in range(5):
    marks = [random.randint(60, 100) for _ in range(6)]
    student_marks.append(marks)

# Print the marks for each student
print("Student Marks:")
for i, marks in enumerate(student_marks, 1):
    print(f"Student {i}: {marks}")

# Calculate and print the average marks for each subject
num_subjects = len(student_marks[0])
average_marks = [sum(subject_marks) / len(student_marks) for subject_marks in zip(*student_marks)]

print("\nAverage Marks for Each Subject:")
for subject, average in enumerate(average_marks, 1):
    print(f"Subject {subject}: {average:.2f}")

# Find the topper student
topper_index = average_marks.index(max(average_marks)) + 1
print(f"\nThe topper student is Student {topper_index} with an average of {max(average_marks):.2f} marks.")
