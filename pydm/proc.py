
import pydm.byond as byond

class Proc:
    """The Proc class represents a proc in dm code"""
    name: str = None
    code: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
