#! Python3
# coding utf-8

from datetime import datetime
from tinydb import TinyDB, Query, where
import json
from Model.tournament import Tournament
from Model.player import Player
from Model.match import Match
from Model.round import Round
from Model.utils import register_end_time
from View.tournament_view import (
    get_tournament_name,
    get_tournament_place,
    get_tournament_start,
    get_tournament_time_control,
    get_user_choice,
)
from View.player_view import (
    get_player_birthday,
    get_player_elo,
    get_player_first_name,
    get_player_gender,
    get_player_name,
)
from View.round_view import enter_score


# players = [
#     Player("BERNICHE", "AURELIE", "09/07/1981", "F", 10), Player("DUPRE", "JEAN MICHEL", "08/31/1951", "M", 60),
#     Player("HARNICHARD", "JOCELYNE", "09/27/1954", "F", 50), Player("DUPONT", "VIRGINIE", "06/03/1975", "F", 20),
#     Player("HUBERT", "JEAN NICOLAS", "10/25/1979", "M", 30), Player("ANDRE", "FREDERIC", "02/12/74", "M", 40),
#     Player("CARPENTIER", "MELANIE", "01/15/78", "F", 70), Player("BOURIENNE", "VALENTIN", "09/04/2002", "M", 80)
# ]


class tournamentControler:
    def __init__(self):
        self.tournament=None

    def start(self):
        name = get_tournament_name()
        place = get_tournament_place()
        start = get_tournament_start()
        end = "On Going" #self.register_end_time() généré au début!
        time_control = get_tournament_time_control()
        self.tournament = Tournament(name, place, start, end, time_control)


    def new_tournament(self):
        self.start()
        self.enter_players()
        self.run_first_round()
        for i in range(2, 5):
            self.run_round(i)
        self.register_end_time()
        self.print_end_tournament()
        self.print_players_score()
        self.serialized_players()
        self.serialized_tournament()

    def reload_tournament(self):
        db = TinyDB('tournaments.json')
        tournaments_table = db.table('tournaments')
        tournaments=tournaments_table.all()
        query = Query()
        # if len(tournaments[i]["rounds"]) < 4:
        for i in range(len(tournaments)):
            print(tournaments[i]["name"])
            print("Rounds number done: ", len(tournaments[i]["rounds"]))
        name = get_user_choice()
        reload_tournament = tournaments_table.search(where("name")==name)
        for tournament in reload_tournament:
            self.deserializer(tournament)
            print(len(tournament["rounds"]))
            if len(tournament["rounds"]) == 0:
                print("condition pour le 1er round")
                print(len(tournament["rounds"]))
                self.run_first_round()
                for lefted_round in range(2,5):
                    self.run_round(lefted_round)
            else:
                for lefted_round in range(len(tournament["rounds"])+1, 5):
                    self.run_round(lefted_round)
            tournaments_table.remove(query.name == tournament["name"])
            self.register_end_time()
            self.print_end_tournament()
            self.print_players_score()
            # if nom existant on remove
            # elif
            self.serialized_players()
            self.serialized_tournament()
        

    def report_tournament(self):
        db = TinyDB('tournaments.json')
        tournaments_table = db.table('tournaments')
        tournaments=tournaments_table.all()
        for i in range(len(tournaments)):
            print(tournaments[i]["name"])
            print("Rounds number done: ", len(tournaments[i]["rounds"]))
            self.deserializer(tournaments[i])
            self.print_end_tournament()
            self.print_players_score()


    def register_end_time(self): # pourquoi je ne peux pas utiliser utils!!
        self.tournament.register_end_time()


    def enter_players(self):
        for i in range(8):
            name = get_player_name()
            first_name = get_player_first_name()
            birthday = get_player_birthday()
            gender = get_player_gender()
            elo = get_player_elo()
            player = Player(name, first_name, birthday, gender, elo)
            self.tournament.add_player(player)
        # self.tournament.players = players


    def run_first_round(self):
        self.tournament.players.sort(key=lambda x: x.elo)
        round = Round("1")
        round.print_start_round_info()
        self.tournament.add_round(round)
        for i in range(4):
            player1 = self.tournament.players[i]
            player2 = self.tournament.players[4 + i]
            round.add_match(player1, player2)

        for match in self.tournament.rounds[0].matchs:
            self.__handle_score(match)
        
        round.print_end_round_info()

        #register_end_time(round)
        
    def get_players_for_round(self):
        next_round_players = list()
        for player in self.tournament.players:
            next_round_players.append(player)
        next_round_players.sort(key=lambda x: x.elo)  # elo
        next_round_players.sort(reverse=True, key=lambda x: x.score)  # score
        return next_round_players

    def run_round(self, round_number):
        i = 0
        print(len(self.tournament.rounds))
        round = Round(round_number)
        round.print_start_round_info()
        next_round_players = self.get_players_for_round()
        self.tournament.add_round(round)
        while len(next_round_players) > 0:
            player1 = next_round_players[i]
            player1_index = i
            player2 = next_round_players[i + 1]
            player2_index = i + 1

            while player2.id_player in player1.opponents:
                try:
                    i += 1
                    player2 = next_round_players[i + 1]
                    player2_index = i + 1
                except IndexError:
                    player2 = next_round_players[1]
                    player2_index = 1
                    break 
            round.add_match(player1, player2)
            del next_round_players[player1_index]
            del next_round_players[player2_index-1]
            i = 0

        for match in self.tournament.rounds[round_number -1].matchs:
            self.__handle_score(match)
        
        round.print_end_round_info()


    def __handle_score(self, match):
        score = enter_score(match)
        while score != "1" and score != "2" and score != "3":
            score = enter_score(match)
        if score == "1":
            match.score_player1 += 1
            match.player1.score += 1
        elif score == "2":
            match.score_player2 += 1
            match.player2.score += 1
        else:
            match.score_player1 += 0.5
            match.player1.score += 0.5
            match.score_player2 += 0.5
            match.player2.score += 0.5

    def print_players_score(self):
        for player in self.tournament.players:
            player.print_score()
            player.print_opponents()
    
    def print_end_tournament(self):
        self.tournament.print_end_tournament_info()

    def serialized_players(self):
        db = TinyDB("players.json", indent=4) # crée un fichier json vide
        players_table = db.table("players")
        query = Query()
        for player in self.tournament.players: #self.tournament.players:
            # players_table.remove(query.name == player["name"])
            players_table.insert(player.serialize())

    def serialized_tournament(self):
        db = TinyDB("tournaments.json", indent=4)
        tournaments_table = db.table("tournaments")
        tournaments_table.insert(self.tournament.serialize())

    def get_player(self, name, first_name, birthday, gender, elo):
        for player in self.tournament.players:
            if player.name == name and player.first_name == first_name \
                and player.birthday == birthday and player.gender == gender \
                and player.elo == elo:
                return player

    def deserializer(self, tournament):
        self.tournament=Tournament(name=tournament['name'], place=tournament['place'], 
                        start=tournament['start'], end=tournament['end'],
                        time_control=tournament['time_control']
            )
        for player in tournament["players"]:
            new_player = Player(player['name'], player['first_name'],
                        player['birthday'], player['gender'], 
                        player['Elo_rating']
            )
            new_player.set_score(player['score'])
            new_player.set_opponents(player['opponents'])
            self.tournament.add_player(new_player)
        
        for round in tournament["rounds"]:
            new_round = Round(round["number"])
            for match in round["matchs"]:
                player1 = self.get_player(match['player1']['name'], match['player1']['first_name'],
                        match['player1']['birthday'], match['player1']['gender'],
                        match['player1']['Elo_rating']
                )
                player2= self.get_player(match['player2']['name'], match['player2']['first_name'],
                        match['player2']['birthday'], match['player2']['gender'],
                        match['player2']['Elo_rating']
                )
                new_match = Match(player1, player2)
                new_match.set_score(match['score_player1'], match['score_player2'])
                new_round.add_reload_match(new_match)
            self.tournament.add_round(new_round)


    # def serialized_matchs(self):
    #     db = TinyDB("matchs.json")
    #     matchs_table = db.table("matchs")
    #     matchs_table.truncate()
    #     # for i in range(1, 5):
    #     for match in self.tournament.rounds[0].matchs:
    #         matchs_table.insert(match.serialize())

    # def serialized_matchs(self):
    #     db = TinyDB("matchs_player.json")
    #     matchs_table = db.table("matchs_player")
    #     matchs_table.truncate()
    #     for i in range(0, 4):
    #         for match in self.tournament.rounds[i].matchs:
    #             print(match.serialize())



    # def serialized_matchs(self):
    #     with open("round_1_matchs_player.json", "w+") as write_file:
    #         for i in range(0, 4):
    #             for match in self.tournament.rounds[i].matchs:
    #                 json.dump(match.player1.serialize(), write_file)
    #                 json.dump(match.player2.serialize(), write_file)
    # 
    #     def serialized_rounds(self):
        # db = TinyDB("rounds.json")
        # rounds_table = db.table("rounds")
        # rounds_table.truncate()
        # for round in self.tournament.rounds:
        #     rounds_table.insert(round.serialize())       
        #for tournament in self.tournaments:
        #     tournament_table.insert(rounds.serialize())
        #     tournament_table.insert(matchs.serialize())

    """     def reload_tournament(self):
        db = TinyDB('tournaments.json')
        tournaments_table = db.table('tournaments')
        tournaments=tournaments_table.all()
        for i in range(len(tournaments)):
            print(tournaments[i]["name"])
            print(len(tournaments[i]["rounds"]))
            if len(tournaments[i]["rounds"]) < 4:
            #input() #choix du tournoi a reprendre
                self.deserializer(tournaments[i])
                print(len(tournaments[i]["rounds"]))
                if len(tournaments[i]["rounds"]) == 0:
                    print("condition pour le 1er round")
                    print(len(tournaments[i]["rounds"]))
                    self.run_first_round()
                    for lefted_round in range(2,5):
                        self.run_round(lefted_round)
                else:
                    for lefted_round in range(len(tournaments[i]["rounds"])+1, 5):
                        self.run_round(lefted_round)
                #remove tinydb tournament == tournaments[i]["name"]
                tournoi=Query()
                tournaments_table.remove(tournoi.name == tournaments[i]["name"])
                self.register_end_time()
                self.print_end_tournament()
                self.print_players_score()
                # if nom existant on remove
                # elif
                self.serialized_players()
                self.serialized_tournament() """