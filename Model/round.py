#! env/bin/script Python 3
# coding utf-8

from Model.match import Match
from datetime import datetime


class Round:
    def __init__(self, number):
        self.number = number
        self.start = self.register_start_time()
        self.end = self.register_end_time()
        self.matchs = list()

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        player1.opponents.append(player2.id_player)
        player2.opponents.append(player1.id_player)
        self.matchs.append(match)

    def add_reload_match(self, match):
        self.matchs.append(match)

    def register_start_time(self):
        start = datetime.now()
        self.start = start.strftime("%m/%d/%Y, %H:%M:%S")
        return self.start

    def register_end_time(self):
        end = datetime.now()
        self.end = end.strftime("%m/%d/%Y, %H:%M:%S")
        return self.end

    def print_start_round_info(self):
        print(f"Round: {self.number}\nDébut du round: {self.start}\n")
    
    def print_end_round_info(self):
        print(f"Fin du round: {self.end}\n")

    def serialize(self):
        serialized_round = {"number": self.number, "start": self.start, 
        "end": self.end, "matchs": [match.serialize() for match in self.matchs]
        }
        return serialized_round