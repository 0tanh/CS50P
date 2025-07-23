import sys
import pytest
from lines import line


def test_lines():
    assert  == "Too many command-line arguments"

def test_no_argument(line):
    line.setattr(sys, "argv", ["my_script.py"])
    assert process_args() == "Too few command-line arguments"

def test_exit_lines():
    with pytest.raises(SystemExit) as excinfo:
        line(True)
    assert str(excinfo.value) == "Too many command-line arguments"