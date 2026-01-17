#Methods - Instance, class & static methods

#! Instance Methods - first param -> always (self), can access class aswell as instance attributes

#! Class Methods - first param -> cls, can access only class attributes, uses decorator (@classmethod)

#! Static Methods - no compulsory param, no self or cls, can't access instance & class attributes, uses decorator (@staticmethod)

class Laptop:
    storage_type = "SSD" #* class attribute

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod #* decorator
    def get_Storage_type(cls): #? Class Method
        print("Storage type:", cls.storage_type)

    def laptopInfo(self): #? Instance Method
        print("Storage type:", self.storage_type)
        print("ram:", self.ram)
        print("storage:", self.storage)

    @staticmethod #* decorator
    def calc_price(price, discount): #? Static Method
        price = price - discount
        print(f"Final Price: {price}")

l1 = Laptop("16gb", "256")
l1.laptopInfo()

l2 = Laptop("8gb", "512")
l2.laptopInfo()

Laptop.get_Storage_type() #* class method called (using class name)
l1.get_Storage_type() #* class methods can be called using objects aswell (priority)

l1.calc_price(1000, 100)
