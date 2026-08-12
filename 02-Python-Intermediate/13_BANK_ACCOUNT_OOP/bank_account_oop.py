"""
Exercise: Bank Account System

Difficulty: Intermediate

Description:
Create a simple bank account system using Object-Oriented Programming.
The system allows users to create accounts, deposit money, withdraw money,
and check their current balance.

Concepts:
- Object-Oriented Programming (OOP)
- Classes
- Objects
- Constructors
- Instance Attributes
- Instance Methods
- Encapsulation
- Conditional Logic
"""

class BankAccount :
    
    def __init__(self, owner, balance) :

        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount) :
        self.balance += amount
        return self.balance

    def withdraw(self, amount) :
        if amount <= self.balance :
            self.balance -= amount
            return self.balance
        else : 
            return "Insufficient funds"

    def check_balance(self) :
        return self.balance    


account = BankAccount("Ali", 1000)

print(account.deposit(500))

print(account.withdraw(300))

print(account.check_balance())   