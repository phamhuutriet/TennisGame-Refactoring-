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

class GameState:
  def __init__(self, game):
      self.player1 = game.player1
      self.player2 = game.player2

  def handle_state(self):
    pass

class WinnerState(GameState):
  def player1_is_winner(self):
    return self.player1.point() >= 4 and self.player2.point() >= 0 and (self.player1.point()-self.player2.point()) >=2

  def player2_is_winner(self):
    return self.player2.point() >= 4 and self.player1.point() >= 0 and (self.player2.point()-self.player1.point()) >=2

  def handle_state(self):
    if self.player1_is_winner():
      return "Win for " + self.player1.name()
    if self.player2_is_winner():
      return "Win for " + self.player2.name()
