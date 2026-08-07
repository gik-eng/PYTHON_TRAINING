"""
Exercise: Character Frequency Counter

Difficulty: Simple

Description:
Count the frequency of each character in a string while ignoring spaces and letter case.

Concepts:
- Strings
- String Methods
- Dictionaries
- Loops
- Character Counting
"""

#removing spaces and converting to lowercase

text = input("Enter your input :")
filterised = text.lower().replace(" ", "")
count = {}


#counting characters

for word in filterised :
    if word in count :
        count[word] += 1
    else :
        count[word] = 1
print(count)        