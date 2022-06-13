import re
import uuid

import pydm.parsing.structures as structures
import pydm.byond
from typing import Dict, List


class DmFile:
    byond = pydm.byond.ByondObject

    def __init__(self, text, *args, **kwargs):
        self.text: str = text
        self.definitions: Dict[str, ] = {}
        self.objects = {}
        self.preprocessed: str = self.preprocess(text)
        self.without_comments: str = self.remove_comments(self.preprocessed)

    def preprocess(self, text):
        return self.get_escaped_text(text)

    def parse(self):
        pass

    def remove_comments(self, text: str):
        for reference in self.byond.references.values():
            if isinstance(reference, structures.DmComment):
                text = text.replace(reference.uuid, '')
        return text

    def get_escaped_text(self, text: str, running: bool = True):
        new_text = text
        while running:
            new_text, running = self.iter_escaped_text(new_text)
        return new_text

    def iter_escaped_text(self, text: str):
        first_single_line_comment = structures.SingleLineComment.find_start(text)
        first_multi_line_comment = structures.MultiLineComment.find_start(text)
        first_single_line_string = structures.SingleLineString.find_start(text)
        first_multi_line_string = structures.MultiLineString.find_start(text)
        first_single_line_file_location = structures.SingleLineFileLocation.find_start(text)

        location = first_single_line_file_location
        location_type = None
        possible_types: Dict[int, any] = {
            first_single_line_comment: structures.SingleLineComment,
            first_multi_line_comment: structures.MultiLineComment,
            first_single_line_string: structures.SingleLineString,
            first_multi_line_string: structures.MultiLineString,
            first_single_line_file_location: structures.SingleLineFileLocation,
        }

        for first_location, first_type in possible_types.items():
            if first_location != -1:
                location = first_location if first_location < location else location
                location_type = first_type if first_location < location else location_type
        if location is None or location == -1:
            return text, 0
        ending = possible_types[location].find_end(text, location + len(possible_types[location].start))
        reference = possible_types[location](text[location:ending + possible_types[location].end_length])
        self.byond.references[reference.uuid] = reference
        return text[:location] + reference.uuid + text[ending + possible_types[location].end_length:], 1



