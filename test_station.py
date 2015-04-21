import pytest, copy, collections
from station import SubwayStation

def test_name_getter_and_setter():
    s = SubwayStation()
    assert s.get_name() == ""
    s.set_name("Atlantic Avenue - Barclay's Center")
    assert s.get_name() == "Atlantic Avenue - Barclay's Center"

def test_use_name_as_repr():
    s = SubwayStation()
    s.set_name('Test Station')
    assert str(s) == "Test Station"

def test_set_neighbors_accepts_optional_distance():
    s = SubwayStation()
    s.set_neighbor('34th St - Penn Station')
    assert s.get_neighbors() == [('34th St - Penn Station', None)]
    s.set_neighbor('23rd St', 4)
    assert set(s.get_neighbors()) == set([('34th St - Penn Station', None), ('23rd St', 4)])

def test_set_neighbors_stores_shortest_distance():
    s = SubwayStation()
    s.set_neighbor('34th St')
    assert s.get_neighbors() == [('34th St', None)]
    s.set_neighbor('34th St', 12)
    assert s.get_neighbors() == [('34th St', 12)]
    s.set_neighbor('34th St', 7)
    assert s.get_neighbors() == [('34th St', 7)]
    s.set_neighbor('34th St', 9)
    assert s.get_neighbors() == [('34th St', 7)]
    s.set_neighbor('34th St')
    assert s.get_neighbors() == [('34th St', 7)]
