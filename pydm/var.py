
from typing import Generic, TypeVar


T = TypeVar('T')


class Var(Generic[T]):
    """The Var class represents a var object in dm code"""
    flags = ['global', 'const', 'static', 'tmp']

    def __init__(self, name: str, value: any = None, *args, **kwargs):
        self.name = name
        self.value = value



