#! Python3
# coding utf-8

from tinydb import TinyDB, where
from Model.utils import is_date_valid
from Model.player import Player


"""Get informations to the player asking to the user
and class ReportPlayer to print players informations"""


def get_player_name():
    name = input("Enter player's name : ")
    name = name.upper()
    while name.isnumeric() is True:
        print("Please, check your entry.")
        print("Only alphabetical letters")
        name = input("Enter player's name : ")
        name = name.upper()
    return name


def get_player_first_name():
    first_name = input("Enter player's first name : ")
    first_name = first_name.upper()
    while not first_name.isalpha():
        print("Please, check your entry.")
        print("Only alphabetical letters")
        first_name = input("Enter player's first name : ")
        first_name = first_name.upper()
    return first_name


def get_player_birthday():
    birthday = input("Enter player's birth date (MM/JJ/YYYY) : ")
    while is_date_valid(birthday) is False:
        print("Incorrect date, enter the birth date in the format MM/DD/YYYY")
        birthday = input("Enter player's birth date (MM/JJ/YYYY) : ")
    return birthday


def get_player_gender():
    gender = input("Enter the player gender (M/F): ")
    gender.upper()
    while gender != "M" and gender != "F":
        print("Please, enter M for male or F for female")
        gender = input("Enter the player gender (M/F): ")
        gender.upper()
    return gender


def get_player_elo():
    elo = input("Enter player's Elo rating : ")
    while not elo.isnumeric():
        print("Please, enter a positive integer number")
        elo = input("Enter player's Elo rating : ")
    print()
    return int(elo)


class ReportPlayer:
    """Print reports for players in several ways"""

    def players_alphabetic_order(self):
        """Deserialize players from DB and sort players by alphabetic order"""
        players = Player.players_deserialized()
        players.sort(key=lambda x: (x.name, x.first_name))
        for i in players:
            print("****************************\n", i)

    def players_elo_ascending_order(self):
        """Deserialize players from DB and sort players in elo ascending order"""
        players = Player.players_deserialized()
        players.sort(key=lambda x: x.elo)
        for i in players:
            print("****************************\n", i)

    def players_elo_descending_order(self):
        """Deserialize players from DB and sort players in elo descending order"""
        players = Player.players_deserialized()
        players.sort(reverse=True, key=lambda x: x.elo)
        for i in players:
            print("****************************\n", i)

    @staticmethod
    def print_modified_player(elo):
        """Static method to check the modification of player's elo"""
        db = TinyDB("players.json", indent=4)
        players_table = db.table("players")
        try:
            player_modified = players_table.search(where("elo") == elo)
            print(
                "Player modified successfully:\nName:\t\t ", player_modified[0]["name"]
            )
            print("First_name:\t ", player_modified[0]["first_name"])
            print("Elo:\t\t ", player_modified[0]["elo"])
        except IndexError:
            print("Player not found")
