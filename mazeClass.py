class Maze:
	def __init__(self,filename):
		rowsNum = 0
		prizesNum = 0
		self.maze = []
		mazeFile = open(filename,'r')
		for line in mazeFile:
			rowList = []
			colsNum = 0
			for ch in line:
				rowList.append(ch)
				if ch == 'P':
					self.startRow = rowsNum
					self.startCol = colsNum
				if ch == '.':
					prizesNum = prizesNum + 1
				colsNum = colsNum + 1
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
		
		return graph

	def move(self,direction):
		xCor = self.currentXcor
		yCor = self.currentYcor
		currentPos = (xCor,yCor)
		if direction == "up":
			if self.maze[xCor - 1][yCor] == "%":
				return ("Blocked")
			else:
				xCor = xCor - 1
				currentPos = (xCor, yCor)
		elif direction == "down":
			if self.maze[xCor + 1][yCor] == "%":
				return "Blocked"
			else:
				xCor = xCor + 1
				currentPos = (xCor, yCor)
		if direction == "left":
			if self.maze[xCor][yCor - 1] == "%":
				return ("Blocked")
			else:
				yCor = yCor - 1
				currentPos = (xCor, yCor)
		if direction == "right":
			if self.maze[xCor][yCor + 1] == "%":
				return ("Blocked")
			else:
				yCor = yCor + 1
				currentPos = (xCor, yCor)
		self.currentXcor = xCor
		self.currentYcor = yCor
		return currentPos

maze = Maze("1prize-open.txt")
print(maze.maze2graph())



