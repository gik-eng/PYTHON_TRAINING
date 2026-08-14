"""
Exercise: Selecting Columns

Difficulty: Simple

Description:
Select one or multiple columns from a Pandas DataFrame.

Concepts:

- Pandas
- DataFrame
- Series
- Column Selection
- Indexing


Exercise Tasks:

1. Select the name column.

2. Select the grade column.

3. Select the name and grade columns.

4. Select the name, age, and city columns.

5. Display the selected columns.
"""
import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima"],
    "age": [20, 21, 19, 22, 20],
    "grade": [18, 15, 19, 17, 14],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad"]
}

df = pd.DataFrame(students)

name = df["name"]
grade = df["grade"]
name_grade = df[["name", "grade"]]
name_age_city = df[["name", "age", "city"]]


print(f"name : {name}")
print(f"grade : {grade}")
print(f"name and grade as Data Frame : {name_grade} ")
print(f"name, age and city : {name_age_city}")

