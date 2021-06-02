#! Python3
# coding utf-8

from Model.utils import is_date_valid


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
    return elo

