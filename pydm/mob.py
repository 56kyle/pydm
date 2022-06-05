
import pydm.atom as atom
import pydm.predefined._procs as _procs
import pydm.predefined._vars as _vars
import pydm.predefined._verbs as _verbs


class Mob(atom.Atom):
    procs = [
        *atom.Atom.procs,
        _procs.Bump,
        _procs.Login,
        _procs.Logout,
        _procs.Move,
    ]


