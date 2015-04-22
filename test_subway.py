import pytest, copy, collections
from subway import SubwaySystem
from station import SubwayStation

#########################
# add_train_line contract
#########################

def test_add_train_line_expects_name():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.add_train_line(["Station 1", "Station 2"])

def test_add_train_line_expects_stations_to_be_nonempty_list():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.add_train_line(name="The Missing Line")
    with pytest.raises(AssertionError):
        subway_system.add_train_line(stops=4, name="The Surrealist Line")

    with pytest.raises(AssertionError):
        subway_system.add_train_line([], name="The Shortest Line")

    subway_system.add_train_line(["Station 1", "Station 2"], name="A Short Line")

def test_add_train_line_returns_none():
    subway_system = SubwaySystem()
    assert subway_system.add_train_line(["Station 1", "Station 2"], name="A Short Line") is None

def test_subway_system_add_new_train_line():
    subway_system = SubwaySystem()
    assert len(subway_system.stations_in_system()) == 0
    subway_system.add_train_line(['14th'], '1')
    assert len(subway_system.stations_in_system()) > 0

#####################
# take_train contract
#####################

def test_take_train_requires_origin():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.take_train(destination="125th")

def test_take_train_requires_destination():
    subway_system = SubwaySystem()
    with pytest.raises(TypeError):
        subway_system.take_train(origin="125th")

def test_take_train_nonsense_trip_returns_empty_path():
    subway_system = SubwaySystem()
    with pytest.raises(AssertionError):
        subway_system.take_train(origin="14th", destination = "Franklin St")
    subway_system.add_train_line(stops=["West 4th", "14th", "34th", "42nd - Port Authority"], name="A")
    subway_system.add_train_line(stops=["Chambers St", "Franklin St", "Canal St", "Houston St"], name="1")
    assert subway_system.take_train(origin="14th", destination="Franklin St") == ([], 0)

def test_take_train_supports_transfers():
    subway_system = SubwaySystem()
    subway_system.add_train_line(stops=["West 4th", "14th", "34th", "42nd - Port Authority"], name="A")
    subway_system.add_train_line(stops=["West 4th", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], name="F")
    assert subway_system.take_train(origin="14th", destination="East Broadway") == (["14th", "West 4th", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], 4)

def test_take_train_survives_cycles():
    subway_system = SubwaySystem()
    subway_system.add_train_line(stops=["West 4th", "14th", "34th", "42nd - Port Authority"], name="A")
    subway_system.add_train_line(stops=["Broadway-Lafayette", "8th St", "14th"], name="6")
    subway_system.add_train_line(stops=["West 4th", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], name="F")
    assert subway_system.take_train(origin="14th", destination= "East Broadway") in [(["14th", "West 4th", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], 4),
                                                                                     (["14th", "8th St", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], 4)]

def test_take_train_respects_time():
    subway_system = SubwaySystem()
    subway_system.add_train_line(stops=["West 4th", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], name="F",
                                time_between_stations=[("West 4th", "Broadway-Lafayette", 2),
                                                       ("Broadway-Lafayette", "2nd Avenue", 2),
                                                       ("2nd Avenue", "East Broadway", 2)])
    subway_system.add_train_line(stops=["West 4th", "THE ALTERNATE DIMENSION",  "East Broadway"], name="X",
                                time_between_stations=[("West 4th", "THE ALTERNATE DIMENSION", 100),
                                                       ("THE ALTERNATE DIMENSION", "East Broadway", 100)])
    assert subway_system.take_train(origin="West 4th", destination="East Broadway") == (["West 4th", "Broadway-Lafayette", "2nd Avenue", "East Broadway"], 6)

#####################
# internal stations data model
#####################

def test_subway_systems_have_stations():
    subway_system = SubwaySystem()
    assert subway_system.stations_in_system() is not None

def test_subway_system_stations_are_unique():
    subway_system = SubwaySystem()
    subway_system.add_train_line(['14th'], '1')
    old_subway_system_stations = copy.deepcopy(subway_system._stations)
    subway_system.add_train_line(['14th'], 'E')
    assert len(subway_system._stations) == len(old_subway_system_stations)
    subway_system.add_train_line(['23rd'], '6')
    assert len(subway_system._stations) > len(old_subway_system_stations)
