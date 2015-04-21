class SubwayStation(object):
    def __init__(self, *args, **kwargs):
        self._neighbors = []
        self._name = ""

    def __repr__(self):
        return self._name

    def add_neighbor(self, neighbor, distance=None):
        self._neighbors.append((neighbor, distance))

    def get_neighbors(self):
        return self._neighbors

    def set_name(self, station_name):
        self._name = station_name

    def get_name(self):
        return self._name
