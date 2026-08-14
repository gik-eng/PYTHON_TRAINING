"""
Exercise 28 — Duplicate Data

This exercise focuses on detecting and removing duplicate
rows from a Pandas DataFrame.

Topics:
- duplicated()
- drop_duplicates()
- Detecting completely duplicated rows
- Detecting duplicates based on selected columns
- Removing duplicate records using subset
"""

import pandas as pd


students = {
    "name": [
        "Ali", "Sara", "Reza", "Mina",
        "Ali", "Nima", "Sara"
    ],
    "age": [
        20, 21, 19, 22,
        20, 20, 21
    ],
    "grade": [
        18, 15, 19, 17,
        18, 14, 15
    ],
    "city": [
        "Tehran", "Shiraz", "Tabriz", "Tehran",
        "Tehran", "Mashhad", "Shiraz"
    ]
}


df = pd.DataFrame(students)

print(df)

print(df.duplicated())
print(df[df.duplicated])
print(df.drop_duplicates())


print(df[df.duplicated(subset=["name"])])
print(df.drop_duplicates(subset=["name"]))
