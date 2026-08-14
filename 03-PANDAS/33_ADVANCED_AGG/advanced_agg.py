"""
Exercise 33 — Advanced Aggregation with agg()

This exercise focuses on applying multiple aggregation
functions to DataFrame columns.

Topics:
- agg()
- Multiple aggregations on a Series
- Multiple aggregations on multiple columns
- Dictionary-based aggregation
- Named aggregation
- Custom names for aggregated results
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

grade_stats = df["grade"].agg(
    ["mean", "min", "max", "std"]
)

print(grade_stats)


statistics = df.agg({
    "age" : ["mean", "min", "max", "std"],
    "grade" : ["mean", "min", "max", "std"]
})

print(statistics)



statistics2 = df.agg(
    average_age=("age", "mean"),
    minimum_age=("age", "min"),
    maximum_age=("age", "max"),
    average_grade=("grade", "mean"),
    highest_grade=("grade", "max")
)

print(statistics2)


statistics3 = df.agg(
    average_age = ("age", "mean"),
    maximum_age = ("age", "max"),
    average_grade = ("grade", "mean"),
    minimum_grade = ("grade", "min"),
    maximum_grade = ("grade", "max")
)

print(statistics3)