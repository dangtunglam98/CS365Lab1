from mazeClass import Maze
from collections import deque

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

single_bfs_path("1prize-medium.txt")
print("\n")
single_dfs_path("1prize-medium.txt")