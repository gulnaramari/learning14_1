from src.product import Product


def test_product_init1(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_init2(first_product, second_product):
    assert first_product.name == "Product"
    assert first_product.description == "Description of the product"
    assert first_product.price == 84.50
    assert first_product.quantity == 10
    assert second_product.name == "Product two"
    assert second_product.description == "Description of the product two"
    assert second_product.price == 155.87
    assert second_product.quantity == 34


def test_add_new_product(product_add):
    product5 = Product.new_product(product_add)
    assert product5.name == "Chocolate"
    assert product5.description == "White chocolate"
    assert product5.price == 200.5
    assert product5.quantity == 33


def test_price_setter(capsys, first_product):
    first_product.price = -84.50
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна" \
                                                  " быть" " нулевая" \
                                                  " или отрицательная"
    first_product.price = 84.50
    assert first_product.price == 84.50


def test_price_update(capsys, first_product):
    first_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна" \
                                                  " быть" " нулевая" \
                                                  " или отрицательная"


def test_product_str(first_product):
    assert str(first_product) == "Product, 84.5 руб. Остаток: 10 шт."


def test_product_add(first_product, second_product):
    assert first_product + second_product == 6144.58


def test_new_product(product_new, first_product):
    test = Product.new_product(product_new)
    assert test.name == "Samsung Galaxy S23 Ultra"
    assert test.description == "256GB, Серый цвет, 200MP камера"
    assert test.price == 180000
    assert test.quantity == 5
