import os
from misc_utils import debug_utils

def test_init():
    assert os.getenv('EXAMPLE_VARIABLE') != None

def test_get_debug():
    assert isinstance(debug_utils.get_debug(), bool)
