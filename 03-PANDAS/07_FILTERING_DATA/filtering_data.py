"""
Exercise: Filtering Data

Difficulty: Simple

Description:
Filter rows from a Pandas DataFrame using single and multiple
Boolean conditions.

Concepts:

- Pandas
- DataFrame
- Boolean Filtering
- Conditional Selection
- Comparison Operators
- AND Conditions
- OR Conditions


Exercise Tasks:

1. Filter students whose grade is greater than 17.

2. Filter students whose age is at least 21.

3. Filter students who live in Tehran.

4. Filter students whose grade is at least 18.

5. Filter students whose age is at least 20
   AND whose grade is at least 17.

6. Filter students whose grade is lower than 15
   OR whose age is greater than 22.
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}

df = pd.DataFrame(students)

grades_17 = df[df["grade"] > 17]
grades_18 = df[df["grade"] >= 18]
ages_21 = df[df["age"] >= 21]
in_tehran = df[df["city"] == "Tehran"]
filter1 = df[(df["grade"] >= 17) & (df["age"] >= 20)] 
filter2 = df[(df["grade"] < 15) | (df["age"] > 22)]

print(f"Grades greater than 17:\n{grades_17}")
print(f"Grades at least 18:\n{grades_18}")
print(f"Ages at least 21:\n{ages_21}")
print(f"Students in Tehran:\n{in_tehran}")
print(f"Grades at least 17 AND ages at least 20:\n{filter1}")
print(f"Grades lower than 15 OR ages greater than 22:\n{filter2}")
