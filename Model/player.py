#! Python3
# coding: utf-8

from tinydb import TinyDB


class Player:
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
        self.id_player = self.name[0:3] + str(self.elo)
        return self.id_player

    def set_score(self, score):
        self.score =int(score)

    def set_opponents(self, opponents):
        self.opponents = opponents

    def __str__(self):
        out = (
            f"name:\t{self.name}\nfirst_name:\t{self.first_name}\n"
            f"birthday:\t{self.birthday}\ngender:\t{self.gender}\n"
            f"elo:\t{self.elo}\nidentification number:"
            f"\t{self.id_player}\nscore:\t{self.score}\n"
        )
        return out

    def serialize(self):
        serialized_player = {"name": self.name, "first_name": self.first_name, 
        "birthday": self.birthday, "gender": self.gender, 
        "elo": self.elo, "identification number": self.id_player, 
        "score": self.score, "opponents": self.opponents
        }
        return serialized_player

    def players_deserialized():
        db = TinyDB("players.json", indent=4) # crée un fichier json vide
        players_table = db.table("players")
        serialized_players = players_table.all()
        players = list()
        for player in serialized_players:
            new_player = Player(player['name'], player['first_name'],
                            player['birthday'], player['gender'], 
                            player['elo'])
            players.append(new_player)
        return players

    def print_score(player):
        print("récapitulatif du match :")
        print(f"{player.name} ({player.id_player}) score =\t{player.score}")


    def print_opponents(player):
        print(f"{player.name} ({player.id_player}) a joué contre :\t{player.opponents}")


