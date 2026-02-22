import pytest
from src.category import Category
from src.product import Product
from src.order import Order
from src.exceptions import ZeroQuantityException


def test_zero_quantity_exception():
    """Test that ZeroQuantityException is raised when quantity is 0."""
    with pytest.raises(ZeroQuantityException):
        Product("Test", "Desc", 100.0, 0)
        # However, the requirement says it should be raised when added to category
        # Or when created. Let's check Category.add_product
    
    p = Product("Valid", "Desc", 100.0, 10)
    c = Category("Cat", "Desc", [p])
    
    # Manually creating a 0 quantity product to add
    p_zero = Product("Zero", "Desc", 100.0, 5)
    p_zero.quantity = 0 
    
    with pytest.raises(ZeroQuantityException):
        c.add_product(p_zero)


def test_category_average_price():
    """Test the average_price method in Category."""
    p1 = Product("P1", "D1", 100.0, 10)
    p2 = Product("P2", "D2", 200.0, 20)
    c = Category("C1", "D1", [p1, p2])
    
    assert c.average_price() == 150.0
    
    # Test empty category
    c_empty = Category("Empty", "Desc", [])
    assert c_empty.average_price() == 0


def test_print_mixin_order(capsys):
    """Test that Order uses PrintMixin correctly."""
    p = Product("Smartphone", "Latest model", 50000.0, 10)
    capsys.readouterr() # Clear previous output
    
    Order(p, 2)
    captured = capsys.readouterr()
    assert "Order" in captured.out
    assert "Smartphone" in captured.out
