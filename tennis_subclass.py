class GameState:
  def __init__(self, player1Name, player2Name, p1points, p2points):
      self.player1Name = player1Name
      self.player2Name = player2Name
      self.p1points = p1points
      self.p2points = p2points

  def generate_score_text(self):
      pass

class AdvantageState(GameState):
  def generate_score_text(self):
      return "Advantage " + self.player1Name if self.p1points > self.p2points else "Advantage " + self.player2Name

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