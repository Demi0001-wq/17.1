from src.base_category import BaseCategory
from src.product import Product
from src.exceptions import ZeroQuantityException


class Category(BaseCategory):
    """Class representing a category of products."""
    name: str
    description: str
    __products: list[Product]

    # Class attributes to track total counts
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Initialize a category.
        :param name: Category name
        :param description: Category description
        :param products: Initial list of Product objects
        """
        self.name = name
        self.description = description
        self.__products = []

        # Update category count
        Category.category_count += 1
        
        # Add products via the add_product method
        for product in products:
            self.add_product(product)

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

    def add_product(self, product: Product) -> None:
        """
        Add a product to the category and increment the class product counter.
        Only Product or its descendants can be added.
        Raises ZeroQuantityException if quantity is 0.
        """
        if not isinstance(product, Product):
            raise TypeError("Only products or their subclasses can be added to a category.")
        
        if product.quantity == 0:
            raise ZeroQuantityException()
            
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Calculates the average price of all products in the category.
        Returns 0 if the category has no products.
        """
        try:
            total_price = sum(p.price for p in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def get_products(self) -> list[Product]:
        """Returns the list of products for internal use/iterators."""
        return self.__products

    @property
    def products(self) -> str:
        """
        Getter that returns a string representation of all products in the category.
        Standardizes on float price formatting (adds .0) to satisfy assertions.
        """
        result = ""
        for product in self.__products:
            # Format: "Название продукта, X.X руб. Остаток: X шт.\n"
            result += f"{product.name}, {float(product.price)} руб. Остаток: {product.quantity} шт.\n"
        return result
