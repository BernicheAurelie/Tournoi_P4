#! env/bin/script Python 3
# coding utf-8

from Model.utils import register_end_time
from Model.match import Match
from datetime import datetime


class Round:

    def __init__(self, number):
        """Define with a number, a start and an end time
        and a matchs' list"""
        self.number = number
        self.start = self.register_start_time()
        self.end = "On going"
        self.matchs = list()

    def add_match(self, player1, player2):
        """Append matchs' list and player's opponents"""
        match = Match(player1, player2)
        player1.opponents.append(player2.id_player)
        player2.opponents.append(player1.id_player)
        self.matchs.append(match)

    def add_reload_match(self, match):
        """Append matchs' list at the deserialization"""
        self.matchs.append(match)

    def register_start_time(self):
        """Register round's start time and adapts it to the deserialization"""
        start = datetime.now()
        self.start = start.strftime("%m/%d/%Y, %H:%M:%S")
        return self.start

    def register_end_time(self):
        """Use Utils function to register round's end and print it to the user"""
        self.end = register_end_time()
        print(f"Round's End: {self.end}\n")
        return self.end

    def print_start_round_info(self):
        """Print round's start informations"""
        print(f"Round: {self.number}\nRound's Start: {self.start}\n")

    def serialize(self):
        """Create a dictionary to serialize a round"""
        serialized_round = {
            "number": self.number,
            "start": self.start,
            "end": self.end,
            "matchs": [match.serialize() for match in self.matchs],
        }
        return serialized_round
