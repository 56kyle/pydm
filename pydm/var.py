
import pydm.byond as byond
import pydm.mixins.pathable as pathable
import re


class Var(byond.ByondObject, pathable.Pathable):
    """The Var class represents a var object in dm code"""
    flags = ['global', 'const', 'static', 'tmp']
    re_syntax = re.compile(r'^\s*var\s+(\w+)\s*=\s*(.*)$')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
