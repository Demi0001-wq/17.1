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


def test_product_zero_quantity() -> None:
    """Test that ValueError is raised when quantity is 0."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Desc", 100.0, 0)
