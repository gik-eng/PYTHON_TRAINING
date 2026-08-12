"""
Exercise: Remove Duplicates

Difficulty: Simple

Description:
Remove duplicate elements from a list while preserving their original order.

Concepts:
- Lists
- Sets
- Functions
- Loops
- Membership Testing
"""

def remove_duplicates(items):

#keeping unique items only
    
    seen = set()
    result = []
    for item in items :
        if item not in seen :
            result.append(item)
            seen.add(item)
    return result

items = [1, 2, 2, 3, 1, 4, 2]
print(remove_duplicates(items))
