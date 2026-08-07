"""
Exercise: Word Frequency Counter

Difficulty: Simple

Description:
Count how many times each word appears in a given sentence.

Concepts:
- Strings
- split()
- Dictionaries
- Loops
- Conditional Statements
"""

text = "apple banana apple cherry banana apple"
words = text.split()
word_count = {}

#counting each word in the list

for word in words:
    if word in word_count :
        word_count[word] += 1
    else :
        word_count[word] = 1

print(word_count)
