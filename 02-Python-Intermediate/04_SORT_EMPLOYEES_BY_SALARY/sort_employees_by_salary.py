"""
Exercise: Sort Employees by Salary

Difficulty: Intermediate

Description:
Sort a list of employee dictionaries based on salary values using a lambda function.

Concepts:
- Lists of Dictionaries
- Sorting
- Lambda Functions
- key Parameter
- Data Processing
"""

employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60}
]

#sorting employees by salary (descending)

employees = sorted(employees, key=lambda employee: employee["salary"], reverse=True)
print(employees)