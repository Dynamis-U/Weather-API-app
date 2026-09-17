# Static Method = A method that belong to a class rather than any object from the class (instance)
# Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Luffy", "Manager")
employee2 = Employee("Sanji", "Cook")
employee3 = Employee("Nami", "Cashier")

print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())