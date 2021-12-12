import pytest


def test_is_capital():
    name = "Michael"
    assert name.isupper() == False


def test_name_in_list():
    students = ['Ivar', 'Jaan', 'Mike']
    assert  "Ivar" in students


def test_raises_exception():
    with pytest.raises(ZeroDivisionError) as ex:
        10/ 0
