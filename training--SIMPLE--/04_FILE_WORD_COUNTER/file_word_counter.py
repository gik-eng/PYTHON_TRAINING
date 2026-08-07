"""
Exercise: File Word Counter

Difficulty: Simple

Description:
Read a text file and count the total number of words it contains.

Concepts:
- File Handling
- open()
- read()
- split()
- Loops
- Counting
"""

#reading file

file = open("note_2.txt", "r")
text = file.read().split()
count = 0

#counting total character in the file 

for ch in text :
    count +=1
print(count)    
file.close()