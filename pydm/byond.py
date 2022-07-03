
import os
import re

from typing import Dict


class ByondObject:
    """The ByondObject class represents a byond object in dm code"""
    references: Dict = {}
    re_syntax = None

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_define(*args, **kwargs)
        self.text = text
        self.replaced = self.parse(text)

    def __str__(self):
        for reference in self.references.values():
            self.text.replace(reference.uuid, str(reference))

    @classmethod
    def find(cls, text: str) -> [object, int, int]:
        """Finds the first instance of the object in the text"""
        text_found: re.Match | None
        if cls.re_syntax:
            text_found = re.search(cls.re_syntax, text)
        else:
            raise NotImplementedError('re_syntax not implemented')
        if text_found:
            return cls(text[text_found.start():text_found.end()]), text_found.start(), text_found.end()
        else:
            return None, 0, 0

    def parse(self, text: str) -> str:
        """Parses the text for other byond objects and replaces them with their uuids"""
        for reference in self.references.values():
            text = text.replace(reference.text, reference.uuid)
        return text

    def on_define(self, *args, **kwargs):
        """Called when the object is defined"""
        pass

















