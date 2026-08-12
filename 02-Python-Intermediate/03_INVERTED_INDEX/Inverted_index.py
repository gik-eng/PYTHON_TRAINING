"""
Exercise: Inverted Index

Difficulty: Intermediate

Description:
Create an inverted index by mapping each book to its corresponding author.

Concepts:
- Dictionaries
- Nested Data Structures
- Loops
- Dictionary Methods
- Data Mapping
"""

authors = {
    "George Orwell": ["1984", "Animal Farm"],
    "J.K. Rowling": ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]
}

#creating inverted index

results = {}
for author, books in authors.items():
    for book in books :
#assigning each book to its author
#         
        results[book] = author

        
print(results)

        