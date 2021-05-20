#! Python3
# coding utf-8

from Model.tournament import Tournament
from Controler.tournament_controler import tournamentControler
from tinydb import TinyDB, Query, where
#from Model.utils import register_end_time

if __name__ == "__main__":
    tournament = tournamentControler()
    tournament.enter_players()
    tournament.run_first_round()
    for i in range(2, 5):
        tournament.run_round(i)
    Tournament.register_end_time(tournament)
    #Tournament.print_end_tournament_info(tournament)
    tournament.print_players_score()
    tournament.serialized_players()
    tournament.serialized_tournament()
    #tournament.serialized_rounds()
    

