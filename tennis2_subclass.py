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
      self.score_text_dict = game.score_text_dict

  def handle_state(self):
    pass

class WinnerState(GameState):
  def player1_is_winner(self):
    return self.player1.point() > self.player2.point()

  def player2_is_winner(self):
    return self.player2.point() > self.player1.point()

  def handle_state(self):
    if self.player1_is_winner():
      return "Win for " + self.player1.name()
    if self.player2_is_winner():
      return "Win for " + self.player2.name()

class AdvantageState(GameState):
  def player1_is_advantage(self):
    return self.player1.point() > self.player2.point()

  def player2_is_advantage(self):
    return self.player2.point() > self.player1.point()

  def handle_state(self):
    if self.player1_is_advantage():
      return "Advantage " + self.player1.name()
    elif self.player2_is_advantage():
      return "Advantage " + self.player2.name()

class EqualState(GameState):
  def is_not_matchpoint(self):
    return self.player1.point() < 3

  def handle_state(self):
    if self.is_not_matchpoint():
      return self.score_text_dict[self.player1.point()] + "-All"
    return "Deuce"

class OneSidedState(GameState):
  def handle_state(self):
      return self.score_text_dict[self.player1.point()] + "-" + self.score_text_dict[self.player2.point()]
