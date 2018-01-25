class Maze:
	def __init__(self,filename):
		rowsNum = 0
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
				colsNum = colsNum + 1
			rowsNum = rowsNum + 1
			self.maze.append(rowList)

		self.rowsNum = rowsNum
		self.colsNum = len(self.maze[0])
	def getMaze(self):
		return self.maze

def main():
	maze = Maze("1prize-open.txt")
	maze.getMaze()

main()

