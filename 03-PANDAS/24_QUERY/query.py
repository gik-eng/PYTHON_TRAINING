"""
Exercise 24 - Pandas query()

Practice filtering DataFrame rows using the query() method.

Topics:
- Filtering rows with conditions
- Comparing numeric values
- Comparing string values
- Using == for comparisons
- Using & for AND conditions
- Using | for OR conditions
- Combining multiple filtering conditions
"""

import pandas as pd

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": [
        "Tehran",
        "Shiraz",
        "Tabriz",
        "Tehran",
        "Mashhad",
        "Tehran"
    ]
}

df = pd.DataFrame(students)

filter_grade = df.query("grade > 17")
print(filter_grade)

filter_age = df.query("age >= 21")
print(filter_age)

filter_city = df.query("city == 'Tehran'")
print(filter_city)

filter_grade_and_age = df.query("grade >= 15 & age < 22") 
print(filter_grade_and_age)

filter_city_or_grade = df.query("city == 'Tehran' | grade > 19")
print(filter_city_or_grade)
