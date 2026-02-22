# Skystore E-commerce Project

Foundational core for an e-commerce platform using Object-Oriented Programming (OOP) in Python. This project implements the foundational logic for managing products, categories, and orders.

## Features

- Product Management: Track name, description, price, and quantity with private price attributes.
- Category Management: Group products and track global category/product statistics.
- Order Management: Handle purchase orders for specific products and quantities.
- Magic Methods (Lesson 16.1):
  - `__str__`: Clear string representation for Products and Categories.
  - `__len__`: Total quantity of products in a category.
  - `__add__`: Secure addition of products (restricted to same-class only).
- Inheritance & Abstraction:
  - `BaseProduct` & `BaseCategory` abstract classes for interface consistency.
  - specialized `Smartphone` and `LawnGrass` subclasses.
  - `PrintMixin` for automatic object creation logging.
- Encapsulation: Strict type checking for adding products and price validation with interactive confirmation.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Demi0001-wq/10.1.git
   ```
2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Example

```python
from src.product import Product
from src.category import Category

# Create products (auto-logged by PrintMixin)
p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5)
p2 = Product("Iphone 15", "512GB, Gray", 210000.0, 8)

# Create category
cat = Category("Smartphones", "Modern mobile devices", [p1, p2])

# Magic methods in action
print(str(p1))      # "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
print(len(cat))     # 13 (total quantity)
print(p1 + p1)      # 1800000.0 (sum of price * quantity)
```

## Testing

To run the unit tests:
```bash
pytest
```
To check coverage:
```bash
pytest --cov=src
```

### Metadata
The project includes a `.gitignore` and `requirements.txt` for clean development and easy setup.
