class Player:
  def __init__(self, playerName, point):
    self._playerName = playerName
    self._point = point

  def name(self):
    return self._playerName
  
  def point(self):
    return self._point

  def set_point(self, new_point):
    self._point = new_point