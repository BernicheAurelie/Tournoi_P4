#! Python3
# coding utf-8

from tinydb import TinyDB, Query, where
from Model.tournament import Tournament

db = TinyDB('tournaments.json')
tournaments_table = db.table('tournaments')
serialized_tournaments = tournaments_table.all()
#print (serialized_tournaments)
for tournament in serialized_tournaments:
    name = tournament['name']
    place=tournament['place']
    start=tournament['start']
    end=tournament['end']
    time_control=tournament['time_control']
    players=tournament['players']
    rounds=tournament['rounds']

    tournament = Tournament(
        name=name, place=place, start=start, end=end, 
        time_control=time_control
    )
    print(tournament.name)
