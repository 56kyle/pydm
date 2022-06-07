

import pydm.parsing.structures as structures


filler_text = 'foo bar baz'

single_line_comment_text = '// This is a comment\n'
multi_line_comment_text = '/* This is a\nmulti - line\ncomment */'
single_line_string_text = '"This is a string"'
multi_line_string_text = '{"This is a multiline\nstring\n"}'
single_line_file_location_text = '\'This is a file location\''


def test_single_line_comment_find_start():
    start = structures.SingleLineComment.find_start(filler_text + single_line_comment_text + filler_text)
    expected = len(filler_text)
    assert start == expected

def test_single_line_comment_find_end():
    start = len(filler_text) + len(structures.SingleLineComment.start)
    ending = structures.SingleLineComment.find_end(filler_text + single_line_comment_text + filler_text, start)
    expected = len(filler_text) + len(single_line_comment_text) - len(structures.SingleLineComment.end)
    assert ending == expected

def test_multi_line_comment_find_start():
    start = structures.MultiLineComment.find_start(filler_text + multi_line_comment_text + filler_text)
    expected = len(filler_text)
    assert start == expected

def test_multi_line_comment_find_end():
    start = len(filler_text) + len(structures.MultiLineComment.start)
    ending = structures.MultiLineComment.find_end(filler_text + multi_line_comment_text + filler_text, start)
    expected = len(filler_text) + len(multi_line_comment_text) - len(structures.MultiLineComment.end)
    assert ending == expected

def test_single_line_string_find_start():
    start = structures.SingleLineString.find_start(filler_text + single_line_string_text + filler_text)
    expected = len(filler_text)
    assert start == expected

def test_single_line_string_find_end():
    start = len(filler_text) + len(structures.SingleLineString.start)
    ending = structures.SingleLineString.find_end(filler_text + single_line_string_text + filler_text, start)
    expected = len(filler_text) + len(single_line_string_text) - len(structures.SingleLineString.end)
    assert ending == expected

def test_multi_line_string_find_start():
    start = structures.MultiLineString.find_start(filler_text + multi_line_string_text + filler_text)
    expected = len(filler_text)
    assert start == expected

def test_multi_line_string_find_end():
    start = len(filler_text) + len(structures.MultiLineString.start)
    ending = structures.MultiLineString.find_end(filler_text + multi_line_string_text + filler_text, start)
    expected = len(filler_text) + len(multi_line_string_text) - len(structures.MultiLineString.end)
    assert ending == expected

def test_single_line_file_location_find_start():
    start = structures.SingleLineFileLocation.find_start(filler_text + single_line_file_location_text + filler_text)
    expected = len(filler_text)
    assert start == expected

def test_single_line_file_location_find_end():
    start = len(filler_text) + len(structures.SingleLineFileLocation.start)
    ending = structures.SingleLineFileLocation.find_end(filler_text + single_line_file_location_text + filler_text, start)
    expected = len(filler_text) + len(single_line_file_location_text) - len(structures.SingleLineFileLocation.end)
    assert ending == expected



