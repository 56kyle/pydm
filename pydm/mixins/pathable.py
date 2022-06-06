
import os
from typing import Iterable


class Pathable:
    def __init__(self, root: str, name: str, *args, **kwargs):
        super().__init__(path=None, *args, **kwargs)
        self.root: str = root
        self.name: str = name
        self.path: str = os.path.join(root, name)


