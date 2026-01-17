#Abstraction

#! Hidding internal details & showing only essential features
#! Abstract classes - blueprint for other classes

from abc import ABC, abstractmethod #? module used for abstraction

class Animal(ABC):
    @abstractmethod
    def make_sound(self): #? abstract method - no implementation
        pass #* kind of null value

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

lion = Lion()
lion.make_sound()

cat = Cat()
cat.make_sound()
