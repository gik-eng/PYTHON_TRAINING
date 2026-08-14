"""
Exercise 22 - Pandas replace()

Practice using replace() to modify existing values in a DataFrame.

Topics:
- Replacing single values
- Replacing multiple values with a dictionary
- Replacing string values
- Replacing numeric values
- Changing column data types with astype()
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "gender": ["M", "F", "M", "F", "M", "F"],
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

df["gender"] = df["gender"].replace({
    "M" : "Male",
    "F" : "Female"   
})
print(df)

df["city"] = df["city"].replace({
    "Tehran" : "TEH",
    "Shiraz" : "SHI",
    "Tabriz" : "TAB",
    "Mashhad" : "MAS"
})
print(df)

df["grade"] = df["grade"].replace(15, 16)
print(df)


df["grade"] = df["grade"].astype(float)
print(df)

