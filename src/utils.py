import json
import os
from src.main import Product, Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result


def create_objects_from_json(result):
    names_ = []
    for name in result:
        products_ = []
        for product in name["products"]:
            products_.append(Product(**product))
        name["products"] = products_
        names_.append(Category(**name))
    return names_


if __name__ == "__main__":
    raw_data = read_json("../products.json")
    print(raw_data)
    object_data = create_objects_from_json(raw_data)
    print(object_data)
    print(object_data[0].name)
    print(object_data[0].products)
