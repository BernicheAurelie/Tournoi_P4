#! Python3
# coding: utf-8

"""get choices from views to print reports (and players?)"""

from tinydb import TinyDB, Query, where
from Controler.tournament_controler import tournamentControler
from View.tournament_view import get_user_choice


class ReportController:

    def report_tournament(self):
        db = TinyDB('tournaments.json')
        tournaments_table = db.table('tournaments')
        tournaments=tournaments_table.all()
        query = Query()
        for i in range(len(tournaments)):
            print(tournaments[i]["name"])
        name = get_user_choice()
        reload_tournament = tournaments_table.search(where("name")==name)
        tournament = reload_tournament[0]
        # report = tournamentControler()
        # report.deserializer(tournament)
        # report.print_players_score()
        print("lieu du tournoi: \n", tournament["place"])
        print("gestion du temps: \n", tournament["time_control"])
        print("début du tournoi: \n", tournament["start"])
        print("Fin du tournoi: \n", tournament["end"])
        print("joueurs du tournoi:\n", tournament["players"])
        
        # for i in range(len(tournaments)):
        #     print(tournaments[i]["name"])
        #     self.deserializer(tournaments[i])
        #     self.tournament.print_end_tournament_info()
        #     self.print_players_score()
        #     print(tournaments[i]["end"])
        #     print(tournaments[i]["players"])

#     def players_alphabetic_order(self):
#         db = TinyDB("players.json", indent=4) # crée un fichier json vide
#         players_table = db.table("players")
#         serialized_players = players_table.all()
#         players = list()
#         for player in serialized_players:
#             new_player = Player(player['name'], player['first_name'],
#                             player['birthday'], player['gender'], 
#                             player['elo'])
#             players.append(new_player)
#         players.sort(key=lambda x: x.name) # (, x.first_name)
#         for i in players:
#             print("****************************\n", i)

