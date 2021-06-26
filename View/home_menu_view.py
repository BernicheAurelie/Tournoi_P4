#! Python3
# coding: utf-8

from Model.utils import is_answer_ok
from View.tournament_view import ReportTournament
from View.player_view import ReportPlayer
from Controller.player_controller import PlayerController
from Controller.tournament_controller import TournamentController


"""Four menus with different actions that can be performed by the user,
asking him different choices and allowing him to quit application"""


class HomeMenu:
    """Principal menu to asking to the user to start or to reload a tournament
    or to print reports or to change player's elo"""

    def print_home_menu(self):
        """Print different choices to the user"""
        print("==================== HOME MENU ====================\n")
        print("1: start new tournament")
        print("2: Reload a tournament")
        print("3: See reports and results")
        print("4: Change Elo rating")
        print("5: Quit\n")

    def home_menu(self):
        is_app_run = True
        while is_app_run:
            self.print_home_menu()
            answer = is_answer_ok(5)
            print()
            if answer == 1:
                print("You're going to start a new tournament\n")
                tournament = TournamentController()
                tournament.new_tournament()
            elif answer == 2:
                print("You're going to reload a tournament\n")
                tournament = TournamentController()
                tournament.reload_tournament()
            elif answer == 3:
                print("You're going to watch reports and results\n")
                report = ReportsMenu()
                report.reports_menu()
            elif answer == 4:
                print("You're going to modify player's elo rating\n")
                player = PlayerController()
                player.modify_elo()
            elif answer == 5:
                print("Bye bye")
                is_app_run = False


class ReportsMenu:
    """Main menu of reports giving choice to print reports
    for players or for tournaments"""

    def print_reports_menu(self):
        """Print different choices to the user"""
        print("=============== REPORTS MENU ===============\n")
        print("1: acceed to players reports")
        print("2: acceed to tournaments reports")
        print("3: return to Home Menu\n")

    def reports_menu(self):
        is_reports_menu = True
        while is_reports_menu:
            self.print_reports_menu()
            answer = is_answer_ok(3)
            print()
            if answer == 1:
                print("You're going to acceed to players reports\n")
                report = PlayerReportsMenu()
                report.players_reports_menu()
            elif answer == 2:
                print("You're going to acceed to tournaments reports\n")
                report = TournamentReportsMenu()
                report.tournament_reports_menu()
            elif answer == 3:
                is_reports_menu = False


class PlayerReportsMenu:
    """Reports for players sorting by alphabetic order
    or in elo ascending or descending order"""

    def print_players_reports_menu(self):
        """Print different choices to the user"""
        print("========== PLAYERS REPORTS MENU ==========\n")
        print("1: get player in alphabetic order")
        print("2: get players in elo ascending order")
        print("3: get players in elo descending order")
        print("4: return to principal reports menu\n")

    def players_reports_menu(self):
        """Reports for players sorting in several ways"""
        is_players_report_menu = True
        while is_players_report_menu:
            self.print_players_reports_menu()
            answer = is_answer_ok(4)
            print()
            if answer == 1:
                print("***** Sorting all players *****")
                print("***** By alphabetic order *****\n")
                reports = ReportPlayer()
                reports.players_alphabetic_order()
            elif answer == 2:
                print("***** Sorting all players *****")
                print("**** in ascending elo order ****\n")
                reports = ReportPlayer()
                reports.players_elo_ascending_order()
            elif answer == 3:
                print("***** Sorting all players *****")
                print("*** in descending elo order ***\n")
                reports = ReportPlayer()
                reports.players_elo_descending_order()
            elif answer == 4:
                is_players_report_menu = False


class TournamentReportsMenu:
    """Menu to print reports for tournaments with general informations, rounds' list
    matchs' list and tournament's players sorting in several ways"""

    def print_tournament_reports_menu(self):
        """Print different choices to the user"""
        print("=============== TOURNAMENT REPORTS MENU ===============\n")
        print("1: See tournaments' informations")
        print("2: See all rounds from a tournament")
        print("3: See all matchs from a tournament")
        print("4: See tournament's players sorted by alphabetic order ")
        print("5: See tournament's players sorted in ascending elo ")
        print("6: See tournament's players sorted in descending elo ")
        print("7: See tournament's list")
        print("8: return to principal reports menu\n")

    def tournament_reports_menu(self):
        """Menu to print reports for tournaments"""
        is_tournament_reports_menu = True
        while is_tournament_reports_menu:
            self.print_tournament_reports_menu()
            answer = is_answer_ok(8)
            print()
            if answer == 1:
                print("Here is tournaments' informations\n")
                tournament = ReportTournament()
                tournament.tournament_info()
            elif answer == 2:
                print("Here is rounds\n")
                tournament = TournamentController()
                tournament.tournament_reports_rounds()
            elif answer == 3:
                print("Here is matches\n")
                tournament = TournamentController()
                tournament.tournament_reports_matchs()
            elif answer == 4:
                print(
                    "Here is list of tournament's players sorted in alphabetic order\n"
                )
                tournament = TournamentController()
                tournament.tournament_reports_players_alphabetic_order()
            elif answer == 5:
                print("Here is list of tournament's players sorted by ascending elo\n")
                tournament = TournamentController()
                tournament.tournament_reports_players_elo_ascending_order()
            elif answer == 6:
                print("Here is list of tournament's players sorted by descending elo\n")
                tournament = TournamentController()
                tournament.tournament_reports_players_elo_descending_order()
            elif answer == 7:
                tournament = ReportTournament()
                tournament.all_tournaments()
            elif answer == 8:
                is_tournament_reports_menu = False
