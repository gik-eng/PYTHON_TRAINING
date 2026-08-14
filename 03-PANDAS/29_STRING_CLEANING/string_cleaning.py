"""
Exercise 29 — String Cleaning

This exercise focuses on cleaning and standardizing
text data in a Pandas DataFrame.

Topics:
- str.strip()
- str.lower()
- str.upper()
- str.replace()
- Chaining string operations
- Creating cleaned text columns
"""

import pandas as pd


students = {
    "name": [
        " Ali ",
        "SARA",
        " Reza",
        "mina ",
        " NIMA ",
        "zahra"
    ],

    "city": [
        " Tehran ",
        "shiraz",
        " TABRIZ ",
        "tehran",
        "Mashhad ",
        " TEHRAN"
    ]
}


df = pd.DataFrame(students)


print(df)

df["name"] = df["name"].str.strip()
df["name"] = df["name"].str.lower()



df["city"] = df["city"].str.upper()
df["city"] = df["city"].str.strip()

df["city"] = df["city"].str.replace(
    "TEHRAN",
    "TEH"
)
print(df)


df["clean_name"] = (
    df["name"]
    .str.strip()
    .str.lower()
)

df["clean_city"] = (
    df["city"]
    .str.strip()
    .str.upper()
)

print(df)