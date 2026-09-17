#Polymorphism = Greek word that means "have many forms or faces"
                # Poly = Many
#               Morphe = Form

# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1.Inheritance = An object could be treated of the same type as a parent class
# "Duck typing" = Object must have neccessary attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping


Shapes = [Circle(7), Triangle(4, 9),Pizza(8,"pepperoni")]

for shape in Shapes:
    print(f"{shape.area()}cm²")
    

    