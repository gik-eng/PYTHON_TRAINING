"""
Exercise: Car Class

Difficulty: Intermediate

Description:
Create a class representing a car with attributes and a method to display its engine status.

Concepts:
- Object-Oriented Programming
- Classes
- Objects
- __init__()
- Methods
- Attributes
"""

#Car blueprint

class Car:
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")  

#creating objects
          
car1 = Car("Toyota", 2022, "Camry")
car2 = Car("Ford", 2018, "Mustang")
car1.start_engine()
car2.start_engine()
