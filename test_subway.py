import pytest, copy, collections
from subway import SubwaySystem
from line import SubwayLine
from station import SubwayStation

# add_train_line requires a name
def test_add_train_line_expects_name():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.add_train_line(["Station 1", "Station 2"])

def test_add_train_line_expects_stations_to_be_nonempty_list():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.add_train_line(line_name="The Missing Line")
    with pytest.raises(AssertionError):
        subway_system.add_train_line(stations=4, line_name="The Surrealist Line")

    with pytest.raises(AssertionError):
        subway_system.add_train_line([], line_name="The Shortest Line")

    subway_system.add_train_line(["Station 1", "Station 2"], line_name="A Short Line")

def test_add_train_line_returns_none():
    subway_system = SubwaySystem()
    assert subway_system.add_train_line(["Station 1", "Station 2"], line_name="A Short Line") is None

def test_subway_systems_have_stations():
    subway_system = SubwaySystem()
    assert subway_system._stations is not None

def test_subway_system_stations_are_unique():
    subway_system = SubwaySystem()
    subway_system.add_train_line(['14th'], '1')
    old_subway_system_stations = copy.deepcopy(subway_system._stations)
    subway_system.add_train_line(['14th'], 'E')
    assert len(subway_system._stations) == len(old_subway_system_stations)


def test_subway_system_add_new_train_line():
    subway_system = SubwaySystem()
    assert len(subway_system.stations_in_system()) == 0
    subway_system.add_train_line(['14th'], '1')
    assert len(subway_system.stations_in_system()) > 0

def test_subway_system_has_lines():
    subway_system = SubwaySystem()
    assert subway_system._lines is not None

def test_subway_system_has_stations():
    subway_system = SubwaySystem()
    assert subway_system._stations is not None
