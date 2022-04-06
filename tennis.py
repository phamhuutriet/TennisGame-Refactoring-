from tennis_subclass import *
from player_subclass import Player
import tennis2_subclass as tennis2


class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name, 0)
        self.player2 = Player(player2Name, 0)
        
    def won_point(self, playerName):
        self.increase_point(self.player_factory(playerName))

    def score(self):
        return self.gameState_factory().generate_score_text()
    
    def player_factory(self, playerName):
        return self.player1 if self.player1.name() == playerName else self.player2

    def increase_point(self, player):
        player.set_point(player.point() + 1)

    def is_equal_score(self):
        return self.point_difference() == 0

    def is_match_point(self):
        return self.player1.point()>=4 or self.player2.point()>=4

    def is_advantage(self):
        return self.is_match_point() and self.point_difference() ==1

    def is_won(self):
        return self.is_match_point() and self.point_difference() >= 2

    def point_difference(self):
        return abs(self.player1.point()-self.player2.point())
    
    def gameState_factory(self):
        if self.is_advantage():
          return AdvantageState(self)
        elif self.is_won():
          return WonState(self)
        elif self.is_equal_score():
          return EqualState(self)
        else:
          return NormalState(self)

## END OF TENNIS1GAME ##

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.score_text_dict = {
          0: "Love",
          1: "Fifteen",
          2: "Thirty",
          3: "Forty"
        }

        self.player1 = tennis2.Player(player1Name)
        self.player2 = tennis2.Player(player2Name)
    
    def score(self):
        return self.gamestate_factory().generate_score_text()
        
    def won_point(self, playerName):
        self.increase_point(self.player_factory(playerName))

    def player_factory(self, playerName):
      return self.player1 if self.player1.name() == playerName else self.player2

    def increase_point(self, player):
      player.set_point(player.point() + 1)

    def is_equal_score(self):
      return self.player1.point() == self.player2.point()

    def is_onesided_score(self):
      return self.player1.point() == 0 or self.player2.point() == 0

    def is_advantage_score(self):
      return self.player1.point() >= 3 and self.player2.point() >= 3

    def is_win_score(self):
      score_diff = abs(self.player1.point() - self.player2.point())
      return score_diff >= 2 and (self.player1.point() >= 4 or self.player2.point() >= 4)

    def gamestate_factory(self):
      if self.is_win_score():
        return tennis2.WinnerState(self)
      elif self.is_equal_score():
        return tennis2.EqualState(self)
      elif self.is_advantage_score():
        return tennis2.AdvantageState(self)
      elif self.is_onesided_score():
        return tennis2.OneSidedState(self)
      else:
        return tennis2.NormalState(self)

        
class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1
    
    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s