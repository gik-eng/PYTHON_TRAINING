"""
Exercise: Merge Sorted Lists

Difficulty: Intermediate

Description:
Merge two sorted lists into a single sorted list without using built-in sorting functions.

Concepts:
- Lists
- Two Pointer Technique
- Loops
- Conditional Logic
- Algorithm Design
"""

list1 = [1, 3, 5, 7, 9, 11]
list2 = [2, 4, 6, 8]
merged_list = []

# Pointers for tracking current positions in both lists
i , j = 0, 0

# Compare elements and add the smaller one
while i < len(list1) and j < len(list2) :
    if list1[i] <= list2[j] :
        merged_list.append(list1[i])
        i += 1
    else : 
        merged_list.append(list2[j])
        j += 1

# Add remaining elements from list1
while i < len(list1) :
    merged_list.append(list1[i])
    i += 1

# Add remaining elements from list2
while j < len(list2) :
    merged_list.append(list2[j])
    j += 1

print(f"Merged sorted list : {merged_list}")
 