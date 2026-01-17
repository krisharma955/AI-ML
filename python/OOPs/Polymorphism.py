#Polymorphism

#! Function Overriding (used in Inheritance)
#* redifing parent class's fxn in the child class

class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")

t1 = Teacher()
t1.get_designation() #? fxn inside teacher gets called and the fxn overrides the one on the parent class

#! Duck Typing
#* Concept - Similar types of fxns in diff classes 
