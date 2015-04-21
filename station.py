class SubwayStation(object):
    def __init__(self, *args, **kwargs):
        self._neighbors = {}
        self._name = kwargs.get('name', "")

    def __repr__(self):
        return self._name

    def set_neighbor(self, neighbor, distance=None):
        distances = filter(lambda dist: dist is not None, [self._neighbors.get(neighbor, None), distance])
        self._neighbors[neighbor] = min(distances) if distances else None

    def get_neighbors(self):
        return [ (k,v) for k, v in self._neighbors.items() ]

    def set_name(self, station_name):
        self._name = station_name

    def get_name(self):
        return self._name
