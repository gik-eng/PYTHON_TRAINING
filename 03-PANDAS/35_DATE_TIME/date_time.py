"""
Exercise 35 — Datetime

This exercise focuses on working with date and time data
in Pandas.

Topics:
- pd.to_datetime()
- Datetime columns
- Extracting year, month, and day
- Extracting weekday and month names
- Date filtering with between()
- Filtering by month
- Date subtraction
- Calculating date differences in days
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "birth_date": [
        "2005-03-15",
        "2004-07-22",
        "2006-01-10",
        "2003-11-05",
        "2005-09-18",
        "2002-06-30"
    ],
    "registration_date": [
        "2024-09-01",
        "2024-09-03",
        "2024-09-05",
        "2024-09-10",
        "2024-09-12",
        "2024-09-15"
    ],
    "grade": [18, 15, 19, 17, 14, 20]
}


df = pd.DataFrame(students)

print(df)
print(df.dtypes)


df["birth_date"] = pd.to_datetime(df["birth_date"])
df["registration_date"] = pd.to_datetime(
    df["registration_date"]
)

print(df.dtypes)


df["birth_year"] = df["birth_date"].dt.year
df["birth_month"] = df["birth_date"].dt.month
df["birth_day"] = df["birth_date"].dt.day
df["birth_weekday"] = df["birth_date"].dt.day_name()

print(df)



df["registration_year"] = (
    df["registration_date"].dt.year
)

df["registration_month"] = (
    df["registration_date"].dt.month
)

print(df)


filtered_students = df[
    df["registration_date"].between(
        "2024-09-03",
        "2024-09-10"
    )
]

print(filtered_students)


df["birth_month_name"] = (
    df["birth_date"].dt.month_name()
)

print(df)

sep_students = df["registration_date"].dt.month == 9
print(sep_students)

df["diff_date"] = (
    df["registration_date"] - df["birth_date"]
).dt.days

print(df)

