from typing import Any


class PrintMixin:
    """
    Mixin class that prints information about the object creation to the console.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Logs the class name and initialization arguments upon creation.
        """
        # Print the class name and all arguments used for creation
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        full_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"{self.__class__.__name__}({full_args})")
        
        super().__init__()
