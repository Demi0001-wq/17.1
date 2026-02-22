class ZeroQuantityException(Exception):
    """Exception raised when a product with zero quantity is added."""
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)
