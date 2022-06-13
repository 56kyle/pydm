
import os

import pydm.mixins.pathable as pathable

from typing import Dict


class ByondObject:
    """The ByondObject class represents a byond object in dm code"""
    byond: Dict = {}
    references: Dict = {}

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_define(*args, **kwargs)
        self.text = text

    def __str__(self):
        for reference in self.references.values():
            self.text.replace(reference.uuid, str(reference))

    def on_define(self, *args, **kwargs):
        """Called when the object is defined"""
        pass
















