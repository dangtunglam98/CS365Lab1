from mazeClass import Maze
from heapq import heappop, heappush

def heuristic(current,goal): #Manhattan Distance
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def mincost_multi_heuristic(start,goal,maze):
    """ Return the cost between two points """
    cost = 0
    pr_queue = []
    heappush(pr_queue,(cost + heuristic(start,goal),cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue,(cost + heuristic(neighbour,goal),cost + 1, path + direction, neighbour))
    return False

def nearest_neighbour(maze):
    """ Return the order of prizes based on minimum cost """
    current = (maze.startRow,maze.startCol)
    points = maze.prizesCor
    nn_points = []
    while len(points) > 0:
        next = points[0]
        for point in points:
            if mincost_multi_heuristic(current,point,maze) < mincost_multi_heuristic(current,next,maze):
                next = point
        nn_points.append(next)
        points.remove(next)
        current = next
    return nn_points

def multi_astar_single(start,subgoal,maze):
    """ Find the least-cost path to get from one subprize to another """
    cost = 0
    pr_queue = []
    heappush(pr_queue, (cost + heuristic(start, subgoal), cost, "", start))
    visited = set()
    graph = maze.maze2graph()
    nodeExpanded = 0
    while pr_queue:
        _, cost, path, current_in_util = heappop(pr_queue)
        if current_in_util == subgoal:
            return path , current_in_util , nodeExpanded
        if current_in_util in visited:
            continue
        visited.add(current_in_util)
        for direction, neighbour in graph[current_in_util]:
            nodeExpanded = nodeExpanded + 1
            heappush(pr_queue, (cost + heuristic(neighbour, subgoal), cost + 1, path + direction, neighbour))
    return False

def multi_astar_util(maze):
    """ Return the least-cost path to get all the prizes using the Minimum-Cost Path """
    goals = nearest_neighbour(maze)
    path = ""
    order = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    current = (maze.startRow,maze.startCol)
    Expandednodes = 0
    for subgoal in goals:
        onepath , current_in_util, nodeEx = multi_astar_single(current,subgoal,maze)
        path = path  +onepath
        current = current_in_util
        (x,y) = current_in_util
        maze.maze[x][y] = order.pop(0)
        Expandednodes = Expandednodes + nodeEx
    return path , Expandednodes

def multi_astar(file):
    """ Return an output file for the function """
    maze = Maze(file)
    path, ExpNode = multi_astar_util(maze)

    output = open("multi_astar_output.txt","a")
    output.write("----------------------------------------------------------------------------------------\n")
    output.write("Multi ASTAR for " + file + "\n")
    for row in maze.maze:
        output.write(''.join(row))
        output.write("\n")
    output.write("The cost is " + str(len(path)) + "\n")
    output.write("Number of Nodes Expanded is " + str(ExpNode) + "\n")
    output.write("\n")