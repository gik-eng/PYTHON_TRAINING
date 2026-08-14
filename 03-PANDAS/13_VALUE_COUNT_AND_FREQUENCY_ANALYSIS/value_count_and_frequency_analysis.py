"""
Exercise: Value Counts and Frequency Analysis

Difficulty: Simple

Description:
Analyze the frequency and distribution of categorical and numerical
data using Pandas.

Concepts:

- Pandas
- DataFrame
- value_counts()
- sort_index()
- normalize=True
- unique()
- nunique()
- Series Indexing
- Frequency Analysis


Exercise Tasks:

1. Count the number of students in each city.

2. Count the number of students for each age.

3. Count the frequency of each grade.

4. Sort the grade frequency by grade value instead of frequency.

5. Find the most common city and its frequency.

6. Calculate the percentage of students in each city.

7. Find the number of unique cities.

8. Find the unique city values.

9. Print all calculated results.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra", "Amir", "Leila", "Hassan", "Maryam"],
    "age": [20, 21, 19, 22, 20, 23, 21, 20, 22, 19],
    "grade": [18, 15, 19, 17, 14, 20, 16, 19, 15, 18],
    "city": [
        "Tehran",
        "Shiraz",
        "Tabriz",
        "Tehran",
        "Mashhad",
        "Tehran",
        "Shiraz",
        "Tabriz",
        "Tehran",
        "Shiraz"
    ]
}


df = pd.DataFrame(students)

students_per_city = df["city"].value_counts()

students_in_each_ages = df["age"].value_counts()

grades_frequency = df["grade"].value_counts()

sorted_grades_frequency = df["grade"].value_counts().sort_index()

city_frequency = df["city"].value_counts()
most_common_city = city_frequency.index[0]
most_common_city_count = city_frequency.iloc[0]

city_percentage = df["city"].value_counts(normalize= True) * 100

number_of_unique_cities = df["city"].nunique()
unique_cities = df["city"].unique()



print(f"Students per city: {students_per_city}")
print(f"Students per age: {students_in_each_ages}")
print(f"Grade frequency: {grades_frequency}")
print(f"Sorted grade frequency: {sorted_grades_frequency}")
print(f"Most common city: {most_common_city}")
print(f"Most common city count: {most_common_city_count}")
print(f"City percentages: {city_percentage}")
print(f"Number of unique cities: {number_of_unique_cities}")
print(f"Unique cities: {unique_cities}")