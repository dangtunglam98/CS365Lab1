from collections import deque
class Maze:
	def __init__(self,filename):
		rowsNum = 0
		prizesNum = 0
		self.maze = []
		self.prizesCor = []
		mazeFile = open(filename,'r')
		for line in mazeFile:
			rowList = []
			colsNum = 0
			for ch in line:
				if ch != '\n':
					if ch == 'P':
						ch = ' '
						self.startRow = rowsNum
						self.startCol = colsNum
					if ch == '.':
						ch = ' '
						prizesNum = prizesNum + 1
						self.prizesCor.append((rowsNum,colsNum))
					colsNum = colsNum + 1
					rowList.append(ch)
			rowsNum = rowsNum + 1
			self.maze.append(rowList)

		self.rowsNum = rowsNum
		self.colsNum = len(self.maze[0])
		self.prizesNum = prizesNum
		self.currentXcor = self.startRow
		self.currentYcor = self.startCol

	def getMaze(self):
		return self.maze

	def maze2graph(self):
		#graph = {(i,j):[] for j in range (self.colsNum) for i in range (self.rowsNum) if not self.maze[i-1][j-1]}
		graph = {}
		for j in range(self.colsNum-1):
			for i in range(self.rowsNum-1):
				if self.maze[i][j] != "%":
					graph.update({(i,j):[]})
		for row , col in graph.keys():
			if row < self.rowsNum - 1 and self.maze[row+1][col] != "%":
				graph[(row,col)].append(("S",(row+1,col)))
				graph[(row+1),col].append(("N",(row,col)))
			if col < self.colsNum - 1 and self.maze[row][col+1] != "%":
				graph[(row,col)].append(("E",(row,col+1)))
				graph[(row,col+1)].append(("W",(row,col)))
		return graph

	def single_bfs(self):
		start, goal = (self.startRow,self.startCol), self.prizesCor[0]
		queue = deque([("", start)])
		visited = set()
		graph = self.maze2graph()
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

	def single_dfs(self):
		start, goal = (self.startRow, self.startCol), self.prizesCor[0]
		stack = deque([("", start)])
		visited = set()
		graph = self.maze2graph()
		while stack:
			path, current = stack.pop()
			if current == goal:
				return path
			if current in visited:
				continue
			visited.add(current)
			for direction, neighbour in graph[current]:
				stack.append((path + direction, neighbour))

			#print((currentRow,currentCol))

	def move(self, direction):
		xCor = self.currentXcor
		yCor = self.currentYcor
		currentPos = (xCor, yCor)
		if direction == "N":
			if self.maze[xCor - 1][yCor] == "%":
				return ("Blocked")
			else:
				self.maze[xCor][yCor] = '#'
				xCor = xCor - 1
				currentPos = (xCor, yCor)
		elif direction == "S":
			if self.maze[xCor + 1][yCor] == "%":
				return currentPos
			else:
				self.maze[xCor][yCor] = '#'
				xCor = xCor + 1
				currentPos = (xCor, yCor)
		if direction == "W":
			if self.maze[xCor][yCor - 1] == "%":
				return currentPos
			else:
				self.maze[xCor][yCor] = '#'
				yCor = yCor - 1
				currentPos = (xCor, yCor)
		if direction == "E":
			if self.maze[xCor][yCor + 1] == "%":
				return currentPos
			else:
				self.maze[xCor][yCor] = '#'
				yCor = yCor + 1
				currentPos = (xCor, yCor)
		self.currentXcor = xCor
		self.currentYcor = yCor
		return currentPos

	def path(self, str):
		for ch in str:
			self.move(ch)

	def drawMaze(self):
		for row in self.maze:
			print(''.join(row))

maze = Maze("1prize-open.txt")
print(maze.maze2graph())
print(maze.startRow)
print(maze.startCol)
print(maze.single_bfs())
print(maze.single_dfs())
maze.path(maze.single_bfs())
maze.drawMaze()
