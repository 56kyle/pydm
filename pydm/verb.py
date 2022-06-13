
import pydm.mixins.pathable as pathable


class Verb(pathable.Pathable):
    """The Verb class represents a verb object in dm code"""
    root = 'verb'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

