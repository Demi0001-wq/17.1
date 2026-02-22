import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Reset the class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0


def test_category_init() -> None:
    """Test category initialization and counters."""
    product1 = Product("Samsung Galaxy S23 Ultra", "200MP", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    
    category = Category("Смартфоны", "Description", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Description"
    assert len(category.get_products()) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories() -> None:
    """Test counting multiple categories and products."""
    p1 = Product("P1", "D1", 100.0, 10)
    p2 = Product("P2", "D2", 200.0, 20)
    c1 = Category("C1", "D1", [p1, p2])

    p3 = Product("P3", "D3", 300.0, 30)
    c2 = Category("C2", "D2", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_middle_price() -> None:
    """Test the middle_price method in Category."""
    p1 = Product("P1", "D1", 100.0, 10)
    p2 = Product("P2", "D2", 200.0, 20)
    c = Category("C1", "D1", [p1, p2])
    
    # middle_price should sum prices (100 + 200) and divide by product count (2)
    assert c.middle_price() == 150.0
    
    # Test empty category
    c_empty = Category("Empty", "Desc", [])
    assert c_empty.middle_price() == 0


def test_category_add_product_zero_quantity() -> None:
    """Test that ValueError is raised when adding a product with 0 quantity."""
    p = Product("Valid", "Desc", 100.0, 10)
    c = Category("Cat", "Desc", [p])
    
    # We can't create a Product with 0 quantity anymore, 
    # but we can try to add one if we bypass init (not recommended) 
    # or if we change it after init if there's a setter.
    # Actually, the requirement says raising ValueError in __init__ should be enough.
    # But add_product also has a check.
    
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        # Since Product.__init__ now raises ValueError, this line will fail before add_product
        c.add_product(Product("Zero", "Desc", 100.0, 0))
