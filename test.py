from tennis import TennisGame2
from tennis2_subclass import *

def play_game(TennisGame, p1Points, p2Points, p1Name, p2Name):
    game = TennisGame(p1Name, p2Name)
    for i in range(max(p1Points, p2Points)):
        if i < p1Points:
            game.won_point(p1Name)
        if i < p2Points:
            game.won_point(p2Name)
    return game

testcase = (3, 3, "Deuce", 'player1', 'player2')
(p1Points, p2Points, score, p1Name, p2Name) = testcase
game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
print(game.score())
