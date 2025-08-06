from src.category import Category
from src.product import Product

import pytest


@pytest.fixture
def caregory_1_fixture():
    return Category(
        name="стройматериалы",
        description="для строительства дома",
        products=[
            Product("кирпич", "новый", 11.5, 10),
            Product("доска", "сосновая", 10.5, 20),
            Product("цемент", "сотой марки", 12.0, 5)
        ],
    )


@pytest.fixture
def caregory_2_fixture():
    return Category(
        name="продукт питания",
        description="для обеда строителей",
        products=[
            Product("молоко", "коровье", 2.1, 5),
            Product("хлеб", "белый", 1.5, 3),
            Product("колбаса", "копченая", 3, 1)
        ],
    )


@pytest.fixture
def caregory_3_fixture():
    return Category(
        name="продукт питания",
        description="для обеда строителей"
    )


def test_category_init(caregory_1_fixture, caregory_2_fixture):
    assert caregory_1_fixture.name == "стройматериалы"
    assert caregory_2_fixture.description == "для обеда строителей"
    assert len(caregory_1_fixture.products) == 100
    assert caregory_1_fixture.category_count == 2
    assert caregory_2_fixture.product_count == 6
    assert str(caregory_1_fixture) == "стройматериалы, количество продуктов: 35 шт."


def test_category_products(caregory_1_fixture):
    caregory_1_fixture.products == 'кирпич, 11.5 руб. Остаток: 10 шт.\n'


def test_category_middle_price(caregory_3_fixture):
    assert caregory_3_fixture.middle_price() == 0

