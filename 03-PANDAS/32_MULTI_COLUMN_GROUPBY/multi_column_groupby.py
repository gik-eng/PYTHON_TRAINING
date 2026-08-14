"""
Exercise 32 — Multi-Column GroupBy

This exercise focuses on grouping DataFrame data
using multiple columns at the same time.

Topics:
- Grouping by multiple columns
- Grouping by city and gender
- Aggregating grouped data
- Calculating mean, count, max, and min
- Selecting multiple columns after groupby()
"""

import pandas as pd


students = {
    "name": [
        "Ali", "Sara", "Reza", "Mina",
        "Nima", "Zahra", "Amir", "Leila"
    ],
    "gender": [
        "M", "F", "M", "F",
        "M", "F", "M", "F"
    ],
    "age": [20, 21, 19, 22, 20, 23, 21, 20],
    "grade": [18, 15, 19, 17, 14, 20, 16, 19],
    "city": [
        "Tehran", "Shiraz", "Tehran", "Tehran",
        "Mashhad", "Tehran", "Mashhad", "Shiraz"
    ]
}


df = pd.DataFrame(students)

print(df)

average_grade = df.groupby(
    ["city", "gender"]
)["grade"].mean()

print(average_grade)


students_count = df.groupby(
    ["city", "gender"]
)["name"].count()

print(students_count)


average_grade_and_age = df.groupby(
    ["city", "gender"]
)[["grade", "age"]].mean()

print(average_grade_and_age)


maximum_grade = df.groupby(
    ["city", "gender"]
)["grade"].max()

print(maximum_grade)


minimum_age = df.groupby(
    ["city", "gender"]
)["age"].min()

print(minimum_age)

count_and_average = df.groupby(
    ["city", "gender"]
)["grade"].agg(["mean", "count"])

print(count_and_average)