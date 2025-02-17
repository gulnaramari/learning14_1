import pytest

from src.product import Product
from src.category import Category


def test_category_init_correct(first_category, second_category):
    assert first_category.name == "Category1"
    assert first_category.description == "Description of the category1"
    assert second_category.name == "Category2"

    assert len(first_category.products_in_list) == 2
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_wrong(first_category):
    with pytest.raises(AssertionError):
        assert first_category.name == "Лекарства"


def test_category_wrong_(second_category):
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


def test_add_product():
    category_test = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,"
                    " но и получение дополнительных функций"
                    " для удобства жизни",
        products=[],
    )
    product_test = Product(name="Nokia",
                           description="212GB, blue цвет, 150MP камера",
                           price=55000.0, quantity=1)

    category_test.add_product(product_test)

    assert category_test.product_count == 11


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


def test_price_middle(price_median, no_price):
    assert price_median.price_middle() == 3
    assert no_price.price_middle() == 0


def test_custom_exception(capsys, second_category):
    assert len(second_category.products_in_list) == 3

    product_add = Product(name="Product",
                          description="Description of the product",
                          price=84.50, quantity=0)
    second_category.__products = product_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Product(Product," \
                                                  " Description" \
                                                  " of the product, 84.5, 0)"
