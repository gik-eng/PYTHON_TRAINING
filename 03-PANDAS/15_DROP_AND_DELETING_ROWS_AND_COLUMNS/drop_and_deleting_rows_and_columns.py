"""
Exercise: Dropping Rows and Columns

Difficulty: Simple

Description:
Learn how to remove unnecessary rows and columns from a Pandas
DataFrame using drop(), inplace=True, and reset_index().

Concepts:

- Pandas
- DataFrame
- drop()
- columns
- index
- inplace=True
- reset_index()
- Filtering
- Finding row indexes


Exercise Tasks:

1. Remove a single column using drop().

2. Remove multiple columns using drop().

3. Remove a single row using its index.

4. Remove multiple rows using their indexes.

5. Understand the difference between drop() and dropna().

6. Use inplace=True to modify the DataFrame directly.

7. Reset the DataFrame index after removing rows.

Challenge:

1. Find the student whose grade is 14 using filtering.

2. Find the index of that student.

3. Remove the student using drop().

4. Reset the DataFrame index.

5. Print the final DataFrame.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"],
    "temporary": [100, 200, 300, 400, 500, 600]
}


df = pd.DataFrame(students)
df2 = pd.DataFrame(students)
challenge_df = pd.DataFrame(students)

df = df.drop(columns= ["temporary"])
print(f"without inplace True : {df}")

df2.drop(columns=["temporary"], inplace=True)
print(f"inplace True : {df2}")

df = df.drop(columns= ["city", "age"])
print(df)

df = df.drop(index=[2])
print(df)

df = df.drop(index=[1, 4])
df = df.reset_index(drop=True)
print(df)

challenge_index = challenge_df[challenge_df["grade"] == 14].index
challenge_df = challenge_df.drop(index=challenge_index)
challenge_df = challenge_df.reset_index(drop=True)
print(challenge_df)