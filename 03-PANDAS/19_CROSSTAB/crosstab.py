"""
Exercise: Crosstab

Difficulty: Simple

Description:
Learn how to use Pandas crosstab() to count, compare,
and analyze categorical data.

The exercise focuses on creating frequency tables,
calculating percentages, and calculating aggregated
values between two categorical variables.


Concepts:

- Pandas
- DataFrame
- pd.crosstab()
- Frequency tables
- index
- columns
- normalize
- normalize="index"
- normalize="all"
- values
- aggfunc
- mean


Exercise Tasks:

1. Create a DataFrame containing student information
   such as name, gender, city, grade, and age.


2. Use pd.crosstab() to find the number of students
   in each city.


3. Create a crosstab showing the number of male and
   female students in each city.


4. Reverse the rows and columns of the previous
   crosstab so that gender is the index and city
   is the columns.


5. Calculate the percentage of male and female
   students within each city.

   Hint:
   Use normalize="index".


6. Calculate the percentage of students in each
   city and gender combination relative to the
   entire DataFrame.

   Hint:
   Use normalize="all".


7. Calculate the average grade of male and female
   students in each city.

   Requirements:

   - city → index
   - gender → columns
   - grade → values
   - mean → aggregation function


Challenge:

Create a crosstab that shows the average grade
of male and female students in each city.

Expected structure:

gender       F       M
city
Shiraz       ?       ?
Tabriz       ?       ?
Tehran       ?       ?

Requirements:

- Use pd.crosstab().
- Use "city" as the index.
- Use "gender" as the columns.
- Use "grade" as the values.
- Use "mean" as the aggregation function.


Goal:

By completing this exercise, you should understand
how crosstab() can be used to create frequency tables,
calculate percentages, and summarize numerical data
based on categorical variables.
"""

import pandas as pd


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

print(df)


students_per_city = pd.crosstab(
    df["city"],
    columns= "count"
)

print(students_per_city)




gender_by_city = pd.crosstab(
    df["city"],
    df["gender"]
)

print(gender_by_city)


city_by_gender = pd.crosstab(
    df["gender"],
    df["city"]
)

print(city_by_gender)


gender_percentage_by_city = pd.crosstab(
    df["city"],
    df["gender"],
    normalize="index"
) * 100 

print(gender_percentage_by_city)


gender_percentage_by_all = pd.crosstab(
    df["city"],
    df["gender"],
    normalize= "all"
) * 100

print(gender_percentage_by_all)



# =========================
# Challenge
# =========================

challenge = pd.crosstab(
    df["city"],
    df["gender"],
    values= df["grade"],
    aggfunc= "mean"
)

print(challenge)