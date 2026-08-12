"""
Exercise: Prime Number Generator

Difficulty: Intermediate

Description:
Generate a list of prime numbers up to a given limit by checking divisibility.

Concepts:
- Loops
- Nested Loops
- Conditional Logic
- Number Theory
- Algorithm Design
"""

#checking prime numbers

limit = int(input("Enter limit :"))
prime_numb = []
for l in range(2, limit + 1) :
    is_prime = True
    for d in range(2, l) : 
        if l % d == 0 :
            is_prime = False
            break
        
#storing prime numbers
#     
    if is_prime == True :
        prime_numb.append(l)
print(prime_numb)
