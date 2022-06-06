
from typing import List


class ParsedFile:
    def __init__(self, text: str, *args, **kwargs):
        self.text = text
        self.contents = [text]
        self.replace_strings(self.contents)

    @staticmethod
    def replace_strings(contents: List) -> List:
        for






