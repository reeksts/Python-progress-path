from random import randint
import matplotlib.pyplot as plt
from pprint import PrettyPrinter
from ttictoc import tic,toc


tic()
pp = PrettyPrinter(indent=2)

players = 1
plays = 10
games = 100000000

player_list = list(range(1, players+1))

player_scores = {}

for player in player_list:
    max_score = 0
    for game in range(games):
        if game % 1000000 == 0:
            print(f'game number: {game}')
        win_count = 0
        for play in range(plays):
            draw_val = randint(1, plays+1)
            if player == draw_val:
                win_count += 1
        if win_count > max_score:
            max_score = win_count

    player_scores[str(player)] = max_score

pp.pprint(player_scores)

print(toc())




