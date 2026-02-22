from src.product import Product


class ProductIterator:
    """
    Helper class to iterate through products in a Category.
    """
    def __init__(self, category_obj) -> None:
        """
        Initialize the iterator with a category object.
        Retrieves the private __products list.
        """
        # Note: Accessing private attribute __products via name mangling
        # or we could make it a property in Category.
        # But per the task, we pass a category object.
        self.products = category_obj.get_products()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Product:
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
