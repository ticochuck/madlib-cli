from madlib_cli import __version__
from madlib_cli import madlib

def test_version():
    assert __version__ == '0.1.0'

def test_words_pass():
    actual = len(words)
    expected = 21
    assert actual == expected

def test_words_fail():
    actual = len(words)
    expected = 0
    assert actual == expected


