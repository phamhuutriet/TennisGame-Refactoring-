from player_subclass import Player

class GameState:
  def __init__(self, game):
      self.player1 = game.player1
      self.player2 = game.player2

  def generate_score_text(self):
      pass

class AdvantageState(GameState):
  def generate_score_text(self):
      return "Advantage " + self.player1.name() if self.player1.point() > self.player2.point() else "Advantage " + self.player2.name()

class WonState(GameState):
  def generate_score_text(self):
      return "Win for " + self.player1.name() if self.player1.point() > self.player2.point() else "Win for " + self.player2.name()

class EqualState(GameState):
  def generate_score_text(self):
      return {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.player1.point(), "Deuce")

class NormalState(GameState):
  def generate_score_text(self):
      score_dict = {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }
      return score_dict[self.player1.point()] + "-" + score_dict[self.player2.point()]