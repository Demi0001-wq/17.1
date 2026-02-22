import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


def test_smartphone_init() -> None:
    s = Smartphone("S23", "Desc", 100.0, 5, 95.0, "ModelX", 128, "Black")
    assert s.name == "S23"
    assert s.efficiency == 95.0
    assert s.model == "ModelX"
    assert s.memory == 128
    assert s.color == "Black"


def test_lawngrass_init() -> None:
    lg = LawnGrass("Grass", "Desc", 10.0, 100, "USA", "5 days", "Green")
    assert lg.name == "Grass"
    assert lg.country == "USA"
    assert lg.germination_period == "5 days"
    assert lg.color == "Green"


def test_product_add_same_class() -> None:
    s1 = Smartphone("S1", "D1", 100.0, 2, 90.0, "M1", 64, "Red")
    s2 = Smartphone("S2", "D2", 200.0, 3, 91.0, "M2", 128, "Blue")
    # (100*2) + (200*3) = 200 + 600 = 800
    assert s1 + s2 == 800.0


def test_product_add_different_class() -> None:
    s = Smartphone("S1", "D1", 100.0, 2, 90.0, "M1", 64, "Red")
    lg = LawnGrass("G1", "D2", 10.0, 50, "RU", "7d", "Green")
    with pytest.raises(TypeError):
        s + lg


def test_category_add_product_validation() -> None:
    cat = Category("Smartphones", "Desc", [])
    s = Smartphone("S1", "D1", 100.0, 2, 90.0, "M1", 64, "Red")
    cat.add_product(s)
    assert Category.product_count == 1
    
    with pytest.raises(TypeError):
        cat.add_product("Not a product")


def test_product_add_base_and_subclass() -> None:
    p = Product("Base", "D", 100.0, 1)
    s = Smartphone("S1", "D1", 100.0, 2, 90.0, "M1", 64, "Red")
    with pytest.raises(TypeError):
        p + s
