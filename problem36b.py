import random

# Initialize an empty list to store student marks
student_marks = []

# Generate random marks for 5 students in 6 subjects
for _ in range(5):
    marks = [random.randint(60, 100) for _ in range(6)]
    student_marks.append(marks)

# Print the original marks for each student
print("Original Student Marks:")
for i, marks in enumerate(student_marks, 1):
    print(f"Student {i}: {marks}")

# Increment 5 marks for each student in each subject
for i in range(len(student_marks)):
    for j in range(len(student_marks[i])):
        student_marks[i][j] += 5

# Print the final marks for each student
print("\nFinal Student Marks (after incrementing 5 marks):")
for i, marks in enumerate(student_marks, 1):
    print(f"Student {i}: {marks}")
