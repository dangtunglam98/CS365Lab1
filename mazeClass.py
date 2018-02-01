
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
						#ch = ' '
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
		"""Return a Graph based on the given maze"""
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

	def move(self, direction):
		"""Move Agent in the Maze"""
		xCor = self.currentXcor
		yCor = self.currentYcor
		currentPos = (xCor, yCor)
		if direction == "N":
			if self.maze[xCor - 1][yCor] == "%":
				return ("Blocked")
			else:
				xCor = xCor - 1
				currentPos = (xCor, yCor)
				self.maze[xCor][yCor] = '#'
		elif direction == "S":
			if self.maze[xCor + 1][yCor] == "%":
				return currentPos
			else:
				xCor = xCor + 1
				currentPos = (xCor, yCor)
				self.maze[xCor][yCor] = '#'
		if direction == "W":
			if self.maze[xCor][yCor - 1] == "%":
				return currentPos
			else:
				yCor = yCor - 1
				currentPos = (xCor, yCor)
				self.maze[xCor][yCor] = '#'
		if direction == "E":
			if self.maze[xCor][yCor + 1] == "%":
				return currentPos
			else:
				yCor = yCor + 1
				currentPos = (xCor, yCor)
				self.maze[xCor][yCor] = '#'
		self.currentXcor = xCor
		self.currentYcor = yCor
		return currentPos

	def path(self, str):
		for ch in str:
			self.move(ch)

	def drawMaze(self):
		for row in self.maze:
			print(''.join(row))

