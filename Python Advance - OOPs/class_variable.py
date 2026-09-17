# class variables = Shared among all instances of a class
#                   Define outside the constructor 
#                   Allow you to share data among objects created fromt the class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Ibrahmovic", 43)
student3 = Student("Mario", 34)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
     