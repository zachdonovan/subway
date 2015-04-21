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
        assert kwargs.get('from', False), "take_train requires a 'from' keyword argument"
        assert kwargs.get('to', False), "take_train requires a 'to' keyword argument"
        origin = kwargs['from']
        destination = kwargs['to']

        start_station = self._stations.get(origin, None)
        end_station = self._stations.get(destination, None)

        assert start_station, "take_train requires an origin point within the existing subway system"
        assert end_station, "take_train requires an end point within the existing subway system"

        queue = [start_station]
        paths = { origin: [] }
        discovered = { origin: True }
        while len(queue):
            next_station = queue.pop()
            next_station_name = next_station.get_name()
            print("next station is {}".format(next_station))

            discovered[next_station_name] = True                              # don't visit this station again
            path_to_station = paths[next_station_name] + [next_station_name]  # add this station to the path for all subsequent stations
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
        station = self._stations.get(station_name, SubwayStation(name=station_name))
        for neighbor in neighbors:
            station.set_neighbor(neighbor)
        self._stations[station_name] = station

    def stations_in_system(self):
        return self._stations.items()
