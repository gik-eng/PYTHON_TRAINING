"""
Exercise 21 - Pandas map()

Practice using map() with dictionaries, functions, and lambda
expressions to transform DataFrame column values.

Topics:
- map() with dictionaries
- map() with functions
- map() with lambda
- Conditional mapping
- Creating transformed columns
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}

df = pd.DataFrame(students)


city_codes = {
    "Tehran" : "TH",
    "Shiraz" : "SH",
    "Tabriz" : "TB",
    "Mashhad" : "MA"

}

df["c_city"] = df["city"].map(city_codes)
print(df)

df["status"] = df["grade"].map(
    lambda grade: "Excellent" if grade >= 18
    else "Good" if grade >= 15
    else "Needs Improvement"
)

print(df)


def make_upper(name) :
    return name.upper()

df["upper_name"] = df["name"].map(make_upper)
print(df)