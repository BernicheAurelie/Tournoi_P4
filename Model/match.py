#! env/bin/script Python 3
# coding utf-8


class Match:
    """Class Match define with two players and methods
    to update score and to serialization"""

    def __init__(self, player1, player2):
        """Define with two players and a score to zero by default"""
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def set_score(self, score_player1, score_player2):
        """Update players' score at the deserialization"""
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def serialize(self):
        """Create a dictionary to serialize a match"""
        serialized_match = {
            "player1": self.player1.serialize(),
            "player2": self.player2.serialize(),
            "score_player1": self.score_player1,
            "score_player2": self.score_player2,
        }
        return serialized_match
