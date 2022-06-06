
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
    vars = [
        *atom.Atom.vars,
        _vars.Ckey,
        _vars.Client,
        _vars.Gender,
        _vars.Key,
        _vars.Loc,
        _vars.Sight,
        _vars.X,
        _vars.Y,
        _vars.Z,
    ]


