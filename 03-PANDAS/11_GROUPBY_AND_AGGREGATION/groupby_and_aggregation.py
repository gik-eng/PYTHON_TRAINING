"""
Exercise: GroupBy and Aggregation

Difficulty: Simple

Description:
Group DataFrame rows based on a column and perform aggregation
operations on the grouped data.

Concepts:

- Pandas
- DataFrame
- groupby()
- Aggregation
- mean()
- max()
- min()
- count()
- agg()
- Multiple Column Selection


Exercise Tasks:

1. Group the students by city.

2. Calculate the average grade for each city.

3. Find the maximum grade for each city.

4. Find the minimum grade for each city.

5. Count the number of students in each city.

6. Calculate the maximum, minimum, and average grade for each
   city using the agg() method.

7. Calculate the average age and average grade for each city.

8. Print the results of the aggregation operations.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra", "Amir", "Leila"],
    "age": [20, 21, 19, 22, 20, 23, 21, 20],
    "grade": [18, 15, 19, 17, 14, 20, 16, 19],
    "city": [
        "Tehran",
        "Shiraz",
        "Tabriz",
        "Tehran",
        "Mashhad",
        "Tehran",
        "Shiraz",
        "Tabriz"
    ]
}


df = pd.DataFrame(students)

group_by_city = df.groupby("city")
average_grade_each_city = df.groupby("city")["grade"].mean()
maximum_grade_each_city = df.groupby("city")["grade"].max()
minimum_grade_each_city = df.groupby("city")["grade"].min()
students_each_city = df.groupby("city")["grade"].count()

##in another way
#filtered = df.groupby("city")["grade"].agg(
# ["max", "min", "mean"]
#)
#print(f"Grade statistics by city: {filtered}")


city_averages = df.groupby("city")[["grade", "age"]].mean()



print(f"Average grade by city: {average_grade_each_city}")
print(f"Maximum grade by city: {maximum_grade_each_city}")
print(f"Minimum grade by city: {minimum_grade_each_city}")
print(f"Number of students by city: {students_each_city}")
print(f"Average age and grade by city:{city_averages}")