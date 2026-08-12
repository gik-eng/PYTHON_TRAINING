"""
Exercise: Dictionary Merge with Preserved Values

Difficulty: Simple

Description:
Merge two dictionaries while preserving duplicate values by storing them in a list.

Concepts:
- Dictionaries
- Loops
- Conditional Statements
- Data Merging
- Lists
"""

#checking duplicate keys

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = {}


#creating merged dictionary

for key in d1:  
    if key in d2:
        result[key] = [d1[key], d2[key]]
    else:
        result[key] = d1[key]  
print(result)