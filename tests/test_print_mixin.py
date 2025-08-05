from src.product import Product
from src.category import Category
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    print (message)