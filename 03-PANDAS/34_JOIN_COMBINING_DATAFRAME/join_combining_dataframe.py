"""
Exercise 34 — Joining DataFrames

This exercise focuses on combining DataFrames
using their indexes.

Topics:
- join()
- Index-based joining
- Inner join
- Left join
- Right join
- Outer join
- Handling missing values after joining
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima"],
    "city": ["Tehran", "Shiraz", "Tehran", "Tabriz", "Mashhad"],
    "grade": [18, 15, 19, 17, 14]
}


df_students = pd.DataFrame(
    students,
    index=["S01", "S02", "S03", "S04", "S05"]
)


print(df_students)


student_details = {
    "age": [20, 21, 19, 22, 20],
    "study_hours": [3, 2, 4, 3, 1]
}


df_details = pd.DataFrame(
    student_details,
    index=["S01", "S02", "S03", "S04", "S05"]
)


print(df_details)




result = df_students.join(df_details)
print(result)



df_details_missing = df_details.drop("S05")
result_inner = df_students.join(
    df_details_missing,
    how="inner"
)

print(result_inner)



result_left = df_students.join(
    df_details_missing,
    how="left"
)

print(result_left)



result_right = df_students.join(
    df_details_missing,
    how="right"
)

print(result_right)




result_outer = df_students.join(
    df_details_missing,
    how="outer"
)

print(result_outer)