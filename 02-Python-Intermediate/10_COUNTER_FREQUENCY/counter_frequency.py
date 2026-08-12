"""
Exercise: Counter Word Frequency

Difficulty: Intermediate

Description:
Count the frequency of each word in a sentence using Python's collections.Counter.
This exercise demonstrates how to replace manual counting logic with a specialized
tool from Python's Standard Library.

Concepts:
- Functions
- Strings
- split()
- collections.Counter
- Standard Library
- Word Frequency Analysis
"""

from collections import Counter
def words_frequency(words) :
    # Count the frequency of each word
    return Counter(words)



text = "python java python c++ python java"

# Split the text into individual words
words = text.split()

result = words_frequency(words)
print(result)