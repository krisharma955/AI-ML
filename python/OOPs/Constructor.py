#Constructor - fxn used to create objects
#! __init__ method (Constructor) -> to initialize a object

class Student:
    #* Default constructor
    def __init__(self):
        print("default constructor")

    #* Parameterized constructor
    def __init__(self, name, cgpa): #? self parameter -> stores the current instance of the class (ref of the current object)
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Lando", 8.9)
stu2 = Student("Lewis", 9.0)

print(stu1.name, stu1.cgpa)
print(stu2.name, stu2.cgpa)

print(stu2.get_cgpa())

#? Python doesn't allow multiple constructors in a single class (final constructor will be taken)