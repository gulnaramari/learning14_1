import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def first_product():
    return Product(
        name="Product",
        description="Description of the product",
        price=84.50,
        quantity=10,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Product two",
        description="Description of the product two",
        price=155.87,
        quantity=34,
    )


@pytest.fixture
def first_category():
    return Category(
        name="Category1",
        description="Description of the category1",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product two",
                description="Description of the product two",
                price=155.87,
                quantity=34,
            ),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Category2",
        description="Description of the category2",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product two",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
            Product(
                name="Product three",
                description="Description of the product three",
                price=8467.56,
                quantity=32,
            ),
        ],
    )


@pytest.fixture
def product_add():
    return {
        "name": "Chocolate",
        "description": "White chocolate",
        "price": 200.5,
        "quantity": 33,
    }
