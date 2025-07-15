from bank2 import value

def test_bank_hello():
    assert value("hello") == "$0"

def test_bank_other_h():
    assert value("Hey") == "$20"
    assert value("howdy") == "$20"

def test_bank_not_h():
    assert value("What's up") == "$100"