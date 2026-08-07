"""
Exercise: Title Case Converter

Difficulty: Simple

Description:
Capitalize the first letter of each word in a sentence without using the built-in title() method.

Concepts:
- Strings
- String Methods
- split()
- join()
- Lists
- Loops
"""

#splitting sentence

text = input("Enter a sentence: ")
words = text.split()

new_words = []
for word in words :


#capitalizing each word

    new_words.append(word.capitalize())

#joining sentence
    
cap_text = " ".join(new_words)    
print(cap_text)