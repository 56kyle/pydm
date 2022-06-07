
import uuid

class DmObject:
    start: str = None
    end: str = None

    def __init__(self, text: str, *args, **kwargs):
        self.text: str = text
        self.uuid = str(uuid.uuid4())

    def __str__(self):
        return self.text

    @classmethod
    def find_start(cls, text: str, start: int = None, end: int = None):
        return text.find(cls.start, start, end)

    @classmethod
    def find_end(cls, text: str, start: int = None, end: int = None):
        end_location = text.find(cls.end, start, end)
        if not cls.is_valid_end(text, end_location):
            return cls.find_end(text, end_location + len(cls.end) + 1, end)
        if end_location == -1:
            raise Exception('End not found')
        return end_location

    @classmethod
    def is_valid_start(cls, text: str, location: int) -> bool:
        return True

    @classmethod
    def is_valid_end(cls, text: str, location: int) -> bool:
        return True


class DmComment(DmObject):
    pass

class DmString(DmObject):
    @classmethod
    def is_valid_end(cls, text: str, location: int) -> bool:
        return text[location - 1] != '\\'

class SingleLineComment(DmComment):
    start = '//'
    end = '\n'

class MultiLineComment(DmComment):
    start = '/*'
    end = '*/'

class SingleLineString(DmString):
    start = '"'
    end = '"'

class MultiLineString(DmString):
    start = '{"'
    end = '"}'

class SingleLineFileLocation(DmString):
    start = '\''
    end = '\''

