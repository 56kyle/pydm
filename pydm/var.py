
import pydm.byond as byond
import pydm.mixins.pathable as pathable


class Var(byond.ByondObject, pathable.Pathable):
    """The Var class represents a var object in dm code"""
    flags = ['global', 'const', 'static', 'tmp']

    def __init__(self, name: str, value: any = None, *args, **kwargs):
        self.name = name
        self.value = value
        super().__init__(*args, **kwargs)



