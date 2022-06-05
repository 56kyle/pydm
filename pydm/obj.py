
import pydm.atom as atom
import pydm.predefined._procs as _procs
import pydm.predefined._vars as _vars
import pydm.predefined._verbs as _verbs



class Obj(atom.Atom):
    procs = [
        *atom.Atom.procs,
        _procs.Bump,
        _procs.Move,
    ]

