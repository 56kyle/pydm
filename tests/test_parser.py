
import pytest

import pydm.parser as parser


Parser = parser.Parser


def test_remove_comments():
    text = '''
    // This is a comment
    foo
    // This is another comment
    /* This is a multi-line
     comment */
    /* This is a multi-line comment /* This is a nested multi-line comment */
    This is after a multi-line nested comment
    */
    '''
    assert Parser.remove_comments(text) == ''




