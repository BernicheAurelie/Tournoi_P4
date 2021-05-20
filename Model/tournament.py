#! Python3
# coding: utf-8

from datetime import datetime


class Tournament:
    def __init__(self, name, place, start, end, time_control):
        self.name = name
        self.place = place
        self.start = start
        self.end = "On going" # self.register_end_time()
        self.time_control = time_control
        self.players = list()
        self.rounds = list()

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def print_end_tournament_info(self):
        print(f"***** fin du tournoi: {self.end} ***** \n")

    def register_end_time(self): 
        end = datetime.now()
        self.end = end.strftime("%m/%d/%Y, %H:%M:%S")
        print(f"***** fin du tournoi: {self.end} ***** \n")

    # def register_end_time(self):
    #     self.end = datetime.now()

    def serialize(self):
        serialized_tournament = {"name": self.name, "place": self.place, 
        "start": self.start, "end": self.end, 
        "time_control": self.time_control, "players": [player.serialize() for player in self.players], 
        "rounds": [round.serialize() for round in self.rounds]
        }
        return serialized_tournament
        # tournaments = list()
        # tournaments.append(serialized_tournament)
        # return tournaments
