from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """
    Abstract base class for Category and Order.
    Ensures a shared interface for product-holding entities.
    """

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the container."""
        pass

    @property
    @abstractmethod
    def products(self) -> str:
        """Return a string representation of the products held."""
        pass
