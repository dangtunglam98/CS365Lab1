from mazeClass import Maze
from collections import deque
from heapq import heappop, heappush

def single_bfs(file):
    maze = Maze(file)
    start, goal = (maze.startRow,maze.startCol), maze.prizesCor[0]
    queue = deque([("", start)])
    visited = set()
    graph = maze.maze2graph()
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path  + direction, neighbour))
    return False

def single_bfs_path(file):
    maze = Maze(file)
    maze.path(single_bfs(file))
    maze.drawMaze()

def single_dfs(file):
    maze = Maze(file)
    start, goal = (maze.startRow,maze.startCol), maze.prizesCor[0]
    queue = deque([("", start)])
    visited = set()
    graph = maze.maze2graph()
    while queue:
        path, current = queue.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return False

def single_dfs_path(file):
    maze = Maze(file)
    maze.path(single_dfs(file))
    maze.drawMaze()

def heuristic(current,goal): #Manhattan
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1] )

def single_astar(file):
    maze = Maze(file)
    start, goal = (maze.startRow, maze.startCol), maze.prizesCor[0]
    cost = 0
    pr_queue = []
    heappush(pr_queue,(cost + heuristic(start,goal),cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue,(cost + heuristic(neighbour,goal),cost + 1, path + direction, neighbour))
    return False

def single_gbfs(file):
    maze = Maze(file)
    start, goal = (maze.startRow, maze.startCol), maze.prizesCor[0]
    cost = 0
    pr_queue = []
    heappush(pr_queue,(heuristic(start,goal),cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue,(heuristic(neighbour,goal),cost + 1, path + direction, neighbour))
    return False

def single_astar_path(file):
    maze = Maze(file)
    maze.path(single_astar(file))
    maze.drawMaze()

def single_astar(file):
    maze = Maze(file)
    start, goal = (maze.startRow, maze.startCol), maze.prizesCor[0]
    cost = 0
    pr_queue = []
    heappush(pr_queue,(cost + heuristic(start,goal),cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue,(cost + heuristic(neighbour,goal),cost + 1, path + direction, neighbour))
    return False

def single_gbfs_path(file):
    maze = Maze(file)
    maze.path(single_gbfs(file))
    maze.drawMaze()

# def nearest_neighbour(points):
#     current = (maze.startRow,maze.startCol)
#     nn_points = []
#     while len(points) > 0:
#         next = points[0]
#         for point in points:
#             if heuristic(current, point) < heuristic(current,next):
#                 next = point
#         nn_points.append(next)
#         points.remove(next)
#         current = next
#     return nn_points

# def multi_astar(file):
#     maze = Maze(file)
#     current = (maze.startRow,maze.startCol)
#     goal = nearest_neighbour(maze.prizesCor)
#     cost = 0
#     pr_queue = []
#     visited = set()
#     graph = maze.maze2graph()
#     index = 0
#     subgoal = goal[index]
#     heappush(pr_queue, (cost + heuristic(current, subgoal), cost, "", current))
#     while pr_queue:
#         _, cost, path, current = heappop(pr_queue)
#         if current == subgoal:
#             if index == (len(goal) - 1):
#                 return path
#             else:
#                 index = index + 1
#
#     #         else:
#     #             goal.remove(subgoal)
#     #             index = index + 1
#     #
#         if current in visited:
#             continue
#         visited.add(current)
#         for direction, neighbour in graph[current]:
#             heappush(pr_queue, (cost + heuristic(neighbour, subgoal), cost + 1, path + direction, neighbour))
#     # return False

def multi_astar_util(start,subgoal):
    cost = 0
    pr_queue = []
    heappush(pr_queue, (cost + heuristic(start, subgoal), cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    while pr_queue:
        _, cost, path, current_in_util = heappop(pr_queue)
        if current_in_util == subgoal:
            return path , current_in_util
        if current_in_util in visited:
             continue
        visited.add(current_in_util)
        for direction, neighbour in graph[current_in_util]:
            heappush(pr_queue, (cost + heuristic(neighbour, subgoal), cost + 1, path + direction, neighbour))
    return False

def multi_astar(file):
    maze = Maze(file)
    goals = nearest_neighbour(maze.prizesCor)
    path = ""
    current = (maze.startRow,maze.startCol)
    for subgoal in goals:
        onepath , current_in_util = multi_astar_util(current,subgoal)
        path = path + "/" + onepath
        current = current_in_util
    return path

def multi_astar_path(file):
    maze.path(multi_astar(file))
    maze.drawMaze()

maze = Maze("multiprize-tiny.txt")
print(maze.prizesCor)
print(nearest_neighbour(maze.prizesCor))
print(multi_astar("multiprize-tiny.txt"))
print(multi_astar_path("multiprize-tiny.txt"))
#print(single_bfs_path("1prize-medium.txt"))
# multi_astar_path("multiprize-tiny.txt")
#single_bfs_path("1prize-large.txt")
# single_dfs_path("1prize-open.txt")
# single_astar_path("1prize-open.txt")
# single_gbfs_path("1prize-open.txt")
# multiple_astar("multiprize-tiny.txt")