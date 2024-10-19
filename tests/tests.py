import pytest


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init_correct(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации,"
                                    " но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3
    assert second_category.name == "Телевизоры"
    assert len(second_category.products) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_wrong(second_category): # тест на корректность
    with pytest.raises(AssertionError):
        assert second_category.name == "Смартфоны"
