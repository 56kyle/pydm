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
        self.escaped_text: str = self.get_escaped_text(text)
        self.without_comments: str = self.replace_comments(self.escaped_text)
        self.without_line_breaks: str = self.replace_line_breaks(self.without_comments)
        self.with_normalized_lines: str = self.normalize_new_lines(self.without_line_breaks)
        self.preprocessed: str = self.with_normalized_lines
        self.current_object = None

    def parse(self):
        pass

    def get_escaped_text(self, text: str, running: bool = True):
        new_text = text
        while running:
            new_text, running = self.iter_escaped_text(new_text)
        return new_text

    def iter_escaped_text(self, text: str):
        """
        Iterates over the text and replaces escaped characters with their unescaped counterparts
        :param text:
        :return:
        """
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

    @staticmethod
    def replace_comments(text: str) -> str:
        return text

    @staticmethod
    def replace_line_breaks(text: str) -> str:
        return re.sub(r'\\\n[ \t]*', '', text)

    @staticmethod
    def normalize_new_lines(text: str) -> str:
        """"""
        lines = []
        for line in text.split('\n'):
            new_line = line
            spacer_tracker = line
            spacers = []
            for i, spacer in enumerate(spacers):
                if spacer in new_line:
                    new_line = spacer_tracker.replace(spacer, '', 1)
                else:
                    spacers.pop(i)
            new_spacer = re.search(r'^([ \t]+)', spacer_tracker)
            if new_spacer:
                spacers.append(new_spacer.group(1))

            if ';' in line:
                spacers_combined = ''.join(spacers)
                print(line, ' - ', spacers_combined)
                new_line = line.replace(';', f'\n{spacers_combined}')
            lines.append(new_line)
        return '\n'.join(lines)

    @staticmethod
    def normalize_node_paths(text: str) -> str:
        """Standardizes all node paths so they are absolute paths"""
        lines = text.split('\n')
        for i, line in enumerate(lines):
            new_line = line
            spacer_tracker = line
            spacers = []
            for j, spacer in enumerate(spacers):
                if spacer in new_line:
                    new_line = spacer_tracker.replace(spacer, '', 1)
                else:
                    spacers.pop(j)
            new_spacer = re.search(r'^([ \t]+)', spacer_tracker)
            if new_spacer:
                spacers.append(new_spacer.group(1))










