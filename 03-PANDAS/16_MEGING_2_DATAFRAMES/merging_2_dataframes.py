"""
Exercise: Merging DataFrames

Difficulty: Simple

Description:
Learn how to combine two Pandas DataFrames using merge()
and understand different types of joins.

Concepts:

- Pandas
- DataFrame
- merge()
- Common keys
- Inner join
- Left join
- Right join
- Outer join


Exercise Tasks:

1. Create two DataFrames containing related student information.

2. Merge two DataFrames using a common column.

3. Perform an inner merge.

4. Create two DataFrames with different IDs and observe
   which rows are kept in an inner merge.

5. Perform a left merge and keep all rows from the left DataFrame.

6. Perform a right merge and keep all rows from the right DataFrame.

7. Perform an outer merge and keep all rows from both DataFrames.


Challenge:

1. Create an employees DataFrame containing employee information
   and department IDs.

2. Create a departments DataFrame containing department IDs
   and department names.

3. Merge the two DataFrames using "department_id".

4. Keep all employees in the final DataFrame.

5. Print the final merged DataFrame.
"""


import pandas as pd


# =========================
# Basic Merge
# =========================

students = {
    "student_id": [101, 102, 103, 104, 105],
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima"],
    "grade": [18, 15, 19, 17, 14]
}


cities = {
    "student_id": [101, 102, 103, 104, 105],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad"]
}


cities2 = {
    "student_id": [101, 102, 104, 105, 106],
    "city": ["Tehran", "Shiraz", "Tehran", "Mashhad", "Karaj"]
}


students_df = pd.DataFrame(students)
cities_df = pd.DataFrame(cities)
cities2_df = pd.DataFrame(cities2)


print("Students DataFrame:")
print(students_df)

print("Cities DataFrame:")
print(cities_df)


# =========================
# Default Merge
# =========================

merged_df = pd.merge(
    students_df,
    cities_df,
    on="student_id"
)

print("Default Merge:")
print(merged_df)


# =========================
# Inner Merge
# =========================

merged_inner = pd.merge(
    students_df,
    cities_df,
    on="student_id",
    how="inner"
)

print("Inner Merge:")
print(merged_inner)


# =========================
# Inner Merge with Different IDs
# =========================

merged_inner2 = pd.merge(
    students_df,
    cities2_df,
    on="student_id",
    how="inner"
)

print("Inner Merge with Different IDs:")
print(merged_inner2)


# =========================
# Left Merge
# =========================

left_merge = pd.merge(
    students_df,
    cities2_df,
    on="student_id",
    how="left"
)

print("Left Merge:")
print(left_merge)


# =========================
# Right Merge
# =========================

right_merge = pd.merge(
    students_df,
    cities2_df,
    on="student_id",
    how="right"
)

print("Right Merge:")
print(right_merge)


# =========================
# Outer Merge
# =========================

outer_merge = pd.merge(
    students_df,
    cities2_df,
    on="student_id",
    how="outer"
)

print("Outer Merge:")
print(outer_merge)


# =========================
# Challenge
# =========================

employees = {
    "employee_id": [1, 2, 3, 4],
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "department_id": [10, 20, 10, 30]
}


departments = {
    "department_id": [10, 20, 30],
    "department": ["IT", "Finance", "Marketing"]
}


employees_df = pd.DataFrame(employees)
departments_df = pd.DataFrame(departments)


merged = pd.merge(
    employees_df,
    departments_df,
    on="department_id",
    how="left"
)


print("Challenge:")
print(merged)