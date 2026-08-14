"""
Exercise 27 — between() & str.contains()

This exercise focuses on filtering DataFrame rows using
numeric ranges and text-based conditions.

Topics:
- between()
- str.contains()
- Combining multiple filtering conditions
- Case-sensitive string searching
- Using & to combine conditions
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

age_between = df[df["age"].between(20, 22)]
print(age_between)

grade_between = df[df["grade"].between(15, 19)]
print(grade_between)




tehran_students = df[df["city"].str.contains("Teh")]
print(tehran_students)

names_with_a = df[df["name"].str.contains("a")]
print(names_with_a)

names_with_A = df[df["name"].str.contains("A")]
print(names_with_A)


grades_between_15_20_and_cities_with_Teh = df[
    df["grade"].between(15, 20) & 
    df["city"].str.contains("Teh")
]   
print(grades_between_15_20_and_cities_with_Teh)
