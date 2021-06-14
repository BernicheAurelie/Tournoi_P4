#! Python3
# coding: utf-8

from View.tournament_view import ReportTournament
from Controler.player_controller import PlayerController
from View.player_view import ReportPlayer
from Controler.tournament_controler import tournamentControler

class HomeMenu:
    def print_home_menu(self):
        print("1: start new tournament")
        print("2: Reload a tournament")
        print("3: See reports and results")
        print("4: Change Elo rating")
        print("5: Quit")
    
    # def is_answer_ok(self, user_input, max_input):
    #     user_input = int(user_input)
    #     return user_input > 0 and user_input <= max_input

    def is_answer_ok(self, user_input, max_input):
        self.print_home_menu()
        while not user_input.isnumeric():
            user_input = input("Please, enter your choice : ")
        user_input = int(user_input)
        while user_input > 0 and user_input <= max_input:
            return user_input

                


    # def answer_valid(self, user_input, max_input):
    #     user_input = int(user_input)
    #     while not 0 < user_input and not user_input <= max_input:
    #         print("ERROR, Please check your choice")
    #     return user_input


    def home_menu(self):
        print("--------- HOME MENU ---------")
        self.print_home_menu()
        answer = input("Enter your choice : ")
        max_input = 5
        while not self.is_answer_ok(answer, max_input):
            self.print_home_menu()
            answer = input("Please, enter your choice : ")    
        if(answer == "1"):
            print("Hello, you're going to start a new tournament")
            tournament = tournamentControler()
            tournament.new_tournament()
            self.home_menu()
        elif(answer == '2'):
            print("Hello, you're going to reload a tournament")
            tournament = tournamentControler()
            tournament.reload_tournament()
            self.home_menu()
        elif(answer == "3"): 
            print("Hello, you're going to watch reports and results")
            report = ReportsMenu()
            report.reports_menu()
            self.home_menu()
        elif(answer=="4"):
            print("You're going to modify player's elo rating")
            player= PlayerController()
            player.modify_elo()
            self.home_menu()
        elif(answer=="5"):
            print("Bye bye")
            self.home_menu()
            


class PlayerReportsMenu:

    def print_players_reports_menu(self):
        print("1: get player in alphabetic order")
        print("2: get players in elo ascending order")
        print("3: get players in elo descending order")
        print("4: return to principal reports menu")

    def is_answer_ok(self, user_input, max_input):
        self.print_players_reports_menu()
        while not user_input.isnumeric():
            user_input = input("Please, enter your choice : ")
        user_input = int(user_input)
        while user_input > 0 and user_input <= max_input:
            return user_input

    def players_reports_menu(self):
        print("------PLAYERS REPORTS  MENU------")
        self.print_players_reports_menu()
        answer = input("Enter your choice : ")
        max_input = 4
        while not self.is_answer_ok(answer, max_input):
            answer = input("Enter your choice : ")
        if answer == "1":
            print("***tri de tous les joueurs***")
            print("***par nom***")
            reports = ReportPlayer()
            reports.players_alphabetic_order()
            self.players_reports_menu()
        elif answer == "2":
            print("***tri de tous les joueurs***")
            print("***par elo ordre croissant")
            reports = ReportPlayer()
            reports.players_elo_ascending_order()
            self.players_reports_menu()
        elif answer == "3":
            print("***tri de tous les joueurs***")
            print("***par elo ordre décroissant")
            reports = ReportPlayer()
            reports.players_elo_descending_order()
            self.players_reports_menu()
        elif answer == "4":
            print("bye bye")
            quit = ReportsMenu()
            quit.reports_menu()

class TournamentReportsMenu:
    
    def print_tournament_reports_menu(self):
        print("1: See all tournaments")
        print("2: See all rounds from a tournament")
        print("3: See all matchs from a tournament")
        print("4: See tournament's players sorted by alphabetic order ")
        print("5: See tournament's players sorted in ascending elo ")
        print("6: See tournament's players sorted in descending elo ")
        print("7: Quit")

    def is_answer_ok(self, user_input, max_input):
        self.print_tournament_reports_menu()
        while not user_input.isnumeric():
            user_input = input("Please, enter your choice : ")
        user_input = int(user_input)
        while user_input > 0 and user_input <= max_input:
            return user_input

    def tournament_reports_menu(self):
        self.print_tournament_reports_menu()
        answer = input("Enter your choice: ")
        max_input = 7
        while not self.is_answer_ok(answer, max_input):
            answer = input("Enter your choice: ")
        if answer == "1":
            print("Here is tournaments' informations")
            tournament = ReportTournament()
            tournament.tournament_info()
        elif answer == "2":
            print("Here is rounds")
            tournament = tournamentControler()
            tournament.tournament_reports_rounds()
        elif answer == "3":
            print("Here is matches")
            tournament = tournamentControler()
            tournament.tournament_reports_matchs()            
        elif answer == "4":
            print("Here is list of tournament's players sorted in alphabetic order")
            tournament = tournamentControler()
            tournament.tournament_reports_players_alphabetic_order() 
        elif answer == "5":
            print("Here is list of tournament's players sorted by ascending elo")
            tournament = tournamentControler()
            tournament.tournament_reports_players_elo_ascending_order()
        elif answer == "6":
            print("Here is list of tournament's players sorted by descending elo")
            tournament = tournamentControler()
            tournament.tournament_reports_players_elo_descending_order()
        elif answer == "7":
            print("by bye")
            quit = HomeMenu()
            quit.home_menu()

class ReportsMenu:

    def print_reports_menu(self):
        print("1: acceed to players reports")
        print("2: acceed to tournaments reports")
        print("3: return to Home Menu")


    def is_answer_ok(self, user_input, max_input):
        self.print_reports_menu()
        while not user_input.isnumeric():
            user_input = input("Please, enter your choice : ")
        user_input = int(user_input)
        while user_input > 0 and user_input <= max_input:
            return user_input

    def reports_menu(self):
        print("-------- REPORTS MENU ---------")
        self.print_reports_menu()
        answer = input("Enter your choice : ")
        max_input = 3
        while not self.is_answer_ok(answer, max_input):
            answer = input("Please, enter your choice : : ")
        if(answer == "1"):
            print("Hello, you're going to acceed to players reports")
            report = PlayerReportsMenu()
            report.players_reports_menu()
            self.reports_menu()
        elif(answer == "2"):
            print("Hello, you're going to acceed to tournaments reports")
            report = TournamentReportsMenu()
            report.tournament_reports_menu()
            self.reports_menu()
        elif (answer == "3"):
            print("bye bye")
            quit = HomeMenu()
            quit.home_menu()
