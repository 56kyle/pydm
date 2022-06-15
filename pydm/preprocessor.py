
import re
import pydm.byond as byond


class Preprocessor(byond.ByondObject):
    re_syntax = None
    re_start = None
    re_end = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def _find(cls, text: str):
        if cls.re_start and cls.re_end:
            start = re.search(cls.re_start, text)
            end = re.search(cls.re_end, text)
            if start and end:
                return cls(text[start.start():end.end()])
        else:
            result = re.search(cls.re_syntax, text)
            if result:
                return cls(text[result.start():result.end()])

