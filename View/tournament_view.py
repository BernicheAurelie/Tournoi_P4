#! python3
# coding utf-8

from Model.utils import is_date_valid


def get_tournament_name():
    name = input("Entrer le nom du tournoi : ")
    while name == "":   # while not name.isalpha():
        print("Veuillez saisir un nom pour le tournoi")
        name = input("Entrer le nom du tournoi : ")
    return name


def get_tournament_place():
    place = input("Entrer le lieu du tournoi : ")
    while place == "":
        print("Veuillez saisir un lieu pour le tournoi")
        place = input("Entrer le lieu du tournoi : ")
    return place


def get_tournament_start():
    start = input("Entrer la date de début du tournoi (JJ/MM/YYYY) : ")
    while is_date_valid(start) is False:
        print("date incorrecte, saisir une date au format JJ/MM/YYYY")
        start = input("Entrer la date de début du tournoi (JJ/MM/YYYY): ")
    return start


def get_tournament_time_control():
    time_control = input(
        "Entrer la méthode de gestion du temps (Bullet/Blitz/Rapid) : "
    )
    time_control = time_control.lower()
    while (
        time_control != "bullet" and time_control != "blitz" and time_control != "rapid"
    ):
        time_control = input(
            "Entrer la méthode de gestion du temps (bullet/blitz/rapid) : "
        )
        time_control = time_control.lower()
    return time_control
