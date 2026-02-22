import json

from src.category import Category
from src.product import Product


def load_data(path: str) -> list[Category]:
    """
    Loads data from a JSON file and returns a list of Category objects.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data.get("products", []):
            products.append(Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"]
            ))
        categories.append(Category(
            category_data["name"],
            category_data["description"],
            products
        ))
    return categories
