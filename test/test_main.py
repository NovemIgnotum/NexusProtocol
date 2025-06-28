import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game import player
from game import utils

def test_true_is_true():
    assert True == True

def test_hello_world(capsys):
    print("Hello, le monde")
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"