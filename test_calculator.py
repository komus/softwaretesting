import pytest
from calculator import Calculator

"Test must be independent of each other"

def test_add():
    cal = Calculator(10)
    first_add = cal.add(20)
    assert first_add == 30
    assert  cal.add(4.5) == 34.5


def test_sub():
    pass

def test_input_is_numeric():
    pass

def test_add_then_subtract():
    cal = Calculator()
    cal.add(10)
    assert cal.sub(5) == 5


def test_divide():
    pass

def test_zero_division_returns_None():
    pass