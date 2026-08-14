"""
Exercise 23 - Pandas Data Types

Practice converting DataFrame columns between different data types.

Topics:
- Checking data types with dtypes
- Converting strings to integers
- Converting strings to floats
- Converting strings to booleans
- Using map() for boolean conversion
- Calculating averages after type conversion
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": ["20", "21", "19", "22", "20", "23"],
    "grade": ["18", "15", "19", "17", "14", "20"],
    "passed": ["True", "True", "True", "True", "False", "True"]
}

df = pd.DataFrame(students)

print(df)
print(df.dtypes)

df["age"] = df["age"].astype(int)
print(df.dtypes)

df["grade"] = df["grade"].astype(float)
print(df.dtypes)

df["passed"] = df["passed"].map({
    "True" : True,
    "False" : False
})

print(df.dtypes)

average_age = df["age"].mean()
average_grade = df["grade"].mean()

print(f"Grades average is {average_grade} and ages average is {average_age}")
