#! Python3
# coding: utf-8


"""View to ask to the user to enter score at the end of the match"""


def enter_score(match):
    print("Match's score :")
    print(
        f"player 1 :\t {match.player1.name} ({match.player1.id_player}), score:{match.player1.score}"
    )
    print(
        f"player 2 :\t {match.player2.name} ({match.player2.id_player}), score:{match.player1.score}"
    )
    score = input("Enter score (1 : player 1 win | 2 : player 2 win | 3 : draw) : ")
    print()
    return score
