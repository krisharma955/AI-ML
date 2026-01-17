#Inheritance

#! Reusing attr & methods from Parent (Base) class - increases code reusability
#! Protected attri & methods are accessible to the class and its subclasses

class Employee:
    start_time = "10AM"
    end_time = "4PM"

    def change_end_time(self, new_end_time):
        self.end_time = new_end_time

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role) #? super keyword - to call the constructor of parent class
        self.salary = salary

class Professor(Employee):
    def __init__(self, subject):
        self.subject = subject


#? Single Level Inheritance -> (1P - 1C)
#* ex- Employee -> Professor - Professor will inherit the properties of Employee class
p1 = Professor("Maths")
p1.change_end_time("6PM")
print(p1.subject, p1.start_time, p1.end_time)

#? Multi Level Inheritance -> (1P - 1M - 1C)
#* ex- Employee -> AdminStaff -> Accountant - Accountant will inherit the properties of both the classes Employee & AdminStaff
a1 = Accountant(10_000, "CA")
print(a1.role, a1.salary, a1.start_time, a1.end_time)

#? Multi Level Inheritance -> a class inherits multiple classes
#* ex- TA -> Teacher + Student - TA will inherit the properties of both Teacher & Student

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(20_000, 8.7, "Gasly")
print(ta1.name, ta1.salary, ta1.gpa)
