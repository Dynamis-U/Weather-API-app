# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):   # Constructor to create an object
           self.model = model
           self.year = year
           self.color = color
           self.for_sale = for_sale

    def drive(self):
          print(f"You drive the {self.model}")

    def stop(self):
          print(f"You stop the {self.model}")

    def describe(self):
          print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mustang", 2024, "red", False )
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2025, "yellow", True)

print(car1)  # Gives the memory address of the given object 

print(car1.model)
print(car2.color)
print(car3.model)

car2.drive()
car3.stop()
car1.describe()


        