"""
Exercise 20: Pandas apply() and lambda

Difficulty: Simple

Description:
Learn how to use the Pandas apply() method with regular
functions and lambda functions to transform and analyze
DataFrame columns and rows.

This exercise also introduces using apply() with axis=1
to process each row of a DataFrame.


Concepts:

- Pandas
- DataFrame
- apply()
- lambda
- Custom functions
- Conditional logic
- String methods
- axis=0
- axis=1
- Row-wise operations
- Column-wise operations
- f-strings


Exercise Tasks:

1. Create a DataFrame containing student information.

2. Create a function that checks whether a student has passed.

   Rules:
   - grade >= 15 -> Passed
   - grade < 15 -> Failed

3. Use a lambda function with apply() to create a
   boolean column indicating whether each student passed.

4. Create a function that classifies students based
   on their grades.

   Rules:
   - grade >= 18 -> Excellent
   - grade >= 15 -> Good
   - grade >= 12 -> Average
   - grade < 12 -> Poor

5. Use apply() to calculate the student's age
   five years from now.

6. Use apply() and a lambda function to convert
   student names to uppercase.

7. Use apply() on multiple numeric columns to
   calculate their averages.

8. Use apply() with axis=1 to calculate the sum
   of age and grade for each student.

Challenge:

Create a new column called "student_summary".

The column should contain a formatted summary
for each student.

Example:

Ali - Tehran - Grade: 18
Sara - Shiraz - Grade: 15
Reza - Tabriz - Grade: 19

Requirements:

- Use DataFrame.apply().
- Use axis=1.
- Create a custom function named create_summary().
- Access the name, city, and grade columns.
- Return the result as a formatted string.


Goal:

By completing this exercise, you should understand
how apply() can be used with both Series and DataFrames,
how lambda functions can simplify simple operations,
and how axis=1 allows row-wise processing.
"""


import pandas as pd


# =========================
# Creating DataFrame
# =========================

students = {
    "name": ["Ali", "Sara", "Reza", "Mina", "Nima", "Zahra"],
    "age": [20, 21, 19, 22, 20, 23],
    "grade": [18, 15, 19, 17, 14, 20],
    "city": ["Tehran", "Shiraz", "Tabriz", "Tehran", "Mashhad", "Tehran"]
}


df = pd.DataFrame(students)


print(df)


# =========================
# Task 1
# Check Passed Students
# =========================

def grade_check(grade):
    """
    Check whether a student's grade is passing.

    Args:
        grade (int or float): The student's grade.

    Returns:
        str: "Passed" if the grade is 15 or higher,
             otherwise "Failed".
    """
    if grade >= 15:
        return "Passed"
    else:
        return "Failed"


df["status"] = df["grade"].apply(grade_check)


print(df)


# =========================
# Task 2
# Lambda Function
# =========================

df["status"] = df["grade"].apply(
    lambda grade: grade >= 15
)


print(df)


# =========================
# Task 3
# Grade Level
# =========================

def grade_level(grade):
    """
    Classify a student's grade into a performance level.

    Args:
        grade (int or float): The student's grade.

    Returns:
        str: The performance level:
             "Excellent", "Good", "Average", or "Poor".
    """
    if grade >= 18:
        return "Excellent"
    elif grade >= 15:
        return "Good"
    elif grade >= 12:
        return "Average"
    else:
        return "Poor"


df["level"] = df["grade"].apply(grade_level)


print(df)


# =========================
# Task 4
# Age After Five Years
# =========================

df["age_after_5_years"] = df["age"].apply(
    lambda age: age + 5
)


print(df)


# =========================
# Task 5
# Uppercase Names
# =========================

df["upper_names"] = df["name"].apply(
    lambda name: name.upper()
)


print(df)


# =========================
# Task 6
# Column-wise Apply
# =========================

numeric_columns = df[["age", "grade"]]


averages = numeric_columns.apply(
    lambda column: column.mean()
)


print(averages)


# =========================
# Task 7
# Row-wise Apply
# =========================

grade_plus_age = numeric_columns.apply(
    lambda row: row.sum(),
    axis=1
)


print(grade_plus_age)


# =========================
# Challenge
# =========================

def create_summary(row):
    """
    Create a short summary containing a student's
    name, city, and grade.

    Args:
        row (pandas.Series): A row from the students DataFrame.

    Returns:
        str: A formatted summary of the student's information.
    """
    return f"{row['name']} - {row['city']} - Grade: {row['grade']}"


df["student_summary"] = df.apply(
    create_summary,
    axis=1
)


print(df)