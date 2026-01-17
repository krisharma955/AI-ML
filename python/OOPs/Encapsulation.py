#Encapsulation
#! Wrapping data & fxns into a single unit
#! Data hiding

class BankAccount:
    def __init__(self, name, balance, accNo):
        self.name = name
        self._accNo = accNo #? protected using (_) - can't be enforced (just a convention)
        self.__balance = balance #? private using (__) - leads to data mangling (little bit of enforcement)

    #? Getters & Setters
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, newBalance):
        self.__balance = newBalance
        

b1 = BankAccount("Lando", 10_000, 4)

print(b1.name) #* Lando
print(b1._accNo) #* 4
# print(b1.__balance) #* not accessible - (AttributeError: 'BankAccount' object has no attribute '__balance')
print(b1._BankAccount__balance) #* private can be accessed this way

print(b1.get_balance())
b1.set_balance(20_000)
print(b1.get_balance())