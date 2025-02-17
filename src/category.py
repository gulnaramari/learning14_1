from typing import Any

from src.my_exception import ZeroProduct
from src.product import Product


class Category:
    """Класс категории"""

    name: str  # название продукта
    description: str  # описание продукта
    products: list  # список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        products_quantity = 0
        for product in self.__products:
            products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {products_quantity} шт."

    def add_product(self, product: Product) -> Any:
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProduct("Нельзя добавлять товар"
                                      " с нулевым количеством")
            except ZeroProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products

    def price_middle(self):
        try:
            return sum([product.price for product
                        in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
        finally:
            print("Средняя цена товаров категории получена")


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения"
        " дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))
    print(category1)

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(str(category1))

    print(category1.product_count)
    print(Category.category_count)

    product5 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    print(product5.name)
    category1.add_product(product5)
    print(str(category1))

    print(category1.products_in_list)
