
import pydm.proc as proc
import pydm.byond as byond
import pydm.mixins.pathable as pathable
import pydm.predefined._procs as _procs
import pydm.predefined._vars as _vars
import pydm.predefined._verbs as _verbs

import re


class Atom(byond.ByondObject, pathable.Pathable):
    """The Atom class is the base class for all objects in the game"""
    root = 'atom'

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
        _vars.Type,
        _vars.Name,
        _vars.Desc,
        _vars.Suffix,
        _vars.Text,
        _vars.Icon,
        _vars.IconState,
        _vars.Overlays,
        _vars.Underlays,
        _vars.Dir,
        _vars.Visibility,
        _vars.Luminosity,
        _vars.Opacity,
        _vars.Density,
    ]
    verbs = None

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def parse(cls, text: str):
        """Gets the object from text"""
        re.fullmatch(r'^[^-_\s]+$', text)

    def on_define(self, *args, **kwargs):
        """Called when the object is defined"""
        pass




