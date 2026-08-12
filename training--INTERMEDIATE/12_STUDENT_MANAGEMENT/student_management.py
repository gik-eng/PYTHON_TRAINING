"""
Exercise: Student Management System

Difficulty: Intermediate

Description:
Manage student data stored in a list of dictionaries.
Calculate student averages and find students who passed based on their grades.

Concepts:
- Functions
- Lists
- Dictionaries
- Nested Data Structures
- Loops
- Conditional Logic
- Data Processing
"""


students = [
    {
        "name": "Ali",
        "grades": [18, 20, 17]
    },
    {
        "name": "Sara",
        "grades": [12, 7, 10]
    },
    {
        "name": "Reza",
        "grades": [19, 18, 20]
    }
]


def calculate_average(student):
    # Calculate the average grade of a student
    total_grade = 0

    for grade in student["grades"]:
        total_grade += grade

    average = total_grade / len(student["grades"])

    return average


def passed_students(students):
    # Find students with an average grade of 15 or higher
    passed = []

    for student in students:
        average = calculate_average(student)

        if average >= 15:
            passed.append(student["name"])

    return passed


result = passed_students(students)

print(result)

    