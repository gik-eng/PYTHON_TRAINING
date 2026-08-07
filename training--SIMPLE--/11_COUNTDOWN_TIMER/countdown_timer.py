"""
Exercise: Countdown Timer

Difficulty: Simple

Description:
Create a countdown timer that counts down from a given number and displays each second until reaching zero.

Concepts:
- While Loops
- Time Module
- time.sleep()
- User Input
"""

import time

#count down timer

limit = int(input("Enter limit :"))
while limit > 0 :
    print(limit)
    time.sleep(1)
    limit -= 1

print("Blast off!")
