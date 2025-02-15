class Product:
    """Класс продуктов"""

    name: str  # название продукта
    description: str  # описание  продукта
    price: str  # цена  продукта
    quantity: int  # количество продукта

    def __init__(self, name, description, price, quantity):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_new, actual_list=None):
        """Возвращает объект класса Product из товара в словаре"""
        if actual_list:
            for product in actual_list:
                if product.name == product_new["name"]:
                    product.quantity += product_new["quantity"]
                    product.price = max([product.price, product_new["price"]])
                    return product
        return cls(product_new["name"], product_new["description"],
                   product_new["price"], product_new["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = input("Нужно изменить цену  Y/N")
            if answer != "Y":
                return self.__price == value


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra"
                       "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

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

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    print(product4.name)
    print(product4.description)
    print(product4.price)
    print(product4.quantity)

    product5 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    print(product5.name)
    print(product5.quantity)
