
import re

import pydm.alias as alias
import pydm.area as area
import pydm.atom as atom
import pydm.client as client
import pydm.datum as datum
import pydm.mob as mob
import pydm.obj as obj
import pydm.proc as proc
import pydm.savefile as savefile
import pydm.turf as turf
import pydm.var as var
import pydm.verb as verb
import pydm.world as world


class Parser:
    def __init__(self, *args, **kwargs):
        self.alias = alias.Alias()
        self.area = area.Area()
        self.atom = atom.Atom()
        self.client = client.Client()
        self.datum = datum.Datum()
        self.mob = mob.Mob()
        self.obj = obj.Obj()
        self.savefile = savefile.SaveFile()
        self.turf = turf.Turf()
        self.world = world.World()

        self.bases = [
            self.alias,
            self.area,
            self.atom,
            self.client,
            self.datum,
            self.mob,
            self.obj,
            self.savefile,
            self.turf,
            self.world,
        ]

    def preprocess(self, text: str) -> str:
        text = self.process_directives(text)
        text = self.remove_comments(text)
        return ''

    def process(self, text: str):
        return ''

    def parse(self):
        pass

    @staticmethod
    def process_directives(text: str) -> str:
        return text

    @staticmethod
    def remove_comments(text: str) -> str:
        text = Parser.remove_single_line_comments(text)
        print('without single line comments: ', text)
        text = Parser.remove_multi_line_comments(text)
        print('without multi line comments: ', text)
        return text

    @staticmethod
    def remove_single_line_comments(text: str) -> str:
        return re.sub(r'//.*', '', text)

    @staticmethod
    def remove_multi_line_comments(text: str | re.Match) -> str:
        if isinstance(text, re.Match):
            text = text.group(0)
            if '/*' not in text:
                return text
        return re.sub(r'/\*(.*)\*/', Parser.remove_multi_line_comments, text)







