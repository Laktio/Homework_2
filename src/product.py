from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.full_price = price*quantity
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.price} руб, Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is Product:
            return self.full_price + other.full_price
        else:
            raise TypeError

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
        self.__price = price if price > 0 else print("Цена не должна быть нулевая или отрицательная")

