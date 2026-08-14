"""
Exercise 26 - Pandas unique() and nunique()

Practice finding unique values and counting unique values
in DataFrame columns.

Topics:
- Using unique()
- Using nunique()
- Finding unique values in a column
- Counting unique values in a column
- Checking unique counts for all columns
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": [
        "Tehran",
        "Shiraz",
        "Tabriz",
        "Tehran",
        "Mashhad",
        "Tehran"
    ]
}


df = pd.DataFrame(students)

print(df)

cities = df["city"].unique()
print(cities)

number_of_cities = df["city"].nunique()
print(number_of_cities)

number_of_ages = df["age"].nunique()
print(number_of_ages)

number_of_grades = df["grade"].nunique()
print(number_of_grades)

all_unique = df.nunique()
print(all_unique)