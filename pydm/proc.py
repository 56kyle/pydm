

class Proc:
    """The Proc class represents a proc in dm code"""
    def __init__(self, name: str, code: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name: str = name
        self.code: str = code



