

import pytest
import os


@pytest.fixture
def tests_dir():
    return os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def pydm_dir(tests_dir):
    return os.path.dirname(tests_dir)
