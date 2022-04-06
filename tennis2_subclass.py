class Player:
  def __init__(self, playerName):
      self._name = playerName
      self._point = 0

  def name(self):
    return self._name
  
  def point(self):
    return self._point

  def set_point(self, point):
    self._point = point