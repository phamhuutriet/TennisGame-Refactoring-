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
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

        self.score_text_dict = {
          0: "Love",
          1: "Fifteen",
          2: "Thirty",
          3: "Forty"
        }

        self.player1 = tennis2.Player(player1Name)
        self.player2 = tennis2.Player(player2Name)
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
  
    def is_not_matchpoint(self):
      return self.player1.point() < 3

    def is_equal_score(self):
      return self.player1.point() == self.player2.point()
    
    def handle_equal(self):
      if self.is_not_matchpoint():
          return self.score_text_dict[self.player1.point()] + "-All"
      return "Deuce"

    def is_onesided_score_player1(self):
      return self.p1points > 0 and self.p2points == 0

    def is_onesided_score_player2(self):
      return self.p2points > 0 and self.p1points == 0

    def is_onesided_score(self):
      return self.is_onesided_score_player1() or self.is_onesided_score_player2()

    def handle_onesided_score(self):
      P1res = P2res = ""
      if self.player1.point() <= 3:
        P1res = self.score_text_dict[self.player1.point()]
      if self.player2.point() <= 3:
        P2res = self.score_text_dict[self.player2.point()]
      return P1res + "-" + P2res

    def is_normal_score(self):
      return (self.p1points>self.p2points and self.p1points < 4) or (self.p2points>self.p1points and self.p2points < 4)

    def handle_normal(self):
      return self.score_text_dict[self.player1.point()] + "-" + self.score_text_dict[self.player2.point()]

    def player1_is_advantage(self):
      return self.p1points > self.p2points and self.p2points >= 3

    def player2_is_advantage(self):
      return self.p2points > self.p1points and self.p1points >= 3

    def is_advantage_score(self):
      return self.player1_is_advantage() or self.player2_is_advantage()

    def handle_advantage(self):
      if self.player1_is_advantage():
        return "Advantage " + self.player1.name()
      elif self.player2_is_advantage():
        return "Advantage " + self.player2.name()

    def player1_is_winner(self):
      return self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2

    def player2_is_winner(self):
      return self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2

    def is_win_score(self):
      return self.player1_is_winner() or self.player2_is_winner()

    def score(self):
        result = ""
        P1res = ""
        P2res = ""
        # Equal score state but it's not passed the matchpoint
        if self.is_equal_score():
          result = self.handle_equal()
        
        # One-sided score on player1 side
        elif self.is_onesided_score():
          result = self.handle_onesided_score()
        
        # Non-zero score on player1 side
        elif self.is_normal_score():
          result = self.handle_normal()
        
        # Advantage state
        elif self.is_advantage_score():
          result = self.handle_advantage()
        
        # Win state
        if self.is_win_score():
          if self.player1_is_winner():
              result = "Win for " + self.player1Name
          if self.player2_is_winner():
              result = "Win for " + self.player2Name
        return result
    
    def P1Score(self):
        self.p1points +=1
        self.player1.set_point(self.player1.point() + 1)
    
    def P2Score(self):
        self.p2points +=1
        self.player2.set_point(self.player2.point() + 1)

        
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