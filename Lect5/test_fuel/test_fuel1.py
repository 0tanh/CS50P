from fuel1 import Convert
from fuel1 import gauge
import pytest
## TESTING CONVERT
def test_fuel_percent():
    assert Convert("3/4") == 75.0

def test_div_0():
    with pytest.raises(ZeroDivisionError):
        Convert("4/0")

def test_value_error_Convert():
    with pytest.raises(ValueError):
        Convert("three/four")

def test_interger_v_float():
    with pytest.raises(ValueError):
        Convert("1.5/2")

def test_exceptions():
    with pytest.raises(ValueError):
        Convert("-3/4")

## TESTING GAUGE
def test_fuel_full():
    assert gauge(Convert("4/4")) == "F"

def test_fuel_empty():
    assert gauge(Convert("0/4")) == "E"



# def test_overfill():
#     assert "5/4" == "Overfill"