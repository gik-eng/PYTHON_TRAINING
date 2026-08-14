"""
Exercise: apply() and Custom Functions

Difficulty: Simple

Description:
Use custom Python functions with the Pandas apply() method to
transform values and create new DataFrame columns.

Concepts:

- Pandas
- DataFrame
- apply()
- Custom Functions
- if / elif / else
- String Methods
- Column Transformation


Exercise Tasks:

1. Create a function that returns "Passed" if a student's grade
   is at least 15, otherwise return "Failed".

2. Apply the function to the grade column and create a "status"
   column.

3. Create a function that categorizes grades into four levels:
   Excellent, Good, Average, and Poor.

4. Apply the grade-level function and create a "level" column.

5. Create a function that calculates a student's age after
   five years and apply it to create a new column.

6. Create a function that converts student names to uppercase
   and apply it to create a new column.

7. Print the final DataFrame.
"""

import pandas as pd


students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}


df = pd.DataFrame(students)

def check_passed(grade) :
    if grade >= 15 :
        return "Passed"
    else :
        return "Failed"
df["status"] = df["grade"].apply(check_passed)




def level(grade) :
    if grade >= 18 :
        return "Excellent"
    elif grade >= 15 :
        return "Good"
    elif grade >= 12 :
        return "Average"
    else :
        return "Poor"
df["level"] = df["grade"].apply(level)


def next_5_year_age(age) :
    age += 5
    return age
df["next_5_year_age"] = df["age"].apply(next_5_year_age)



def upper(name) :
    upper_name = name.upper()
    return upper_name
df["upper_name"] = df["name"].apply(upper)



    
print(df)    

