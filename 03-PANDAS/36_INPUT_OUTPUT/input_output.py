"""
Exercise 36 — Pandas Input / Output

This exercise focuses on reading and writing data
using Pandas.

Topics:
- read_csv()
- to_csv()
- read_excel()
- to_excel()
- read_json()
- to_json()
- Basic introduction to read_sql()
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": [
        "Tehran",
        "Shiraz",
        "Tehran",
        "Tabriz",
        "Mashhad",
        "Tehran"
    ]
}


df = pd.DataFrame(students)

print(df)

df.to_csv(
    "students.csv",
    index=False
)
df_csv = pd.read_csv("students.csv")

print(df_csv)
print(df_csv.dtypes)



df.to_excel(
    "students.xlsx",
    index=False
)
df_excel = pd.read_excel("students.xlsx")

print(df_excel)




df.to_json(
    "students.json",
    orient="records",
    indent=4
)
df_json = pd.read_json("students.json")

print(df_json)




# Challenge 1
high_grade_students = df_csv[
    df_csv["grade"] >= 18
]

print(high_grade_students)


# Challenge 2
high_grade_students.to_csv(
    "high_grade_students.csv",
    index=False
)


# Challenge 3
high_grade_students.to_json(
    "high_grade_students.json",
    orient="records",
    indent=4
)


# Challenge 4
high_grade_from_json = pd.read_json(
    "high_grade_students.json"
)

print(high_grade_from_json)