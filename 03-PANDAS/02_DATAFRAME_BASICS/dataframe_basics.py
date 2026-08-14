"""
Exercise: DataFrame Basics

Difficulty: Simple

Description:
Create a Pandas DataFrame from a dictionary and inspect its
basic structure and properties.

Concepts:

- Pandas
- DataFrame
- Dictionary
- columns
- shape
- dtypes
- iloc


Exercise Tasks:

1. Create a DataFrame from the students dictionary.

2. Display the DataFrame columns.

3. Find the number of rows and columns using shape.

4. Display the data types of the columns.

5. Select and display the first student using iloc.
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "age": [20, 21, 19, 22],
    "grade": [18, 15, 19, 17]
}

df = pd.DataFrame(students)
columns = df.columns
rows_and_columns = df.shape
types = df.dtypes
first_student = df.iloc[0]


print(f"our first student is {first_student}")
print(f"our columns are {columns}")
print(f"our rows and columns are {rows_and_columns}")
print(f"our data type are {types}")
