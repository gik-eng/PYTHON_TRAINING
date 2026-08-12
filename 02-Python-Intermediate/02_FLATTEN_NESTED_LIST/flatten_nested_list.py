"""
Exercise: Flatten Nested List

Difficulty: Intermediate

Description:
Flatten a nested list into a single list using recursion.

Concepts:
- Recursion
- Lists
- Nested Data Structures
- isinstance()
- Functions
"""

def flatten(data) :
    result = []

#checking nested list

    for word in data :
        if isinstance(word, list) :

#recursive flatten

            result.extend(flatten(word))
        else :
            result.append(word)
    return result
data = [1, [2, 3], [4, [5, 6]], 7]            
print(flatten(data))