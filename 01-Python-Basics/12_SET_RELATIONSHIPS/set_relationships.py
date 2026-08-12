"""
Exercise: Set Relationships

Difficulty: Simple

Description:
Determine whether one set is a subset, superset, or disjoint from another set.

Concepts:
- Sets
- Set Methods
- Conditional Statements
- Collection Relationships
"""

list_a = [1,2,3]
list_b = [1,2,3,4,5]

#Into sets

set_a = set(list_a)
set_b = set(list_b)



#checking subset, superset and disjoint

if set_a.issubset(set_b) :
    print("list_a is a subset of list_b")
else : 
    print("list_a is not a subset of list_b")

if set_b.issuperset(set_a) :
    print("list_b is a superset of list_a")
else : 
    print("list_b is not a superset of list_a")

if set_a.isdisjoint(set_b) :
    print("list_a and list_b are disjoint sets")
else :
    print("list_a and list_b are not disjoint sets")
