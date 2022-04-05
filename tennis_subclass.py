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