"""
Exercise: Selecting Data with loc

Difficulty: Simple

Description:
Select specific rows and columns from a Pandas DataFrame using
the loc indexer and label-based indexing.

Concepts:

- Pandas
- DataFrame
- loc
- Label-Based Indexing
- Row Selection
- Column Selection
- Slicing


Exercise Tasks:

1. Select the student with index 2.

2. Select only the name and grade of the student with index 2.

3. Select students with indexes 1 through 3.

4. Select the name and city columns for students with indexes 1 through 3.

5. Select the students with indexes 0 and 4.
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima"],
    "age": [20, 21, 19, 22, 20],
    "grade": [18, 15, 19, 17, 14],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad"]
}

df = pd.DataFrame(students)

student_2 = df.loc[2]
name_grade_student_2 = df.loc[2, ["name", "grade"]]
students_1_to_3 = df.loc[1 : 3]
name_city_students_1_to_3 = df.loc[1 : 3, ["name", "city"]]
index_0_and_4 = df.loc[[0, 4]]

print(f"student number 2 : {student_2}")
print(f"name and grade of student number 2 : {name_grade_student_2}")
print(f"students 1 to 3 : {students_1_to_3}")
print(f"name and city of students 1 to 3 : {name_city_students_1_to_3}")
print(f"index 0 to 4 of students : {index_0_and_4}")