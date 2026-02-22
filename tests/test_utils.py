import os

import pytest

from src.category import Category
from src.utils import load_data


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Reset the class-level counters before each test."""
    Category.category_count = 0
    Category.product_count = 0


def test_load_data(tmp_path) -> None:
    """Test loading data from a temporary JSON file."""
    json_content = """
    [
      {
        "name": "Test Category",
        "description": "Test Desc",
        "products": [
          {
            "name": "Test Product",
            "description": "Test P Desc",
            "price": 100.0,
            "quantity": 10
          }
        ]
      }
    ]
    """
    json_file = tmp_path / "test_products.json"
    json_file.write_text(json_content, encoding="utf-8")
    categories = load_data(str(json_file))
    
    assert len(categories) == 1
    assert categories[0].name == "Test Category"
    assert len(categories[0].get_products()) == 1
    assert categories[0].get_products()[0].name == "Test Product"
    assert Category.category_count == 1
    assert Category.product_count == 1
