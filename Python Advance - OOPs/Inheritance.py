#Inheritance = Allows a class to inherit attributes and methods from another class
#              helps with code reusablity and extensility
#              class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
mouse.sleep()
cat.speak()
