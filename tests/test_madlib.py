from madlib_cli import __version__
from madlib_cli.madlib import open_template, get_words, write_new_content

def test_version():
    assert __version__ == '0.1.0'

