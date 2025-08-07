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

@pytest.fixture
def product_fixture_2():
    return Product(
        name="доска",
        description="новый",
        price=1.0,
        quantity=20
    )

@pytest.fixture
def product_fixture_3():
    return Product(
        name="кирпич",
        description="новый",
        price=0,
        quantity=0
    )


def test_product_init(product_fixture):
    assert product_fixture.name == "кирпич"
    assert product_fixture.description == "новый"
    assert product_fixture.price == 1.5
    assert product_fixture.quantity == 10

    product_fixture.price = -100
    assert product_fixture.price == None

    product_var = product_fixture.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert product_var.name == "Samsung Galaxy S23 Ultra"
    assert str(product_fixture) == "кирпич, None руб, Остаток: 10 шт."


def test_product_price_sum(product_fixture, product_fixture_2):
    result = product_fixture + product_fixture_2
    assert result == 35

def test_product_no_price():
    with pytest.raises(ValueError):
        Product(
            name="кирпич",
            description="новый",
            price=0,
            quantity=0
        )

