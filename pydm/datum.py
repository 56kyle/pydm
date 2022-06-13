
import pydm.byond as byond
import pydm.mixins.pathable as pathable


class Datum(byond.ByondObject, pathable.Pathable):
    root = 'datum'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_define(self, *args, **kwargs):
        """Called when the object is defined"""
        pass




