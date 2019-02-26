import os
from misc_utils import debug_utils

def test_init():
    assert os.getenv('EXAMPLE_VARIABLE') != None
    assert eval(os.getenv('EXAMPLE_VARIABLE')) 

def test_is_debug():
    assert isinstance(debug_utils.is_debug(), bool)
