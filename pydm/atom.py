
import pydm.proc as proc
import predefined._procs as _procs
import predefined._vars as _vars
import predefined._verbs as _verbs


class Atom:
    """The Atom class is the base class for all objects in the game"""
    procs = [
        _procs.New,
        _procs.Click,
        _procs.DblClick,
        _procs.Del,
        _procs.Enter,
        _procs.Exit,
        _procs.Read,
        _procs.Stat,
        _procs.Topic,
        _procs.Write,
    ]
    vars = [

    ]
    verbs = None

    def __init__(self, *args, **kwargs):
        pass


