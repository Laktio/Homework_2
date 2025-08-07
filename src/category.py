from src.product import Product


class Category:
    name:str
    description:str
    products:list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        product_list = self.__products
        product_quantity = []
        for product in product_list:
            product_dict = product.__dict__
            product_quantity.append(product_dict['quantity'])

        return f'{self.name}, количество продуктов: {sum(product_quantity)} шт.'

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

