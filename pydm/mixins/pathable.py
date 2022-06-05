
import os
from typing import Iterable


class Pathable:
    def __init__(self, segments=Iterable[str], *args, **kwargs):
        super().__init__(path=None, *args, **kwargs)
        self.segment = self.__name__




