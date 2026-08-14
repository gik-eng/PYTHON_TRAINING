"""
Exercise 25 - Pandas isin()

Practice filtering DataFrame rows using the isin() method.

Topics:
- Filtering rows by multiple values
- Using isin() with strings
- Using isin() with numbers
- Using ~ for NOT conditions
- Combining boolean filtering with DataFrame columns
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

not_in_tehran_shiraz = df[~df["city"].isin(["Tehran", "Shiraz"])]
print(not_in_tehran_shiraz)

in_tehran_shiraz_mashhad = df[df["city"].isin(["Tehran", "Shiraz", "Mashhad"])]
print(in_tehran_shiraz_mashhad)

names_are_ali_reza_zahra = df[df["name"].isin(["Ali", "Reza", "Zahra"])]
print(names_are_ali_reza_zahra)

grades_are_14_18_20 = df[df["grade"].isin([14, 18, 20])]
print(grades_are_14_18_20)

