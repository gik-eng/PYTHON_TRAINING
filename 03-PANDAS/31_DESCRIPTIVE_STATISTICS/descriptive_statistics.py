"""
Exercise 31 — Descriptive Statistics

This exercise focuses on analyzing numerical data
using descriptive statistical methods in Pandas.

Topics:
- mean()
- median()
- std()
- min()
- max()
- count()
- describe()
- Comparing statistical values
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

grade_mean = df["grade"].mean()
print(f"average : {grade_mean}")

grade_median = df["grade"].median()
print(f"grade median : {grade_median}")

grade_std = df["grade"].std()
print(f"grade std : {grade_std}")

grade_min = df["grade"].min()
print(f"grade minimum : {grade_min}")

grade_max = df["grade"].max()
print(f"grade maximum : {grade_max}")

grade_count = df["grade"].count()
print(f"grade count : {grade_count}")


grade_statistics = df["grade"].describe()
print(f"grade statistics : {grade_statistics}")

age_statistics = df["age"].describe()
print(f"age statistics : {age_statistics}")


age_mean = df["age"].mean()

if grade_mean > age_mean : 
    print("Grade average is higher")
else : 
    print("Age average is higher")    