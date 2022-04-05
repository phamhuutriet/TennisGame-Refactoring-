from player_subclass import Player

class GameState:
  def __init__(self, game, player1, player2):
      self.player1 = player1
      self.player2 = player2

  def generate_score_text(self):
      pass

class AdvantageState(GameState):
  def generate_score_text(self):
      return "Advantage " + self.player1.get_name() if self.player1.get_point() > self.player2.get_point() else "Advantage " + self.player2.get_name()

class WonState(GameState):
  def generate_score_text(self):
      return "Win for " + self.player1.get_name() if self.player1.get_point() > self.player2.get_point() else "Win for " + self.player2.get_name()

class EqualState(GameState):
  def generate_score_text(self):
      return {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.player1.get_point(), "Deuce")

class NormalState(GameState):
  def generate_score_text(self):
      score_dict = {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }
      return score_dict[self.player1.get_point()] + "-" + score_dict[self.player2.get_point()]