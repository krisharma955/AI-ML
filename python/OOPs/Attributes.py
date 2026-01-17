#Attributes

#! Class Attributes -> belongs to the class (common for all the objects)
#! Instance Attributes -> belongs to a object (unique)

class Student:
    college_name = "ABC" #* Class attribute
    pi = 3.1

    def __init__(self, name, gpa): #* name, gpa - instance attributes
        self.name = name
        self.gpa = gpa
        self.pi = 3.14

s1 = Student("Lando", 9.0)
print(Student.college_name) #* because college_name is a class attribute - can be accessed using class name
print(s1.college_name)
print(s1.name) #* instance att requires object - can't be accesssed by class name
print(s1.gpa)
print(s1.pi) #* priority => instance att > class att

#? priority => instance att > class att