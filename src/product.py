class Product:
    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, product):
        name = product['name']
        description = product['description']
        price = product['price']
        quantity = product['quantity']
        return cls(name, description, price, quantity)

    @price.setter
    def price(self, price):
        self.__price = price if price > 0 else "Цена не должна быть нулевая или отрицательная"

