"""
Exercise: Sorting Data

Difficulty: Simple

Description:
Sort a Pandas DataFrame by one or multiple columns in ascending
or descending order.

Concepts:

- Pandas
- DataFrame
- sort_values()
- Sorting
- Ascending Order
- Descending Order
- Multiple Column Sorting


Exercise Tasks:

1. Sort students by grade from lowest to highest.

2. Sort students by grade from highest to lowest.

3. Sort students by age from lowest to highest.

4. Sort students by age from highest to lowest.

5. Sort students by city in ascending order.

6. Sort students first by city and then by grade,
   both in ascending order.

7. Sort students first by city in ascending order
   and then by grade in descending order.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}


df = pd.DataFrame(students)

ascending_grades = df.sort_values(
    by= "grade",
    ascending= True
)
descending_grades = df.sort_values(
    by= "grade",
    ascending= False
)
ascending_age = df.sort_values(
    by= "age",
    ascending= True
)
descending_age = df.sort_values(
    by= "age",
    ascending= False
)

sorting_by_city = df.sort_values(
    by= "city",
    ascending=True
)
sorting_by_city_and_grades = df.sort_values(
    by=["city", "grade"],
    ascending=[True, False]
)

print(f"sorting grades ascending : {ascending_grades}")
print(f"sorting grades descending : {descending_grades}")
print(f"sorting ages ascending : {ascending_age}")
print(f"sorting ages descending : {descending_age}")
print(f"sorting city ascending : {sorting_by_city}")
print(f"sorting by city and grades : {sorting_by_city_and_grades}")
