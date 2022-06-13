
import os
from typing import Iterable


class Pathable:
    def __init__(self, *args, **kwargs):
        super().__init__(path=None, *args, **kwargs)
        self.root = getattr(self, 'root', None)
        self.path: str = self._get_path()

    @property
    def segments(self) -> Iterable[str]:
        """Iterates over the segments of the path"""
        return os.path.split(self.path)

    def _get_path(self) -> str:
        """Gets the path of the object"""
        pass





