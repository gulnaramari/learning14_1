import pytest
from src.main import Product, Category


@pytest.fixture
def smartphone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category():
    return Category("Смартфоны",
                    ("Смартфоны, как средство не только коммуникации,"
                                    " но и получения дополнительных функций для удобства жизни"),
                    1)

