class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}," \
               f"" f"{self.description}, {self.price}, {self.quantity})"
