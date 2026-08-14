"""
Exercise: Rename Columns and Index Management

Difficulty: Simple

Description:
Rename DataFrame columns, create a custom index, select rows
using index labels with loc, and reset the index.

Concepts:

- Pandas
- DataFrame
- rename()
- columns
- Index
- loc
- reset_index()
- Custom Index


Exercise Tasks:

1. Rename the "name" column to "student_name".

2. Rename multiple columns:
   - age -> student_age
   - grade -> final_grade
   - city -> student_city

3. Inspect the original DataFrame index.

4. Create a custom index using student IDs from ST001 to ST006.

5. Select student ST003 using loc.

6. Select students ST002 through ST004 using loc.

7. Reset the DataFrame index back to the default integer index.

8. Print the DataFrame and the selected rows.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}


df = pd.DataFrame(students)

#one column
df = df.rename(columns={"name" : "student_name"})

#many columns
df = df.rename(columns={
    "age" : "student_age",
    "grade" : "final_grade",
    "city" : "student_city"
    })


df.index = ["ST001", "ST002", "ST003", "ST004", "ST005", "ST006"]

print(f"custome index : {df}")

student_ST003 = df.loc["ST003"]
students_ST002_to_ST004 = df.loc["ST002" : "ST004"]

print(f"student ST003 : {student_ST003}")
print(f"students ST002 to ST004 : {students_ST002_to_ST004}")


df = df.reset_index(drop= True)

print(f"original index : {df}")

