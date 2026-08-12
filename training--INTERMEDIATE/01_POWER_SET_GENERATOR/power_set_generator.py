"""
Exercise: Power Set Generator

Difficulty: Intermediate

Description:
Generate the power set of a list by creating all possible combinations of its elements.

Concepts:
- Lists
- Loops
- itertools
- combinations()
- Combinatorics
"""

from itertools  import combinations

#Generating all possible combinations

#storing all combinations

our_list = [1,2,3]
result = []

#creating combinations with different lengths

for n in range(1, len(our_list) + 1):
    result.extend(list(combinations(our_list, n)))

print(result)
