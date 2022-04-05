from player_subclass import Player

class GameState:
  def __init__(self, game):
      self.player1Name = game.player1Name
      self.player2Name = game.player2Name
      self.p1points = game.p1points
      self.p2points = game.p2points

      self.player1 = Player(game.player1Name, game.p1points)
      self.player2 = Player(game.player2Name, game.p2points)

  def generate_score_text(self):
      pass

class AdvantageState(GameState):
  def generate_score_text(self):
      return "Advantage " + self.player1.get_name() if self.player1.get_point() > self.player2.get_point() else "Advantage " + self.player2.get_name()

class WonState(GameState):
  def generate_score_text(self):
      return "Win for " + self.player1Name if self.p1points > self.p2points else "Win for " + self.player2Name

class EqualState(GameState):
  def generate_score_text(self):
      return {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")

class NormalState(GameState):
  def generate_score_text(self):
      score_dict = {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }
      return score_dict[self.p1points] + "-" + score_dict[self.p2points]