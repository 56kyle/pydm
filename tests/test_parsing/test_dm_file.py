
import pytest
import os

import pydm.parsing.dm_file as dm_file


def test_dm_file_escape_text():
    dm = dm_file.DmFile(
        '''foo
        // This is a comment
        // This is another comment
        /* This is a
        multi - line
        comment */
        "This is a string"
        {"This is a multiline
        string
        "}
        \'This is a file location\'
        bar
        '''
    )
    escaped_text = dm.get_escaped_text(dm.text)
    assert 'foo' in escaped_text
    assert 'bar' in escaped_text
    assert 'This is a comment' not in escaped_text
    assert 'This is another comment' not in escaped_text
    assert 'This is a' not in escaped_text
    assert 'multi - line' not in escaped_text
    assert 'comment' not in escaped_text
    assert 'This is a string' not in escaped_text
    assert 'This is a multiline' not in escaped_text
    assert 'string' not in escaped_text
    assert 'This is a file location' not in escaped_text

