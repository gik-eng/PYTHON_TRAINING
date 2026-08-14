"""
Exercise 30 — Vectorized Operations

This exercise focuses on performing operations directly
on Pandas Series without using explicit loops.

Topics:
- Vectorized arithmetic operations
- Operations between columns
- Creating calculated columns
- Multiplication and division between Series
- Avoiding unnecessary loops and apply()
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "daily_study_hours": [3, 2, 4, 3, 1, 5]
}


df = pd.DataFrame(students)


print(df)

df["new_grade"] = df["grade"] + 1

df["age_in_5_years"] = df["age"] + 5

df["weekly_study_hours"] = df["daily_study_hours"] * 7

df["grade_per_study"] = (
    df["grade"] / df["daily_study_hours"]
) 

df["grades_in_percentage"] = df["grade"] * 5

df["study_hours_after_2x"] = df["daily_study_hours"] * 2

df["age_grade_score"] = df["age"] * df["grade"]


print(df)