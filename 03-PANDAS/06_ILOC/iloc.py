"""
Exercise: Selecting Data with iloc

Difficulty: Simple

Description:
Select specific rows and columns from a Pandas DataFrame using
the iloc indexer and position-based indexing.

Concepts:

- Pandas
- DataFrame
- iloc
- Position-Based Indexing
- Row Selection
- Column Selection
- Slicing


Exercise Tasks:

1. Select the third student using position-based indexing.

2. Select students in positions 2 and 3.

3. Select the name and grade columns for students in positions 2 and 3.

4. Select the first and last students.

5. Create a 2x2 DataFrame containing Sara and Reza,
   with their age and grade columns.
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima"],
    "age": [20, 21, 19, 22, 20],
    "grade": [18, 15, 19, 17, 14],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad"]
}

df = pd.DataFrame(students)

student_3 = df.iloc[2]
student_2_to_4 = df.iloc[2 : 4]
name_and_grade_of_student_2_to_4 = df.iloc[2 : 4,[0 , 2]]
first_and_last_student = df.iloc[[0, 4]]
DataFrame_2x2 = df.iloc[[1, 2], [1, 2]] 

print(f"student 3 is :  {student_3}")
print(f"students 2 to 4 :  {student_2_to_4}")
print(f"name and grade of students 2 to 4 : \n {name_and_grade_of_student_2_to_4}")
print(f"first and last students : {first_and_last_student}")
print(f"Date Frame : {DataFrame_2x2}")