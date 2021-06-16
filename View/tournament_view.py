#! python3
# coding utf-8

from Model.utils import is_date_valid
from Model.player import Player
from tinydb import TinyDB, where


def get_tournament_name():
    name = input("Enter tournament's name : ")
    name = name.upper()
    # while name == "":
    while not name.isalnum():
        print("Please, check your entry.")
        print("Only alpha and numeric lettering")
        name = input("Enter tournament's name : ")
        name = name.upper()
    return name


def get_tournament_place():
    place = input("Enter tournament's place : ")
    place = place.upper()
    while not place.isalnum():
        print("Please, check your entry.")
        print("Only alpha and numeric lettering")
        place = input("Enter tournament's place : ")
    return place


def get_tournament_start():
    start = input("Enter tournament's start date (MM/DD/YYYY) : ")
    while is_date_valid(start) is False:
        print("Incorrect date, enter a date in the format MM/DD/YYYY")
        start = input("Enter tournament's start date (MM/DD/YYYY) : ")
    return start


def get_tournament_time_control():
    time_control = input(
        "Enter speed game shape (Bullet/Blitz/Rapid) : "
    )
    time_control = time_control.lower()
    while (
        time_control != "bullet" and time_control != "blitz" and time_control != "rapid"
    ):
        time_control = input(
            "Enter speed game shape (Bullet/Blitz/Rapid) : "
        )
        time_control = time_control.lower()
    return time_control

def get_confirmation():
    print("Do you want to continue tournament? Yes or No?")
    confirmation = input("Enter Y or N: ")
    confirmation = confirmation.lower()
    while (confirmation != "y" and confirmation != "n"):
        print("Do you want to continue tournament? Yes or No?")
        confirmation = input("Please, enter Y or N:")
        confirmation = confirmation.lower()
    return confirmation


def get_user_choice():    
    print("which tournament do you want to reload?\n")
    choice = input("Please, enter its name: ")
    choice = choice.upper()
    print()
    while not choice.isalnum():
        print("Please, check your entry, see choices above")
        print("which tournament do you want to reload?\n")
        choice = input("Please, enter tournament's name: ")
        choice = choice.upper()
        print()
    return choice

def get_tournaments():
    db = TinyDB('tournaments.json')
    tournaments_table = db.table('tournaments')
    tournaments=tournaments_table.all()
    for i in range(len(tournaments)):
        print(i+1, ") ", tournaments[i]["name"])
        if len(tournaments[i]["rounds"]) < 4:
            print("\t --> lefted rounds : ", (4-len(tournaments[i]["rounds"])))
    print()


class ReportTournament:

    def tournament_info(self):
        db = TinyDB('tournaments.json')
        tournaments_table = db.table('tournaments')
        get_tournaments()
        name = get_user_choice()
        reload_tournament = tournaments_table.search(where("name")==name)
        tournament = reload_tournament[0]
        print("Tournament's place: \n", tournament["place"])
        print("Tournament's time control: \n", tournament["time_control"])
        print("Tournament's start: \n", tournament["start"])
        print("Tournament's end: \n", tournament["end"])

    def tournament_rounds(self, tournament):
        for round in tournament["rounds"]:
            print(f"*************************** ROUND " , round["number"], "*************************** \n")
            print("Start:\t ", round["start"])
            print("End:\t ", round["end"])
            print("======================== MATCHS ======================")
            print()
        self.tournament_matchs(tournament)
        print()

    def tournament_matchs(self, tournament):
        for round in tournament["rounds"]:
            i=1
            for match in round["matchs"]:
                print("--> Match number ", i, "\n")
                print("---------- Player 1 ----------\n")
                if match["score_player1"]==1:
                    print("*** Winner ***\n")
                elif match["score_player1"]==0:
                    print("*** Looser ***\n")
                print("Name:\t " , match["player1"]["name"])
                print("First name:\t " , match["player1"]["first_name"])
                print("Birthday:\t " , match["player1"]["birthday"])
                print("Gender:\t " , match["player1"]["gender"])
                print("Elo:\t " , match["player1"]["elo"])
                print("Identification number:\t " , match["player1"]["identification number"])
                print("Score:\t", match["score_player1"], "\n")
                print("---------- Player 2 ----------\n")
                if match["score_player2"]==1:
                    print("*** Winner ***\n")
                elif match["score_player2"]==0:
                    print("*** Looser ***\n")
                print("Name:\t " , match["player2"]["name"])
                print("First name:\t " , match["player2"]["first_name"])
                print("Birthday:\t " , match["player2"]["birthday"])
                print("Gender:\t " , match["player2"]["gender"])
                print("Elo:\t " , match["player2"]["elo"])
                print("Identification number:\t " , match["player2"]["identification number"])
                # print("score:\t " , match["player2"]["score"])
                print("Score:\t", match["score_player2"], "\n")
                print("********************************************\n")
                i+=1
        print()

    def get_players_list(self, tournament):
        players = list()
        for player in tournament["players"]:
            player = Player(player['name'], player['first_name'],
                        player['birthday'], player['gender'], 
                        player['elo']
            )
            players.append(player)
        return players

    def tournament_players_alphabetic_order(self, tournament):
        players = self.get_players_list(tournament)
        players.sort(key=lambda x: x.name)
        for player in players:
            print(player)

    def tournament_players_elo_ascending_order(self, tournament):
        players = self.get_players_list(tournament)
        players.sort(key=lambda x: x.elo)
        for player in players:
            print(player)

    def tournament_players_elo_descending_order(self, tournament):
        players = self.get_players_list(tournament)
        players.sort(reverse=True, key=lambda x: x.elo)
        for player in players:
            print(player)