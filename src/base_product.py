from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Abstract base class for all products.
    Defines the interface that every product must implement.
    """

    @abstractmethod
    def __str__(self) -> str:
        """String representation must be implemented by subclasses."""
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        """Addition logic must be implemented by subclasses."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Price getter must be implemented."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Price setter must be implemented."""
        pass
