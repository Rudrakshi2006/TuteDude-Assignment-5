student_marks = {
    "Arya": 85,
    "Rohan": 78,
    "Krish": 92,
    "Dev": 88,
    "Eva": 95
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")