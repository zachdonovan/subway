class SubwayStation(object):
    def __init__(self, *args, **kwargs):
        self._neighbors = {}
        self._name = kwargs.get('name', "")

    def __repr__(self):
        return self._name

    def set_neighbor(self, neighbor, distance=1):
        distances = filter(lambda val: val is not None, [self._neighbors.get(neighbor, None), distance])
        self._neighbors[neighbor] = min(distances)

    def get_neighbors(self):
        return list(self._neighbors.items())

    def set_name(self, station_name):
        self._name = station_name

    def get_name(self):
        return self._name


    # support comparison of stations

    def __lt__(self, other):
        return self._name < other._name

    def __gt__(self, other):
        return self._name > other._name

    def __eq__(self, other):
        return self._name == other._name

    def __le__(self, other):
        return self._name <= other._name

    def __ge__(self, other):
        return self._name >= other._name

    def __ne__(self, other):
        return self._name != other._name
