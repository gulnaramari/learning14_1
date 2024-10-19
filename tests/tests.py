import pytest
from src.main import Product, Category
from tests.conftest import smartphone, category


def test_product(smartphone):  # тест на инициализацию
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5


def test_category(category): # тест на инициализацию
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации,"
                                    " но и получения дополнительных функций для удобства жизни")
    assert category.products == 1

