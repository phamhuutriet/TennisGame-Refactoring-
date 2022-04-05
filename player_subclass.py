class Player:
  def __init__(self, playerName, point):
    self._playerName = playerName
    self._point = point

  def get_name(self):
    return self._playerName

  def get_point(self):
    return self._point