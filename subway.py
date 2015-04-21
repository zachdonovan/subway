import collections
from station import SubwayStation

class SubwaySystem(object):
    def __init__(self, *args, **kwargs):
        self._stations = collections.defaultdict(SubwayStation)

    def add_train_line(self, stations, line_name):
        assert isinstance(stations, list)
        assert len(stations)

        for index, station in enumerate(stations):
          neighbors = []
          if index > 0:
              neighbors.append(stations[index-1])
          if index < len(stations) - 1:
              neighbors.append(stations[index+1])
          self._add_station(station, neighbors)

    def take_train(self, origin, destination):
        start_station = self._stations[origin]
        end_station = self._stations[destination]
        queue = [start_station]
        paths = { origin: [] }
        discovered = { origin: True }
        while len(queue):
            next_station = queue.pop()
            next_station_name = next_station.get_name()
            print("next station is {}".format(next_station))

            discovered[next_station_name] = True                         # don't visit this station again
            path_to_station = paths[next_station_name] + [next_station]  # add this station to the path for all subsequent stations
            if next_station == end_station:
                print("we're done here")                
                return path_to_station # current station is our destination

            for tup in next_station.get_neighbors():
                neighbor, distance = tup
                if discovered.get(neighbor, False):
                    continue # we've already visited this station 
                paths[neighbor] = path_to_station
                queue.append(self._stations[neighbor])
                print("queue is now {}".format(queue))

        return []


    def _add_station(self, station_name, neighbors):
        station = self._stations[station_name]
        station.set_name(station_name)
        for neighbor in neighbors:
            station.add_neighbor(neighbor)

    def stations_in_system(self):
        return self._stations.values()
