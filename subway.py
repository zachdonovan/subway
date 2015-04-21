from station import SubwayStation

class SubwaySystem(object):
    def __init__(self, *args, **kwargs):
        self._stations = {}

    def add_train_line(self, stops, name, time_between_stations=None):
        assert isinstance(stops, list)
        assert len(stops)

        for index, stop in enumerate(stops):
          neighbors = []
          if index > 0:
              neighbors.append(stops[index-1])
          if index < len(stops) - 1:
              neighbors.append(stops[index+1])
          self._add_station(stop, neighbors)

    def take_train(self, **kwargs):
        # this nonsense is required to support from as a keyword argument
        assert kwargs.get('from', False), "take_train requires a 'from' keyword argument"
        assert kwargs.get('to', False), "take_train requires a 'to' keyword argument"
        origin = kwargs['from']
        destination = kwargs['to']

        start_station = self._stations.get(origin, None)
        end_station = self._stations.get(destination, None)

        assert start_station, "take_train requires an origin point within the existing subway system"
        assert end_station, "take_train requires an end point within the existing subway system"


        # A Basic Bread-First Search

        queue = [start_station]                                               # prime the queue with the first station
        paths = { origin: [] }                                                # insert the start station into the list of candidate paths
        discovered = { origin: True }                                         # mark the start station as discovered

        while len(queue):                                                     # while we have unvisited stations
            next_station = queue.pop()                                        # visit the next station
            next_station_name = next_station.get_name()                       # extract the station's unique identifier

            discovered[next_station_name] = True                              # don't visit this station again
            path_to_station = paths[next_station_name] + [next_station_name]  # add this station to the path for all subsequent stations
            if next_station == end_station:                                   # if we're at the destination
                return path_to_station                                        # return path to this station

            for tup in next_station.get_neighbors():                          # get adjacent stations for exploration
                neighbor, distance = tup
                if discovered.get(neighbor, False):                           # unless we've already visited them
                    continue
                paths[neighbor] = path_to_station                             # set their paths to match the current station
                queue.append(self._stations[neighbor])                        # enqueue!

        return []                                                             # fail case - no route found


    def _add_station(self, station_name, neighbors):
        station = self._stations.get(station_name, SubwayStation(name=station_name))
        for neighbor in neighbors:
            station.set_neighbor(neighbor)
        self._stations[station_name] = station

    def stations_in_system(self):
        return self._stations.items()
