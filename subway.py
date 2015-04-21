import collections
from line import SubwayLine
from station import SubwayStation

class SubwaySystem(object):
    def __init__(self, *args, **kwargs):
        self._stations = collections.defaultdict(SubwayStation)
        self._lines = collections.defaultdict(SubwayLine) 

    def add_train_line(self, stations, line_name):
        assert isinstance(line_name, str)
        assert isinstance(stations, list)
        assert len(line_name)
        assert len(stations)

        for index, station in enumerate(stations):
          self._add_station(station, [stations[index-1], stations[index+1]], line_name)

    def take_train(self, origin, destination):
        start_station = self._stations[origin]
        end_station = self._stations[destination]
        queue = [start_station]
        paths = { origin: [start_station] }
        discovered = { origin: True }
        while len(queue):
            next_station = queue.pop()
            next_station_name = next_station.get_name()

            discovered[next_station_name] = True                         # don't visit this station again
            path_to_station = paths[next_station_name] + [next_station]  # add this station to the path for all subsequent stations
            if next_station == end_station:
                return path_to_station # current station is our destination

            for neighbor in next_station.get_neighbors():
                if discovered.get(next_station_name, False):
                    continue # we've already visited this station 
                paths[neighbor.get_name()] = path_to_station

            # check all adjacent stations
            queue = queue + next_station.get_neighbors()

        return []


    def _add_station(self, station_name, neighbors, line_name):
        station = self._stations[station_name]
        station.set_name(station_name)
        station.add_line(line_name)
        for neighbor in neighbors:
            station.add_neighbor(neighbor)
        self._lines[line_name].add_station(station)

    def stations_in_system(self):
        return self._stations.values()

    def lines_in_system(self):
        return self._lines.values()
