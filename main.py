from singlePrize import single_bfs, single_dfs, single_gbfs, single_astar
from multiPrize import multi_astar

one_prize_file = ["1prize-open.txt", "1prize-medium.txt", "1prize-large.txt"]
multi_prize_file = ["multiprize-tiny.txt","multiprize-small.txt","multiprize-medium.txt"]

for file in one_prize_file:
    single_bfs(file)
    single_dfs(file)
    single_gbfs(file)
    single_astar(file)

for file in multi_prize_file:
    multi_astar(file)

