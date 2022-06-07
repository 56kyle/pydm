import re
import uuid

import pydm.parsing.structures as structures


class DmFile:
    def __init__(self, text, *args, **kwargs):
        self.text: str = text
        self.preprocessed = self.preprocess(text)
        self.parsed = self.parse()
        self.objects = {}
        self.references = {}

    @staticmethod
    def preprocess(text):
        pass

    def parse(self):
        pass

    @staticmethod
    def replace_single_line_comments(text: str):
        new_lines = []
        for line in text.split('\n'):
            if '//' in line:
                new_lines.append(line.split('//')[0])

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
        possible_types = {
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
        reference = possible_types[location](text[location:ending + len(possible_types[location].end)])
        self.references[reference.uuid] = reference
        return text[:location] + reference.uuid + text[ending + len(possible_types[location].end):], 1

