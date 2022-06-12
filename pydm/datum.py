
import pydm.byond as byond
import pydm.mixins.pathable as pathable


class Datum(byond.ByondObject, pathable.Pathable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




