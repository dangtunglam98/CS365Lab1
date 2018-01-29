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

def single_astar_path(file):
    maze = Maze(file)
    maze.path(single_astar(file))
    maze.drawMaze()

single_bfs_path("1prize-medium.txt")
print("\n")
single_dfs_path("1prize-medium.txt")
print(single_astar("1prize-medium.txt"))
single_astar_path("1prize-medium.txt")