
import os
import pydm.mixins.pathable as pathable


class ByondObject:
    """The ByondObject class represents a byond object in dm code"""
    def __init__(self, *args, **kwargs):
        self.byond = {}
        super().__init__(*args, **kwargs)
        self.on_define(*args, **kwargs)

    @classmethod
    def parse(cls, *args, **kwargs):
        """Gets the object from text"""
        pass

    def on_define(self, *args, **kwargs):
        """Called when the object is defined"""
        pass














