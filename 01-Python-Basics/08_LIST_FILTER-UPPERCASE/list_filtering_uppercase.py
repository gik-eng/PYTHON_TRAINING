"""
Exercise: List Filtering and Uppercase Conversion

Difficulty: Simple

Description:
Filter words by length and convert the remaining words to uppercase.

Concepts:
- Lists
- Loops
- Conditional Statements
- String Methods
- Filtering
"""

words = ["apple", "bat", "cherry", "dog", "elderberry"]
filterised = []

#filtering words with length >= 4

for word in words :
    if len(word) >= 4 :

#convert to uppercase

        filterised.append(word.upper())

    else :
        continue
print(filterised)    



