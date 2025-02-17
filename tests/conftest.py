import pytest

from src.cat_iter import CategoryIterator
from src.category import Category
from src.new_class import LawnGrass, Smartphone
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


@pytest.fixture
def new_price():
    return -100


@pytest.fixture
def cat_iterator(first_category):
    return CategoryIterator(first_category)


@pytest.fixture
def cat_iterator_second(second_category):
    return CategoryIterator(second_category)


@pytest.fixture
def product_new():
    product_new = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    return product_new


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона",
                     500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава",
                     450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
        180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space",
                      210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_empty_quantity():
    return Product(name="Samsung", description="256GB, Серый цвет,"
                                               " 200MP камера",
                   price=180000.0, quantity=1)


@pytest.fixture
def price_median():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни",
        products=[
            Product("Samsung", "256GB, Серый цвет, 200MP камера", 2, 1),
            Product("Iphone 15", "512GB, Gray space", 4, 1),
        ],
    )
