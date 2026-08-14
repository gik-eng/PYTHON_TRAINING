"""
Exercise: Handling Missing Data

Difficulty: Simple

Description:
Identify, count, replace, and remove missing values in a Pandas
DataFrame.

Concepts:

- Pandas
- DataFrame
- Missing Values
- NaN
- isna()
- notna()
- fillna()
- mean()
- dropna()


Exercise Tasks:

1. Find all missing values in the DataFrame.

2. Count the number of missing values in each column.

3. Find students whose age is missing.

4. Find students whose grade is not missing.

5. Replace missing age values with 20.

6. Calculate the average grade and use it to replace missing
   grade values.

7. Remove rows where the city value is missing.

8. Print the final DataFrame.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, None, 22, 20, None],
    "grade": [18, 15, 19, None, 14, 20],
    "city": ["Tehran", "Shiraz", None, "Tehran", "Mashhad", "Tehran"]
}


df = pd.DataFrame(students)

df.isna()
df.isna().sum()
df[df["age"].isna()]
df[df["grade"].notna()]
df["age"] = df["age"].fillna(20)
average_grade = df["grade"].mean()
df["grade"] = df["grade"].fillna(average_grade)
df = df.dropna(subset=["city"])
print(df)