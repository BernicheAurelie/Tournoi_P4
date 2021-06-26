#! Python3
# coding: utf-8


from Model.utils import register_time


class Tournament:
    """Class define with several informations and methods to append players and rounds lists
    and serialize a tournament"""

    def __init__(self, name, place, start, end, time_control):
        """Define with some informations, a players' list and a rounds' list"""
        self.name = name
        self.place = place
        self.start = start
        self.end = "On going"
        self.time_control = time_control
        self.players = list()
        self.rounds = list()

    def add_player(self, player):
        """Add a player to the tournament's players' list"""
        self.players.append(player)

    def add_round(self, round):
        """Add a round to the tournament's rounds' list"""
        self.rounds.append(round)

    def register_end_time(self):
        """Use utils functions and print tournament's end"""
        self.end = register_time()
        print(f"Tournament's End: {self.end}\n")

    def serialize(self):
        """Create a dictionary to serialize a tournament"""
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "start": self.start,
            "end": self.end,
            "time_control": self.time_control,
            "players": [player.serialize() for player in self.players],
            "rounds": [round.serialize() for round in self.rounds],
        }
        return serialized_tournament
