#! Python3
# coding: utf-8

from tinydb import TinyDB


class Player:
    """Class Player define with some items and several methods
    to update score and opponents' list and
    serialize and deserialize players from the tinydb database"""

    def __init__(self, name, first_name, birthday, gender, elo, score=0):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.elo = elo
        self.id_player = self._id_player()
        self.score = score
        self.opponents = list()

    def _id_player(self):
        """Create an identification number with name and ranking"""
        self.id_player = self.name[0:3] + str(self.elo)
        return self.id_player

    def set_score(self, score):
        """Update score at the deserialisation"""
        self.score = score

    def set_opponents(self, opponents):
        """Update opponents list at the deserialisation"""
        self.opponents = opponents

    def __str__(self):
        out = (
            f"\nname:\t\t\t{self.name}\nfirst_name:\t\t{self.first_name}\n"
            f"birthday:\t\t{self.birthday}\ngender:\t\t\t{self.gender}\n"
            f"elo:\t\t\t{self.elo}\nidentification number:"
            f"\t{self.id_player}\nscore:\t\t\t{self.score}\n"
        )
        return out

    def serialize_player_in_player_db(self):
        """Return a dictionary to serialise player in DB"""
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "elo": self.elo,
            "identification number": self.id_player
        }
        return serialized_player

    def serialize(self):
        """Return a dictionary to serialise player in DB"""
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "elo": self.elo,
            "identification number": self.id_player,
            "score": self.score,
            "opponents": self.opponents,
        }
        return serialized_player

    def players_deserialized():
        """Deserialise players from DB and append players' list"""
        db = TinyDB("players.json", indent=4)
        players_table = db.table("players")
        serialized_players = players_table.all()
        players = list()
        for player in serialized_players:
            new_player = Player(
                player["name"],
                player["first_name"],
                player["birthday"],
                player["gender"],
                player["elo"]
            )
            players.append(new_player)
        return players

    def print_score(player):
        """Print player's score at the end of the match"""
        print("---------- Match's summary ----------- :\n")
        print(f"{player.name} ({player.id_player})\t score =\t\t{player.score}")

    def print_opponents(player):
        """Print player's opponents at the end of the match"""
        print(
            f"{player.name} ({player.id_player})\t played against :\t{player.opponents}\n"
        )
