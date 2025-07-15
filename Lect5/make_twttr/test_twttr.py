from twttr import shorten

def test_shorten():
    assert shorten("love") == "ur tweet without vowels: lv"

def test_shorten_caps():
    assert shorten("LOvE") == "ur tweet without vowels: Lv"
