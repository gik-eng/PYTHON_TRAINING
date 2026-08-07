"""
Exercise: File Read & Write

Difficulty: Simple

Description:
Write text to a file and read it back to display its contents.

Concepts:
- File Handling
- open()
- write()
- read()
- close()
"""
##writing
file = open("note.txt", "w")
file.write("Hello, this is my first note.\n")
file.write("Python file handling is simple.\n")
file.write("End of file.\n")
file.close()

##reading
file = open("note.txt", "r")
content = file.read()
print(content)
file.close()