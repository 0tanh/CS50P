from bank2 import bank_greet

def test_bank_hello():
    assert bank_greet("hello") == "$0"

def test_bank_other_h():
    assert bank_greet("Hey") == "$20"
    assert bank_greet("howdy") == "$20"

def test_bank_not_h():
    assert bank_greet("What's up") == "$100"