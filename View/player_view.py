#! Python3
# coding utf-8

from Model.utils import is_date_valid


def get_player_name():
    name = input("Entrer le nom du joueur : ")
    while name.isnumeric() is True:
        print(
            "Veuillez saisir des caractères valides, ni chiffres ni caractères spéciaux"
        )
        name = input("Entrer le nom du joueur : ")
    return name


def get_player_first_name():
    first_name = input("Entrer le prénom du joueur : ")
    while first_name.isnumeric() is True:
        print(
            "Veuillez saisir des caractères valides, ni chiffres ni caractères spéciaux"
        )
        first_name = input("Entrer le prénom du joueur : ")
    return first_name


def get_player_birthday():
    birthday = input("Entrer la date de naissance du joueur (JJ/MM/YYYY) : ")
    while is_date_valid(birthday) is False:
        print("date incorrecte, saisir une date au format JJ/MM/YYYY")
        birthday = input("Entrer la date de naissance du joueur (JJ/MM/YYYY): ")
    return birthday


def get_player_gender():
    gender = input("Entrer le genre du joueur (M/F): ")
    while gender != "M" and gender != "F":
        print("Veuillez saisir M pour masculin ou F pour féminin")
        gender = input("Entrer le genre du joueur (M/F): ")
    return gender


def get_player_elo():
    elo = input("Entrer le classement elo du joueur : ")
    while not elo.isnumeric():
        print("Veuillez saisir un nombre entier positif")
        elo = input("Entrer le classement elo du joueur : ")
    return elo

