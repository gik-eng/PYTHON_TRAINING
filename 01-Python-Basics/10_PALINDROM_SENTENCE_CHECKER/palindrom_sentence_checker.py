"""
Exercise: Palindrome Sentence Checker

Difficulty: Simple

Description:
Check whether a sentence is a palindrome by ignoring spaces, punctuation, and letter case.

Concepts:
- Strings
- String Methods
- Lists
- Loops
- Slicing
- Data Cleaning
"""

#removing spaces and punctuation

text = input("sey sth :").lower()
temp = []

#reversing cleaned sentence

for char in text :
    if char.isalnum() :
        temp.append(char)

#checking palindrome

rev_temp = temp[::-1]
if temp == rev_temp :
    print(True)
else :
    print(False)
