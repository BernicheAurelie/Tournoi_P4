#! Python3
# coding utf-8

from tinydb import TinyDB, Query, where
from Model.player import Player

db = TinyDB('players.json')
players_table = db.table('players')
serialized_players = players_table.all()
# Player = Query()
# players_table.update({"Elo_rating" : 20}, Player.name == "Berniche")
#print (players_table.search(where("name")=="Berniche"))
#print(serialized_players)
for serialized_player in serialized_players:
    name = serialized_player["name"]
    first_name = serialized_player["first_name"]
    birthday = serialized_player["birthday"]
    gender = serialized_player["gender"]
    elo = serialized_player["Elo_rating"]
    id_player = serialized_player["identification number"]
    score = serialized_player["score"]
    opponents = serialized_player["opponents"]
    #print(serialized_player)
    player = Player(
        name=name, first_name=first_name, birthday=birthday,
        gender=gender, elo=elo, 
        score=score
    )
    players=list()
    players.append(player)
    print(players[0])

    