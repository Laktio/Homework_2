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
        return f'{self.name}, количество продуктов: {Category.product_count} шт.'

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str

    def add_product(self, product: Product):
        self.__products.append(product) if isinstance(product, Product) else print ("Не является атрибутом класса Product")
        Category.product_count += 1

