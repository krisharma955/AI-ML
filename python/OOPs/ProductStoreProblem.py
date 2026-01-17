#Example - Product Store

class Store:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Store.count += 1 #* count is a class attribute

    def get_Product_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

    @classmethod
    def get_total_Products(cls):
        print(f"Total number of products: {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"Discounted Price: {price - (price * discount/100)}")

p1 = Store("Laptop", 40_000)
p1.get_Product_info()

p2 = Store("Phone", 10_000)
p2.get_Product_info()

p1.calc_discount(p1.price, 12)

Store.get_total_Products()
print(Store.count)