#! Python3
# coding utf-8


"""Define the tournament, execute different actions to enter player,
add rounds and matchs and return players's score.
Deserialize a tournament to reload it and print different reports"""


from tinydb import TinyDB, Query, where
from Model.tournament import Tournament
from Model.player import Player
from Model.match import Match
from Model.round import Round
from View.tournament_view import ReportTournament
from View.tournament_view import (
    get_tournament_name,
    get_tournament_place,
    get_tournament_start,
    get_tournament_time_control,
    get_confirmation,
    get_tournaments,
    get_user_choice,
)
from View.player_view import (
    get_player_birthday,
    get_player_elo,
    get_player_first_name,
    get_player_gender,
    get_player_name
)
from View.round_view import enter_score


players = [
    Player("BERNICHE", "AURELIE", "09/07/1981", "F", 10),
    Player("DUPRE", "JEAN MICHEL", "08/31/1951", "M", 60),
    Player("HARNICHARD", "JOCELYNE", "09/27/1954", "F", 50),
    Player("DUPONT", "VIRGINIE", "06/03/1975", "F", 20),
    Player("HUBERT", "JEAN NICOLAS", "10/25/1979", "M", 30),
    Player("ANDRE", "FREDERIC", "02/12/74", "M", 40),
    Player("CARPENTIER", "MELANIE", "01/15/78", "F", 70),
    Player("BOURIENNE", "VALENTIN", "09/04/2002", "M", 80),
]


