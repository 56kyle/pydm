import pydm.proc as proc


class Exit(proc.Proc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

