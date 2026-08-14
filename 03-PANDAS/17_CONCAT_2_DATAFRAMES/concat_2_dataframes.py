"""
Exercise: Concatenating DataFrames

Difficulty: Simple

Description:
Learn how to combine Pandas DataFrames using concat()
and understand how axis and index handling affect the result.

Concepts:

- Pandas
- DataFrame
- concat()
- axis=0
- axis=1
- ignore_index
- Index alignment


Exercise Tasks:

1. Create multiple DataFrames containing student information.

2. Concatenate two DataFrames vertically.

3. Concatenate multiple DataFrames vertically.

4. Use ignore_index=True to create a new sequential index.

5. Concatenate two DataFrames horizontally using axis=1.

6. Understand the difference between axis=0 and axis=1.

7. Combine DataFrames using matching indexes.


Challenge:

1. Create two DataFrames representing morning and afternoon students.

2. Concatenate both DataFrames vertically.

3. Use ignore_index=True.

4. Keep all columns from both DataFrames.

5. Print the final DataFrame.
"""


import pandas as pd


# =========================
# Creating DataFrames
# =========================

students_1 = {
    "name": ["Ali", "Sara", "Reza"],
    "grade": [18, 15, 19]
}


students_2 = {
    "name": ["Mina", "Nima", "Zahra"],
    "grade": [17, 14, 20]
}


students_3 = {
    "name": ["Amir", "Leila"],
    "grade": [16, 19]
}


df1 = pd.DataFrame(students_1)
df2 = pd.DataFrame(students_2)
df3 = pd.DataFrame(students_3)


print("DataFrame 1:")
print(df1)

print("DataFrame 2:")
print(df2)

print("DataFrame 3:")
print(df3)


# =========================
# Concatenating DataFrames
# =========================

all_students_df = pd.concat(
    [df1, df2]
)


print("Concatenated DataFrames:")
print(all_students_df)


# =========================
# Concatenating with New Index
# =========================

all_students_df2 = pd.concat(
    [df1, df2],
    ignore_index=True
)


print("Concatenated DataFrames with New Index:")
print(all_students_df2)


# =========================
# Concatenating Three DataFrames
# =========================

all_students_df3 = pd.concat(
    [df1, df2, df3],
    ignore_index=True
)


print("Three DataFrames Concatenated:")
print(all_students_df3)


# =========================
# Horizontal Concatenation
# =========================

names = {
    "name": ["Ali", "Sara", "Reza"]
}


grades = {
    "grade": [18, 15, 19]
}


names_df = pd.DataFrame(names)
grades_df = pd.DataFrame(grades)


print("Names DataFrame:")
print(names_df)

print("Grades DataFrame:")
print(grades_df)


names_and_grades_df = pd.concat(
    [names_df, grades_df],
    axis=1
)


print("Horizontal Concatenation:")
print(names_and_grades_df)


# =========================
# Challenge
# =========================

morning_students = {
    "student_id": [101, 102, 103],
    "name": ["Ali", "Sara", "Reza"],
    "grade": [18, 15, 19]
}


afternoon_students = {
    "student_id": [104, 105, 106],
    "name": ["Mina", "Nima", "Zahra"],
    "grade": [17, 14, 20]
}


morning_students_df = pd.DataFrame(morning_students)
afternoon_students_df = pd.DataFrame(afternoon_students)


print("Morning Students:")
print(morning_students_df)

print("Afternoon Students:")
print(afternoon_students_df)


concat_df = pd.concat(
    [morning_students_df, afternoon_students_df],
    ignore_index=True,
    axis=0
)


print("Final Concatenated DataFrame:")
print(concat_df)