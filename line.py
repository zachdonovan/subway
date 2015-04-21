class SubwayLine(object):
  def __init__(self, *args, **kwargs):
    self._stations = []

  def add_station(self, station):
    self._stations.append(station)
