
import pydm.byond as byond


class Macro(byond.ByondObject):
    def __init__(self, name: str, value: any, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.value = value

    @classmethod
    def parse(cls, text: str):
        """Gets the object from text"""