class TournamentController:
    """Controle all tournament actions, enter player, run rounds, update score with match's results
    reload tournament to continue it or to print informations"""

    def __init__(self):
        self.tournament = None

    def start(self):
        """Get tournament's informations from the user with the views
        and define the new tournament"""
        name = get_tournament_name()
        place = get_tournament_place()
        start = get_tournament_start()
        end = "On Going"
        time_control = get_tournament_time_control()
        self.tournament = Tournament(name, place, start, end, time_control)

    def new_tournament(self):
        """Run new tournament with 8 players and 4 rounds if the user confirms to continue it"""
        self.start()
        self.enter_players()
        confirmation = get_confirmation()
        if confirmation == "y":
            self.run_first_round()
            for i in range(2, 5):
                confirmation = get_confirmation()
                if confirmation == "y":
                    self.run_round(i)
                elif confirmation == "n":
                    break
        self.tournament.register_end_time()
        self.print_players_score()
        self.serialized_players()
        self.serialized_tournament()

    def enter_players(self):
        """Add 8 players to tournament's players list getting informations
        from the user from player_view"""
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
        """Add round and print its informations.
        Sort players list in elo order, add match
        with player 1 and player 5 and so on.
        Handle score with match results obtained from the user"""
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

        round.register_end_time()

    def get_players_for_round(self):
        """Create new list from tournament's players list and
        sort it in elo and score order"""
        next_round_players = list()
        for player in self.tournament.players:
            next_round_players.append(player)
        next_round_players.sort(key=lambda x: x.elo)  # elo
        next_round_players.sort(reverse=True, key=lambda x: x.score)  # score
        return next_round_players

    def run_round(self, round_number):
        """Run round from the new players list. While isn't empty,
        take player 1 (i) and player 2 (i+1), unless they've already played together.
        In this case, take the next one (i+=1).
        Define players index and delete them from the list
        Handle score and print round's informations like for round one"""
        i = 0
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
            del next_round_players[player2_index - 1]
            i = 0

        for match in self.tournament.rounds[round_number - 1].matchs:
            self.__handle_score(match)

        round.register_end_time()

    def __handle_score(self, match):
        """From match results obtained by the user entry,
        add point to the player's score"""
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
        """Print players' score and opponents"""
        for player in self.tournament.players:
            player.print_score()
            player.print_opponents()

    def serialized_players(self):
        """Serialize tournament's players in the player DB"""
        db = TinyDB("players.json", indent=4)
        players_table = db.table("players")
        for player in self.tournament.players:
            players_table.insert(player.serialize())

    def serialized_tournament(self):
        """Serialize tournament in the tournament DB"""
        db = TinyDB("tournaments.json", indent=4)
        tournaments_table = db.table("tournaments")
        tournaments_table.insert(self.tournament.serialize())

    def get_player(self, name, first_name, birthday, gender, elo):
        """Get player to define a match when we reload a tournament"""
        for player in self.tournament.players:
            if (
                player.name == name
                and player.first_name == first_name
                and player.birthday == birthday
                and player.gender == gender
                and player.elo == elo
            ):
                return player

    def deserializer(self, tournament):
        """Deserializes tournament with DB informations
        and recreats tournament, round, match and player in class instances.
        Update player's score and opponents list"""
        self.tournament = Tournament(
            name=tournament["name"],
            place=tournament["place"],
            start=tournament["start"],
            end=tournament["end"],
            time_control=tournament["time_control"],
        )
        for player in tournament["players"]:
            new_player = Player(
                player["name"],
                player["first_name"],
                player["birthday"],
                player["gender"],
                player["elo"],
            )
            new_player.set_score(player["score"])
            new_player.set_opponents(player["opponents"])
            self.tournament.add_player(new_player)

        for round in tournament["rounds"]:
            new_round = Round(round["number"])
            for match in round["matchs"]:
                player1 = self.get_player(
                    match["player1"]["name"],
                    match["player1"]["first_name"],
                    match["player1"]["birthday"],
                    match["player1"]["gender"],
                    match["player1"]["elo"],
                )
                player2 = self.get_player(
                    match["player2"]["name"],
                    match["player2"]["first_name"],
                    match["player2"]["birthday"],
                    match["player2"]["gender"],
                    match["player2"]["elo"],
                )
                new_match = Match(player1, player2)
                new_match.set_score(match["score_player1"], match["score_player2"])
                new_round.add_reload_match(new_match)
            self.tournament.add_round(new_round)

    def reload_tournament_name(self):
        """Reload a tournament from the tinydb DB, asking tournament's name to the user"""
        db = TinyDB("tournaments.json")
        tournaments_table = db.table("tournaments")
        get_tournaments()
        name = get_user_choice()
        reload_tournament = tournaments_table.search(where("name") == name)
        while not reload_tournament:
            name = get_user_choice()
            reload_tournament = tournaments_table.search(where("name") == name)
        tournament = reload_tournament[0]
        return tournament

    def reload_tournament(self):
        """Reload tournament, run remaining rounds and serialize it"""
        db = TinyDB("tournaments.json")
        tournaments_table = db.table("tournaments")
        query = Query()
        tournament = self.reload_tournament_name()
        self.deserializer(tournament)
        if len(tournament["rounds"]) == 0:
            self.run_first_round()
            for lefted_round in range(2, 5):
                confirmation = get_confirmation()
                if confirmation == "y":
                    self.run_round(lefted_round)
                elif confirmation == "n":
                    break
        else:
            for lefted_round in range(len(tournament["rounds"]) + 1, 5):
                confirmation = get_confirmation()
                if confirmation == "y":
                    self.run_round(lefted_round)
                elif confirmation == "n":
                    break
        tournaments_table.remove(query.name == tournament["name"])
        self.tournament.register_end_time()
        self.print_players_score()
        self.serialized_tournament()

    def tournament_reports_players_alphabetic_order(self):
        """Deserialize tournament and reload it.
        Print tournament's players list, sorted by alphabetic order, with view"""
        tournament = self.reload_tournament_name()
        self.deserializer(tournament)
        report_players = ReportTournament()
        report_players.tournament_players_alphabetic_order(tournament)

    def tournament_reports_players_elo_ascending_order(self):
        """Deserialize tournament and reload it.
        Print tournament's players list, sorted in elo ascending order, with view"""
        tournament = self.reload_tournament_name()
        self.deserializer(tournament)
        report_players = ReportTournament()
        report_players.tournament_players_elo_ascending_order(tournament)

    def tournament_reports_players_elo_descending_order(self):
        """Deserialize tournament and reload it.
        Print tournament's players list, sorted in elo ascending order, with view"""
        tournament = self.reload_tournament_name()
        self.deserializer(tournament)
        report_players = ReportTournament()
        report_players.tournament_players_elo_descending_order(tournament)

    def tournament_reports_rounds(self):
        """Deserialize tournament and reload it.
        Print tournament's rounds with view"""
        tournament = self.reload_tournament_name()
        self.deserializer(tournament)
        report_rounds = ReportTournament()
        report_rounds.tournament_rounds(tournament)

    def tournament_reports_matchs(self):
        """Deserialize tournament and reload it.
        Print tournament's matchs with view"""
        tournament = self.reload_tournament_name()
        self.deserializer(tournament)
        report_matchs = ReportTournament()
        report_matchs.tournament_matchs(tournament)
