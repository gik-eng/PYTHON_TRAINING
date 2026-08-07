"""
Exercise: Dictionary Merge with Summed Values

Difficulty: Simple

Description:
Merge two dictionaries by adding the values of duplicate keys while keeping unique keys unchanged.

Concepts:
- Dictionaries
- Dictionary Methods
- get()
- Loops
- Data Merging
"""

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
result = {}

#copy first dictionary

result.update(dict_a)


#merge second dictionary

for i in dict_b :
    result[i] = result.get(i, 0) + dict_b[i]
print(result)    