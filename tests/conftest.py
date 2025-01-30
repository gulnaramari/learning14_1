import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера", 180000.0, 5)



@pytest.fixture
def first_product():
    return Product(
        name="Butter",
        description="Description of the product",
        price=84.50,
        quantity=10,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Milk",
        description="Description of the product",
        price=155.87,
        quantity=34,
    )

@pytest.fixture
def first_category():
    return Category(
        name="Category",
        description="Description of the category",
        products=[
            Product(
                name="Butter",
                description="Description of the product",
                price=200.50,
                quantity=20,
            ),
            Product(
                name="Milk",
                description="Description of the product",
                price=120.8,
                quantity=100,
            ),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Category number two",
        description="Description of the category number two",
        products=[
            Product(
                name="Pizza",
                description="Description of the product",
                price=450.50,
                quantity=20,
            ),
            Product(
                name="Cheese",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
            Product(
                name="Pasta",
                description="Description of the product three",
                price=467.56,
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
