#! Python3
# coding: utf-8

from View.player_view import (
    get_player_elo,
    get_player_first_name,
    get_player_name,
    ReportPlayer,
)
from tinydb import TinyDB, Query


class PlayerController:
    def __init__(self) -> None:
        self.name = get_player_name()
        self.first_name = get_player_first_name()

    def modify_elo(self):
        db = TinyDB("players.json", indent=4)
        players_table = db.table("players")
        Player = Query()
        elo = get_player_elo()
        players_table.update(
            {"elo": int(elo)},
            Player.name == self.name and Player.first_name == self.first_name,
        )
        ReportPlayer.print_modified_player(elo)
