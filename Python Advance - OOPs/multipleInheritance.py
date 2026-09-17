#multiple inheritence = inherit from more than one parent class
#                       C(A, B)
# multilevel inheritence = inherit from a parent which inherits from another parent 
                        #    C(B) <- B(A) <- A
class Animal :
    def __init__(self, name):
        self.name = name   #constructor only inherit from parent in multilevel inheritance
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal) : 
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Tony")
hawk = Hawk("Robb")
fish = Fish("Dunk")

# fish.flee()
# fish.hunt()

rabbit.flee()
hawk.sleep()  #hawk -> predator -> Animal -> sleep() "Multi level inheritance"

