#Assignment

from abc import ABC, abstractmethod

#! Q1
class BankAccount:
    def __init__(self, accNo, name, balance):
        self.accNo = accNo
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        if(amt > 0):
            self.balance += amt
        else:
            print("Amount to be deposited should to be greater than ZERO")
        
    def withdraw(self, amt):
        if(amt <= self.balance):
            self.balance -= amt
        else:
            print("Not Enough Balance")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

b1 = BankAccount(1, "Oscar", 2000)
b1.deposit(500)
b1.withdraw(100)
b1.check_balance()
b1.withdraw(5000)

#! Q2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    
    def add_new_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        print(len(self.reviews))

    def display_reviews(self):
        for review in self.reviews:
            print(review)

b1 = Book("Harry Potter", "JK Rowling")
b1.add_new_review("Brilliant series")
b1.add_new_review("Fantastic")
b1.display_reviews()
b1.count_reviews()

#! Q3
class Student:
    def __init__(self, name, rollNo, marks):
        self.__name = name
        self.__rollNo = rollNo
        self.__marks = marks

    #? Getters & Setters
    def get_name(self):
        print(self.__name)

    def set_name(self, new_name):
        self.__name = new_name

    def get_rollNo(self):
        print(self.__rollNo)

    def set_rollNo(self, new_rollNo):
        self.__rollNo = new_rollNo

    def get_marks(self):
        print(self.__marks)

    def set_marks(self, new_marks):
        self.__marks = new_marks

    def student_info(self):
        print(f"Name: {self.__name}")
        print(f"Roll.No: {self.__rollNo}")
        print(f"Marks: {self.__marks}")

s1 = Student("Lando", 4, 90)
s1.get_name()
s1.get_rollNo()
s1.get_marks()

s1.set_name("Lewis")
s1.set_rollNo(44)
s1.set_marks(100)

s1.student_info()

#! Q4
class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad
    def calc_area(self):
        print(3.14 * self.rad * self.rad)

class Rectangle(Shape):
    def calc_area(self, length, breadth):
        print(length * breadth)

class Triangle(Shape):
    def calc_area(self, base, height):
        print(0.5 * base * height)

circle = Circle(1)
circle.calc_area()

rec = Rectangle()
rec.calc_area(2, 3)

tri = Triangle()
tri.calc_area(2, 2)

#! Q5
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def bike_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Engine_CC: {self.engine_cc}")

car = Car("Mercedes", "AMG", 2)
car.car_info()

bike = Bike("Kawasaki", "Ninja", 200)
bike.bike_info()

#! Q6
class Employee(ABC):
    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calc_salary(self):
        pass

class Intern(Employee):
    def calc_salary(self):
        print(f"Intern Salary: {self.salary - 500}")

class FullTimeEmployee(Employee):
    def calc_salary(self):
        print(f"FullTime Employee Salary: {self.salary}")

class ContractEmployee(Employee):
    def calc_salary(self):
        print(f"Contract Employee Salary: {self.salary - 400}")

i = Intern(1000)
i.calc_salary()

f = FullTimeEmployee(1000)
f.calc_salary()

c = ContractEmployee(1000)
c.calc_salary()

#! Q7
class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        if self.age is not None:
            print(f"Age: {self.age}")
        if self.address is not None:
            print(f"Address: {self.address}")

p1 = Person("Lando")
p1.display()

p2 = Person("Lando", 25)
p2.display()

p3 = Person("Lando", 25, "Monaco")
p3.display()

#! Q8
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def player_info(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")

    def total_players():
        print(Player.player_count)

p1 = Player("Charles", "A+")
p1.player_info()

p2 = Player("Isack", "A")
p2.player_info()

Player.total_players()

#! Q9
class Herbivore:
    food = "veg"

    def food_type_herb(self):
        print(Herbivore.food)

class Carnivore:
    food = "non-veg"

    def food_type_carn(self):
        print(Carnivore.food)

class Omnivore:
    food = "veg + non-veg"

    def food_type_omni(self):
        print(Omnivore.food)

class Bear(Herbivore, Carnivore, Omnivore):
    def food_types(self):
        self.food_type_herb()
        self.food_type_carn()
        self.food_type_omni()

bear = Bear()
bear.food_types()