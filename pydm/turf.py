
import pydm.atom as atom
import pydm.predefined._procs as _procs
import pydm.predefined._vars as _vars
import pydm.predefined._verbs as _verbs


class Turf(atom.Atom):
    vars = [
        *atom.Atom.vars,
        _vars.Loc,
        _vars.X,
        _vars.Y,
        _vars.Z,
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


