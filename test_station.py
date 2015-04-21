import pytest, copy, collections
from station import SubwayStation

def test_name_getter_and_setter():
    s = SubwayStation()
    assert s.get_name() == ""
    s.set_name("Atlantic Avenue - Barclay's Center")
    assert s.get_name() == "Atlantic Avenue - Barclay's Center"
