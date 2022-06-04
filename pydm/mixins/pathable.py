
import os


class Pathable:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segment = self.__name__
        self.path = self._get_path()

    def _get_path(self, existing_path=None):
        if existing_path is None:
            return super()._get_path(self.segment)
        return os.path.join()

