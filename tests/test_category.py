import pytest


def test_category_init_correct(first_category, second_category):
    assert first_category.name == "Category1"
    assert first_category.description == "Description of the category1"
    assert second_category.name == "Category2"

    assert len(first_category.products_in_list) == 2
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_wrong(second_category):
    with pytest.raises(AssertionError):
        assert second_category.name == "Смартфоны"


def test_products_getter(first_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.products == "Product, 84.5 руб."
        " Остаток: 10 шт.\n"
        "Product two, 155.87 руб."
        " Остаток: 34 шт.\n"
    )


def test_category_str(first_category):
    assert str(first_category) == "Category1, количество продуктов: 44 шт."


def test_category_iterator(cat_iterator):
    iter(cat_iterator)
    assert cat_iterator.index == 0
    assert next(cat_iterator).name == "Product"
    assert next(cat_iterator).name == "Product two"


def cat_iterator_second(cat_iterator):
    with pytest.raises(StopIteration):
        next(cat_iterator)


def test_price_middle(price_median, product_empty_quantity):
    assert price_median.price_middle() == 3
