from src.product import Product
import pytest


@pytest.fixture
def product_fixture():
    return Product(
        name="кирпич",
        description="новый",
        price=1.5,
        quantity=10
    )


def test_product_init(product_fixture):
    assert product_fixture.name == "кирпич"
    assert product_fixture.description == "новый"
    assert product_fixture.price == 1.5
    assert product_fixture.quantity == 10
    product_fixture.price = -100
    assert product_fixture.price == "Цена не должна быть нулевая или отрицательная"
    product_var = product_fixture.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert product_var.name == "Samsung Galaxy S23 Ultra"




