
from typing import Generic, TypeVar


T = TypeVar('T')


class Var(Generic[T]):
    """The Var class represents a var object in dm code"""
    def __init__(self, value: any):
        self.value = value



