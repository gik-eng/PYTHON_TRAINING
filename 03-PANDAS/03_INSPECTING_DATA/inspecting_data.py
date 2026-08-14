"""
Exercise: Inspecting Data

Difficulty: Simple

Description:
Inspect the structure, summary statistics, and basic information
of a Pandas DataFrame.

Concepts:

- Pandas
- DataFrame
- head()
- tail()
- describe()
- shape
- columns
- dtypes
- info()


Exercise Tasks:

1. Display the first 5 rows.

2. Display the last 2 rows.

3. Generate descriptive statistics using describe().

4. Find the shape of the DataFrame.

5. Display the column names.

6. Display the data types of the columns.

7. Display general information about the DataFrame using info().
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20]
}

df = pd.DataFrame(students)

first_5_rows = df.head(5)
last_2_rows = df.tail(2)
description = df.describe()
shape_of_DataFrame = df.shape
columns = df.columns
types = df.dtypes


print(f"first 5 rows are {first_5_rows}")
print(f"last 2 rows are {last_2_rows}")
print(f"our columns are {columns}")
print(f"our types are {types}") 

df.info()
print(f"description of our Data Frame : {description}")
print(f"shape of our Data Frame : {shape_of_DataFrame}")

