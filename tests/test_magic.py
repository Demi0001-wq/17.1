import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Reset the class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0


def test_product_str() -> None:
    """Test string representation of Product."""
    product = Product("Samsung", "200MP", 100.0, 5)
    assert str(product) == "Samsung, 100.0 руб. Остаток: 5 шт."


def test_category_str() -> None:
    """Test string representation of Category."""
    p1 = Product("P1", "D1", 100.0, 10)
    p2 = Product("P2", "D2", 200.0, 20)
    category = Category("Smartphones", "Desc", [p1, p2])
    assert str(category) == "Smartphones, количество продуктов: 30 шт."


def test_product_add() -> None:
    """Test magic addition of two products."""
    p1 = Product("P1", "D1", 100.0, 10)  # 1000
    p2 = Product("P2", "D2", 200.0, 2)   # 400
    assert p1 + p2 == 1400


def test_iterator() -> None:
    """Test ProductIterator functionality."""
    p1 = Product("P1", "D1", 100.0, 1)
    p2 = Product("P2", "D2", 200.0, 2)
    cat = Category("C1", "D1", [p1, p2])
    
    it = ProductIterator(cat)
    prods = [p for p in it]
    
    assert len(prods) == 2
    assert prods[0] == p1
    assert prods[1] == p2
