"""
Exercise: List Rotation

Difficulty: Intermediate

Description:
Rotate the elements of a list left or right by a given number of positions using slicing.

Concepts:
- Lists
- Slicing
- Functions
- Modulo Operator
- Algorithm Design
"""

#rotating list

def rotate (lst, n, direction) :
    if direction == 'left':
        n = n % len(lst)
        return lst[n:] + lst[:n]
    elif direction == 'right':
        n = n % len(lst)
        return lst[-n:] + lst[:-n]

#handling invalid direction
    
    else:
        raise ValueError("Direction must be 'left' or 'right'") 
input_list = [1, 2, 3, 4, 5]

#user inputs

n = int(input("Enter the number of positions to rotate: "))    
direction = input("Enter the direction to rotate ('left' or 'right'): ")    

rotated_list = rotate(input_list, n, direction)

print("Original list:", input_list)
print("Rotated list:", rotated_list)    