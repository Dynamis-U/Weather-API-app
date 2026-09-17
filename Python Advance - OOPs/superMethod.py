#super() = Function used in a child class to call methods from a parent class (superclass).
#          Allows you to extend the functionality of the inherited methods also called method overidding
#          method overriding done in describe()

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius



    def describe(self):
        print(f"Its is a circle with an area of {3.14 * self.radius * self.radius :.3f}")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a Square with an area of {self.width * self.width}cm^2")
        super().describe()

Circle(color = "red", is_filled = True, radius = 6).describe()

# class A :
#   pass
# class B(A) :
#   pass
# class C(A) :
#   pass
# class D(B, C) :
#   pass

# This is where super() is exactly helpful so here D inherited from multiple classes B and C for it executed in order using super() but
# cant helpful if youre going to use direct parent class name instead of super() method 
# so super() method exceuted from left to right in parent class parameter passing
        