#! Python3
# coding: utf-8

from View.player_view import get_player_elo, get_player_name
from tinydb import TinyDB, Query, where

class PlayerController:

    def __init__(self) -> None:
        self.name = get_player_name()

    def modify_elo(self):
        db = TinyDB("players.json", indent=4)
        players_table = db.table("players")
        Player = Query()
        # choiced_name = get_new_information()
        elo = get_player_elo()
        try:
            players_table.update({"elo" : elo}, Player.name == self.name)
        except:
            print("player not found")