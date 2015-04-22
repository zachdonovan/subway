import Queue
from station import SubwayStation

class SubwaySystem(object):
    def __init__(self, *args, **kwargs):
        self._stations = {}

    def add_train_line(self, stops, name, time_between_stations=None):
        assert isinstance(stops, list)
        assert len(stops)

        if time_between_stations is not None:
            for start, end, dist in time_between_stations:
                self._add_station(start, [(end, dist)])
                self._add_station(end, [(start, dist)])
        else:
            for index, stop in enumerate(stops):
                neighbors = []
                if index > 0:
                    neighbors.append((stops[index-1], 1))
                if index < len(stops) - 1:
                    neighbors.append((stops[index+1], 1))
                self._add_station(stop, neighbors)

    def take_train(self, origin, destination):
        start_station = self._stations.get(origin, None)
        end_station = self._stations.get(destination, None)

        assert start_station, "take_train requires an origin point within the existing subway system"
        assert end_station, "take_train requires an end point within the existing subway system"

        return self._dijkstra(start_station, end_station)


    def _dijkstra(self, start_station, end_station):
        queue = Queue.PriorityQueue()                                         # instantiate an honest-to-god priority queue!
        queue.put((0, start_station), False)                                  # prime the priority queue with the first station
        start_name = start_station.get_name()
        paths = { start_name: [] }                                            # insert the start station into the list of candidate paths
        distance = { start_name: 0 }                                          # distance from origin to itself is zero

        while not queue.empty():                                              # while we have unvisited stations
            next_dist, next_station = queue.get(False)                        # visit the next station
            next_station_name = next_station.get_name()                       # extract the station's unique identifier

            dist_sum = distance[next_station_name]                            # get the recorded distance to this station
            path_to_station = paths[next_station_name] + [next_station_name]  # add this station to the path for all subsequent stations
            if next_station == end_station:                                   # if we're at the destination
                return path_to_station, dist_sum                              # return path to this station and the distance

            for tup in next_station.get_neighbors():                          # get adjacent stations for exploration
                neighbor, dist = tup
                alt = distance.get(neighbor, None)
                if alt is None or (dist + dist_sum) < alt:                    # unless we've already found a better path
                    distance[neighbor] = dist + dist_sum                      # update the best path
                    paths[neighbor] = path_to_station                         # set their paths to match the current station
                    queue.put((dist + dist_sum, 
                      self._stations[neighbor]), False)                       # enqueue!

        return ([], 0)                                                        # fail case - no route found
        
    def _add_station(self, station_name, neighbor_tuples):
        station = self._stations.get(station_name, SubwayStation(name=station_name))
        for neighbor, dist in neighbor_tuples:
            station.set_neighbor(neighbor, dist)
        self._stations[station_name] = station

    def stations_in_system(self):
        return self._stations.items()
