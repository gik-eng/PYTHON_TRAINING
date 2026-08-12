"""
Exercise: Binary Search

Difficulty: Intermediate

Description:
Search for a target value in a sorted list using the Binary Search algorithm.
The algorithm repeatedly divides the search range in half to find the target efficiently.

Concepts:
- Functions
- Lists
- Divide and Conquer
- Loops
- Conditional Logic
- Algorithm Design
- Time Complexity Optimization
"""

def binary_search(numbers, target) :
    left = 0 
    right = len(numbers) - 1
    while left <= right :
        mid = (left + right) // 2

        if numbers[mid] == target :
            return mid
        

        elif numbers[mid] < target :
            left = mid + 1

        else :
            right = mid - 1

    return -1

numbers = [1, 3, 5, 7, 9, 11, 13]
print(numbers)
target = int(input("Enter your target :"))

result = binary_search(numbers, target)

if result != -1 :
    print(f"Target found at {result}")
else : 
    print("Target not found")    
