#! env/bin/script Python 3
# coding utf-8

"""tuple de 2 listes (player1, score1) (player2,score2)
    score_gagnant += 1
    score_perdant += 0
    score_egalite += 0.5
"""
import json


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def serialize(self):
        serialized_match = {
        "player1": self.player1.serialize(), "player2": self.player2.serialize(),
        "score_player1": self.score_player1, "score_player2": self.score_player2
        }
        return serialized_match

