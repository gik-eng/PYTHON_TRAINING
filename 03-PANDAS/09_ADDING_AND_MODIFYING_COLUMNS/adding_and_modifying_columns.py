"""
Exercise: Adding and Modifying Columns

Difficulty: Simple

Description:
Create, modify, and remove columns in a Pandas DataFrame.
Perform calculations and create new columns based on existing data.

Concepts:

- Pandas
- DataFrame
- Adding Columns
- Modifying Columns
- Boolean Conditions
- Column Calculations
- String Operations
- drop()
- Column Removal


Exercise Tasks:

1. Create a "passed" column that contains True if the student's
   grade is at least 15, otherwise False.

2. Create a "grade_plus_1" column by increasing each student's
   grade by 1.

3. Create an "age_next_year" column containing each student's
   age for the next year.

4. Increase the existing "grade" column by 2.

5. Create a "student_info" column by combining the student's
   name and city.

6. Remove the "passed" column from the DataFrame.

7. Print the final DataFrame.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}


df = pd.DataFrame(students)

df["passed"] = df["grade"] >= 15 
df["grade_plus_1"] = df["grade"] + 1
df["age_next_year"] = df["age"] + 1
df["grade"] = df["grade"] +2
df["student_info"] = df["name"] + "---" + df["city"]

print(df)

df = df.drop(columns=["passed"])

print(df)