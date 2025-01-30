from src.product import Product


def test_product(first_product, second_product):
    assert first_product.name == "Butter"
    assert first_product.description == "Description of the product"
    assert first_product.price == 200.50
    assert first_product.quantity == 20

    assert second_product.name == "Milk"
    assert second_product.description == "Description of the product"
    assert second_product.price == 120.8
    assert second_product.quantity == 100


def test_add_new_product(product_add):
    product4 = Product.new_product(product_add)
    assert product4.name == "Chocolate"
    assert product4.description == "White chocolate"
    assert product4.price == 200.5
    assert product4.quantity == 33


def test_price_setter(capsys, first_product):
    first_product.price = -600.9
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    first_product.price = 600.9
    assert first_product.price == 600.9
