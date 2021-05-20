def enter_score(match):
    print("scores du match :")
    print(f"player 1 :\t {match.player1.name}, score:{match.player1.score} ({match.player1.id_player})")
    print(f"player 2 :\t {match.player2.name}, score:{match.player1.score} ({match.player2.id_player})")
    score = input("Enter score (1 : player 1 win | 2 : player 2 win | 3 : draw) : ")
    return score
