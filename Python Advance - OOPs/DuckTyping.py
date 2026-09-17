# "Duck typing " = Another way to achieve polymorphism besides
#                  Object must have the minimum necessary attributes/ methods
#                 " If it look like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False     # Duck typing

    def speak(self):   #Duck typing
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)