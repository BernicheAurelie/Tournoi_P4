#! python3
# coding utf-8

from Model.utils import is_date_valid
from Model.player import Player
from tinydb import TinyDB, where


"""Several methods to get tournament's informations form the user
and class ReportTournament to print different reports for the tournaments"""


def get_tournament_name():
    name = input("Enter tournament's name : ")
    name = name.upper()
    while name == "":
        print("Please, check your entry.")
        name = input("Enter tournament's name : ")
        name = name.upper()
    return name


def get_tournament_place():
    place = input("Enter tournament's place : ")
    place = place.upper()
    while place == "":
        print("Please, check your entry.")
        place = input("Enter tournament's place : ")
    return place


def get_tournament_start():
    start = input("Enter tournament's start date (MM/DD/YYYY) : ")
    while is_date_valid(start) is False:
        print("Incorrect date, enter a date in the format MM/DD/YYYY")
        start = input("Enter tournament's start date (MM/DD/YYYY) : ")
    return start


def get_tournament_time_control():
    time_control = input("Enter speed game shape (Bullet/Blitz/Rapid) : ")
    time_control = time_control.lower()
    while (
        time_control != "bullet" and time_control != "blitz" and time_control != "rapid"
    ):
        time_control = input("Enter speed game shape (Bullet/Blitz/Rapid) : ")
        time_control = time_control.lower()
    return time_control


def get_confirmation():
    print()
    print("Do you want to continue tournament? Yes or No?")
    confirmation = input("Enter Y or N: ")
    confirmation = confirmation.lower()
    print()
    while confirmation != "y" and confirmation != "n":
        print("Do you want to continue tournament? Yes or No?")
        confirmation = input("Please, enter Y or N:")
        confirmation = confirmation.lower()
        print()
    return confirmation


def get_user_choice():
    print("Which tournament do you want to reload?\n")
    choice = input("Please, enter its name: ")
    choice = choice.upper()
    print()
    while choice == "":
        print("Please, check your entry, see choices above")
        print("Which tournament do you want to reload?\n")
        choice = input("Please, enter tournament's name: ")
        choice = choice.upper()
        print()
    return choice


def get_tournaments():
    db = TinyDB("tournaments.json")
    tournaments_table = db.table("tournaments")
    tournaments = tournaments_table.all()
    for i in range(len(tournaments)):
        print(i + 1, ") ", tournaments[i]["name"])
        if len(tournaments[i]["rounds"]) == 4:
            print("\t --> Tournament finished")
        elif len(tournaments[i]["rounds"]) < 4:
            print("\t --> lefted rounds : ", (4 - len(tournaments[i]["rounds"])))
    print()


def print_error_serialization():
    print("Warning, tournament backup failed")


class ReportTournament:
    """get tournament asking its name to the user and print several informations"""

    def tournament_info(self):
        """Ask tournament name to the user and
        deserialize it to print generals informations"""
        db = TinyDB("tournaments.json")
        tournaments_table = db.table("tournaments")
        get_tournaments()
        name = get_user_choice()
        reload_tournament = tournaments_table.search(where("name") == name)
        try:
            tournament = reload_tournament[0]
            print("Tournament's place:\t\t", tournament["place"])
            print("Tournament's speed game:\t", tournament["time_control"])
            print("Tournament's start:\t\t", tournament["start"])
            print("Tournament's end:\t\t", tournament["end"], "\n")
        except IndexError:
            print("Tournament not found\n")

    def tournament_rounds(self, tournament):
        """Print rounds' informations"""
        for round in tournament["rounds"]:
            print(
                "*************************** ROUND ",
                round["number"],
                "*************************** \n",
            )
            print("Start:\t ", round["start"])
            print("End:\t ", round["end"], "\n")
            print("======================== MATCHS ======================")
            print()
            i = 0
            for match in round["matchs"]:
                i += 1
                self.print_tournament_matchs(i, match)
        print("\nEND OF ROUND REPORT\n")

    def print_tournament_matchs(self, i, match):
        """Print matchs' informations"""
        print("--> Match number ", i, "\n")
        print("---------- Player 1 ----------\n")
        if match["score_player1"] == 1:
            print("*** Winner ***\n")
        elif match["score_player1"] == 0:
            print("*** Looser ***\n")
        elif match["score_player1"] == 0.5:
            print("*** Egality ***\n")
        print("Name:\t\t\t ", match["player1"]["name"])
        print("First name:\t\t ", match["player1"]["first_name"])
        print("Birthday:\t\t ", match["player1"]["birthday"])
        print("Gender:\t\t\t ", match["player1"]["gender"])
        print("Elo:\t\t\t ", match["player1"]["elo"])
        print("Identification number:\t ", match["player1"]["identification number"])
        print("Score:\t\t\t ", match["score_player1"], "\n")
        print("---------- Player 2 ----------\n")
        if match["score_player2"] == 1:
            print("*** Winner ***\n")
        elif match["score_player2"] == 0:
            print("*** Looser ***\n")
        elif match["score_player2"] == 0.5:
            print("*** Egality ***\n")
        print("Name:\t\t\t ", match["player2"]["name"])
        print("First name:\t\t ", match["player2"]["first_name"])
        print("Birthday:\t\t ", match["player2"]["birthday"])
        print("Gender:\t\t\t ", match["player2"]["gender"])
        print("Elo:\t\t\t ", match["player2"]["elo"])
        print("Identification number:\t ", match["player2"]["identification number"])
        print("Score:\t\t\t ", match["score_player2"], "\n")
        print("***************************************************************\n")
        i += 1

    def tournament_matchs(self, tournament):
        """Print matchs informations for each round"""
        for round in tournament["rounds"]:
            i = 0
            for match in round["matchs"]:
                i += 1
                self.print_tournament_matchs(i, match)
        print("\nEND OF MATCHS REPORT\n")

    def get_players_list(self, tournament):
        """Get the tournament's players list from DB"""
        players = list()
        for player in tournament["players"]:
            player = Player(
                player["name"],
                player["first_name"],
                player["birthday"],
                player["gender"],
                player["elo"],
                player["score"]
            )
            players.append(player)
        return players

    def tournament_players_alphabetic_order(self, tournament):
        """Sort players list by alphabetic order"""
        players = self.get_players_list(tournament)
        players.sort(key=lambda x: x.name)
        for player in players:
            print(player)

    def tournament_players_elo_ascending_order(self, tournament):
        """Sort players list in elo ascending order"""
        players = self.get_players_list(tournament)
        players.sort(key=lambda x: x.elo)
        for player in players:
            print(player)

    def tournament_players_elo_descending_order(self, tournament):
        """Sort players list in elo descending order"""
        players = self.get_players_list(tournament)
        players.sort(reverse=True, key=lambda x: x.elo)
        for player in players:
            print(player)

    def all_tournaments(self):
        get_tournaments()
