from mazeClass import Maze
from collections import deque
from heapq import heappop, heappush

def single_bfs_util(maze):
    start, goal = (maze.startRow,maze.startCol), maze.prizesCor[0]
    queue = deque([("", start)])
    visited = set()
    graph = maze.maze2graph()
    nodeExpanded = 0
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path , nodeExpanded
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            nodeExpanded = nodeExpanded + 1
            queue.append((path  + direction, neighbour))
    return False

def single_bfs(file):
    maze = Maze(file)
    path , ExpNode = single_bfs_util(maze)
    maze.path(path)
    maze.drawMaze()
    print("The cost is " + str(len(path)))
    print("Number of Node Expanded is " + str(ExpNode))

def single_dfs_util(maze):
    start, goal = (maze.startRow,maze.startCol), maze.prizesCor[0]
    queue = deque([("", start)])
    visited = set()
    graph = maze.maze2graph()
    nodeExpanded = 0
    while queue:
        path, current = queue.pop()
        if current == goal:
            return path, nodeExpanded
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            nodeExpanded = nodeExpanded + 1
            queue.append((path + direction, neighbour))
    return False

def single_dfs(file):
    maze = Maze(file)
    path, nodeExpanded = single_dfs_util(maze)
    maze.path(path)
    maze.drawMaze()
    print("The cost is " + str(len(path)))
    print("Number of Node Expanded is " + str(nodeExpanded))

def heuristic(current,goal): #Manhattan
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def single_gbfs_util(maze):
    start, goal = (maze.startRow, maze.startCol), maze.prizesCor[0]
    cost = 0
    pr_queue = []
    heappush(pr_queue,(heuristic(start,goal),cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    nodeExpanded = 0
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path, nodeExpanded
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            nodeExpanded = nodeExpanded + 1
            heappush(pr_queue,(heuristic(neighbour,goal),cost + 1, path + direction, neighbour))
    return False

def single_gbfs(file):
    maze = Maze(file)
    path, nodeExpanded = single_gbfs_util(file)
    maze.path(path)
    maze.drawMaze()
    print("The cost is " + str(len(path)))
    print("Number of Node Expanded is " + str(nodeExpanded))

def single_astar_util(maze):
    start, goal = (maze.startRow, maze.startCol), maze.prizesCor[0]
    cost = 0
    pr_queue = []
    nodeExpanded = 0
    heappush(pr_queue,(cost + heuristic(start,goal),cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path , nodeExpanded
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            nodeExpanded = nodeExpanded + 1
            heappush(pr_queue,(cost + heuristic(neighbour,goal),cost + 1, path + direction, neighbour))
    return False

def single_astar(file):
    maze = Maze(file)
    path, nodeExpanded = single_astar_util(maze)
    maze.path(path)
    maze.drawMaze()
    print("The cost is " + str(len(path)))
    print("Number of Node Expanded is " + str(nodeExpanded))
