import pytest

from src.product import Product


def test_product_init() -> None:
    """Test product initialization."""
    name = "Samsung Galaxy S23 Ultra"
    description = "256GB, Серый цвет, 200MP камера"
    price = 180000.0
    quantity = 5
    product = Product(name, description, price, quantity)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity
