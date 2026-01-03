#Class - bluprint/template to create objects
#Objects - instance of classes

#? Class creation
class Student:
    subject = "python"
    college = "abc"
    year = "2nd year"

#? Object creation
s1 = Student()
s2 = Student()

print(s1.subject, s1.college, s1.year)
print(s2.subject, s2.college, s2.year)