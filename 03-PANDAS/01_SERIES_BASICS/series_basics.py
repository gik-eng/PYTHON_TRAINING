"""
Exercise: Series Basics

Difficulty: Simple

Description:
Create a Pandas Series from a list of grades and perform basic
operations on the Series.

Concepts:

- Pandas
- Series
- min()
- max()
- len()
- Indexing


Exercise Tasks:

1. Create a Pandas Series from the grades list.

2. Find the minimum grade.

3. Find the maximum grade.

4. Find the number of grades.

5. Get the first grade using its index.

6. Calculate the average of all grades.
"""
import pandas as pd

grades = [18, 15, 20, 12, 17]

df = pd.Series(grades)
total = 0

min_grades = df.min()
max_grades = df.max()
length_grades = len(df)
for grade in grades :
    total += grade
    avg_grades = total / len(grades)


print(f"first grade of grades is {df[0]}")
print(f"maximum grade is {max_grades}")
print(f"minimum grade is {min_grades}")
print(f"number of grades is {length_grades}")
print(f"average of grades is {avg_grades} ")


