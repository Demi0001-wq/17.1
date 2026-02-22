from typing import Optional

from src.product import Product


class Category:
    """Class representing a category of products."""
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None) -> None:
        """
        Initialize a category.
        """
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the category.
        Task 1: Adds product to private attribute via append and increments product counter.
        Validation: Only Product instances (or subclasses) allowed.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты классов Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Getter for the private products attribute.
        Task 2: Returns a string with all products formatted according to the template.
        """
        result = ""
        for product in self.__products:
            # Format: "Название продукта, X руб. Остаток: X шт.\n"
            p_price = int(product.price) if product.price == int(product.price) else product.price
            result += f"{product.name}, {p_price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __len__(self) -> int:
        """
        Returns the total number of products in the category.
        Task 2 of 16.1.
        """
        return sum(p.quantity for p in self.__products)

    def __str__(self) -> str:
        """
        String representation of the category.
        Task 1 of 16.1.
        """
        return f"{self.name}, количество продуктов: {len(self)} шт."
