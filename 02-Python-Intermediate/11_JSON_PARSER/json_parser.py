"""
Exercise: JSON Parser

Difficulty: Intermediate

Description:
Parse JSON data and extract specific information from nested structures.
This exercise demonstrates how to convert JSON strings into Python objects
and filter data based on specific conditions.

Concepts:
- Functions
- JSON Parsing
- json.loads()
- Lists
- Dictionaries
- Nested Data Structures
- Data Filtering
"""

import json

def get_active_users(users_json) :

# Convert JSON string into Python objects
    data = json.loads(users_json)

 # Extract names of active users
    active_users = []
    for user in data :
        if user["active"] :
            active_users.append(user["name"])
    return active_users


users_json = """
[
    {
        "id": 1,
        "name": "Ali",
        "active": true
    },
    {
        "id": 2,
        "name": "Sara",
        "active": false
    },
    {
        "id": 3,
        "name": "Reza",
        "active": true
    }
]
"""

result = get_active_users(users_json)
print(result)
