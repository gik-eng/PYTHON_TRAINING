"""
Exercise: Anagram Checker

Difficulty: Simple

Description:
Determine whether two strings are anagrams by comparing their sorted characters.

Concepts:
- Strings
- String Methods
- Sorting
- Functions
- Conditional Statements
"""

#without function
char1 = input("Enter character 1 :").lower().replace(" ", "")
char2 = input("Enter character 2 :").lower().replace(" ", "")
filt_char1 = sorted(char1)
filt_char2 = sorted(char2)
if filt_char1 == filt_char2 :
    print(f"{char1} is an anagram of {char2}")
else:     
    print(f"{char1} is not an anagram of {char2}")

##with function
def is_anagram(char1, char2) :
    f_char1 = sorted(char1)
    f_char2 = sorted(char2)
    if f_char1 == f_char2 :
        print((f"{char1} is an anagram of {char2}"))
    else :
        print(f"{char1} is not an anagram of {char2}")

char1 = input("Enter your character :").lower().replace(" ", "")
char2 = input("Enter your character :").lower().replace(" ", "")
is_anagram(char1, char2)

