# Get user input for student's marks
marks = float(input("Enter the student's marks: "))

# Determine the grade based on the specified rules
if 90 <= marks <= 100:
    grade = 'O'
elif 80 <= marks < 90:
    grade = 'E'
elif 70 <= marks < 80:
    grade = 'A'
elif 60 <= marks < 70:
    grade = 'B'
elif 50 <= marks < 60:
    grade = 'C'
elif 40 <= marks < 50:
    grade = 'D'
elif 0 <= marks < 40:
    grade = 'F (FAILED)'
else:
    grade = 'INVALID'

# Print the determined grade
print(f"The student's grade is: {grade}")
