
import os
from typing import Iterable


class Pathable:
    def __init__(self, *args, **kwargs):
        super().__init__(path=None, *args, **kwargs)
        self.path: str = self.get_path()

    def get_path(self) -> str:
        """Gets the path of the object"""
        pass



