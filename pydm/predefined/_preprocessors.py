
import pydm.preprocessor as preprocessor


class Define(preprocessor.Preprocessor):
    keyword = '#define'
    syntax = '#define {name} {value}'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def action(self, *args, **kwargs):
        self.byond.define(self.name, self.value)

class If(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Elif(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Ifdef(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Ifndef(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Else(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Include(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Error(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Warn(preprocessor.Preprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

