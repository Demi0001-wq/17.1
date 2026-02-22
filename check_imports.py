import src.category
import src.product
import inspect

print(f"Category from: {inspect.getfile(src.category.Category)}")
print(f"Product from: {inspect.getfile(src.product.Product)}")

cat = src.category.Category("Test", "Desc", [])
print(f"Has get_products: {hasattr(cat, 'get_products')}")
