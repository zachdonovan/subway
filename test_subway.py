import pytest

class SubwaySystem(object):
    def add_train_line(self, stops, name):
        assert isinstance(stops, list)
        assert len(stops)

# add_train_line requires a name
def test_add_train_line_expects_name():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.add_train_line(["Station 1", "Station 2"])

def test_add_train_line_expects_stops_to_be_nonempty_list():
    subway_system = SubwaySystem()
    j
    with pytest.raises(TypeError):
        subway_system.add_train_line(name="The Missing Line")
    with pytest.raises(AssertionError):
        subway_system.add_train_line(stops=4, name="The Surrealist Line")

    with pytest.raises(AssertionError):
        subway_system.add_train_line([], name="The Shortest Line")

    subway_system.add_train_line(["Station 1", "Station 2"], name= "A Short Line")

def test_add_train_line_returns_none():
    subway_system = SubwaySystem()
    assert subway_system.add_train_line(["Station 1", "Station 2"], name="A Short Line") is None


