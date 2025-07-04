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

