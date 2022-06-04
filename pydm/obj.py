
import atom
import predefined._procs as _procs
import predefined._vars as _vars
import predefined._verbs as _verbs


class Obj(atom.Atom):
    procs = [
        *atom.Atom.procs,
        _procs.Bump,
        _procs.Move,
    ]

