from typing import Any, Optional
from src.base_product import BaseProduct
from src.print_mixin import PrintMixin
from src.exceptions import ZeroQuantityException


class Product(PrintMixin, BaseProduct):
    """Class representing a product in the store."""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Initialize a product.
        :param name: Name of the product
        :param description: Description of the product
        :param price: Product price (float)
        :param quantity: Quantity in stock (int)
        """
        if quantity == 0:
            raise ZeroQuantityException()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        # Call PrintMixin.__init__
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """
        String representation of the product.
        Format: "Название продукта, X.X руб. Остаток: X шт."
        """
        return f"{self.name}, {float(self.price)} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """Technical representation of the product."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    def __add__(self, other: Any) -> float:
        """
        Magic method for adding two products.
        Only objects of the exact same class can be added.
        Returns the sum of (price * quantity) for both products.
        """
        if type(self) is not type(other):
            raise TypeError("Can only add products of the same class.")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, data: dict[str, Any], existing_products: Optional[list["Product"]] = None) -> "Product":
        """
        Class method to create or update a Product instance from a dictionary.
        """
        name = data["name"]
        description = data["description"]
        price = data["price"]
        quantity = data["quantity"]

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Getter for the price attribute."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Setter for the price attribute with validation."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            confirm = input("Цена понижается. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.__price = value
        else:
            self.__price = value


class Smartphone(Product):
    """Subclass representing a smartphone."""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Subclass representing lawn grass."""
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
