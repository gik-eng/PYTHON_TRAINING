"""
Exercise: Pivot Tables

Difficulty: Simple

Description:
Learn how to summarize and analyze data using Pandas pivot_table().
This exercise focuses on grouping data and calculating statistics
across different categories.

Concepts:

- Pandas
- DataFrame
- pivot_table()
- values
- index
- columns
- aggfunc
- mean
- max
- min
- count
- Multiple values
- Multiple dimensions


Exercise Tasks:

1. Create a DataFrame containing student information.

2. Calculate the average grade for each city.

3. Find the maximum grade for each city.

4. Find the minimum grade for each city.

5. Calculate multiple grade statistics for each city.

6. Calculate the average grade for each city and gender.

7. Count the number of students in each city and gender.

8. Calculate the average age and grade for each city.


Challenge:

Create a pivot table that shows the average grade of
male and female students in each city.

Requirements:

- Use pd.pivot_table().
- Use "grade" as the value.
- Use "city" as the index.
- Use "gender" as the columns.
- Use "mean" as the aggregation function.
"""


import pandas as pd


# =========================
# Creating DataFrame
# =========================

students = {
    "name": [
        "Ali", "Sara", "Reza", "Mina", "Nima",
        "Zahra", "Amir", "Leila", "Hassan", "Maryam"
    ],

    "gender": [
        "M", "F", "M", "F", "M",
        "F", "M", "F", "M", "F"
    ],

    "city": [
        "Tehran", "Shiraz", "Tehran", "Tabriz", "Shiraz",
        "Tehran", "Tabriz", "Shiraz", "Tehran", "Tabriz"
    ],

    "grade": [
        18, 15, 19, 17, 14,
        20, 16, 19, 15, 18
    ],

    "age": [
        20, 21, 19, 22, 20,
        23, 21, 20, 22, 19
    ]
}


df = pd.DataFrame(students)


print("Students DataFrame:")
print(df)


# =========================
# Average Grade by City
# =========================

average_grade_by_city = pd.pivot_table(
    df,
    values="grade",
    index="city",
    aggfunc="mean"
)


print("Average Grade by City:")
print(average_grade_by_city)


# =========================
# Maximum Grade by City
# =========================

maximum_grade_by_city = pd.pivot_table(
    df,
    values="grade",
    index="city",
    aggfunc="max"
)


print("Maximum Grade by City:")
print(maximum_grade_by_city)


# =========================
# Minimum Grade by City
# =========================

minimum_grade_by_city = pd.pivot_table(
    df,
    values="grade",
    index="city",
    aggfunc="min"
)


print("Minimum Grade by City:")
print(minimum_grade_by_city)


# =========================
# Grade Statistics by City
# =========================

grade_statistics_by_city = pd.pivot_table(
    df,
    values="grade",
    index="city",
    aggfunc=["mean", "max", "min"]
)


print("Grade Statistics by City:")
print(grade_statistics_by_city)


# =========================
# Average Grade by City and Gender
# =========================

grade_by_city_gender = pd.pivot_table(
    df,
    values="grade",
    index="city",
    columns="gender",
    aggfunc="mean"
)


print("Average Grade by City and Gender:")
print(grade_by_city_gender)


# =========================
# Number of Students by City and Gender
# =========================

total_students = pd.pivot_table(
    df,
    values="name",
    index="city",
    columns="gender",
    aggfunc="count"
)


print("Number of Students by City and Gender:")
print(total_students)


# =========================
# Average Age and Grade by City and Gender
# =========================

average_grade_and_age_by_city = pd.pivot_table(
    df,
    values=["grade", "age"],
    index="city",
    columns="gender",
    aggfunc="mean"
)


print("Average Age and Grade by City and Gender:")
print(average_grade_and_age_by_city)


# =========================
# Challenge
# =========================

challenge = pd.pivot_table(
    df,
    values="grade",
    index="city",
    columns="gender",
    aggfunc="mean"
)


print("Challenge:")
print(challenge)