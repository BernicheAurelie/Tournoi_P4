#! python3
# coding utf-8

from Model.utils import is_date_valid


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

def get_user_choice():
    print("which tournament do you want to reload?")
    choice = input("Please, enter its name: ")
    choice = choice.upper()
    while not choice.isalnum():
        print("Please, check your entry, see choices above")
        print("which tournament do you want to reload?")
        choice = input("Please, enter tournament's name: ")
        choice = choice.upper()
    return choice