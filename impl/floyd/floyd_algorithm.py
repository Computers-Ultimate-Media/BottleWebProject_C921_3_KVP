
from typing import List

class FloydAlgorithm:
	graph:		List[List[int]]
	shortest: 	List[List[int]]
	paths: 		List[List[int]]
	size:		int
	
	def __IncrementEachField(self):
		for i in range(self.size):
			for j in range(self.size):
				if(self.shortest[i][j] != float('inf') or self.paths != float('inf')):
					self.shortest[i][j] += 1
					self.paths[i][j] += 1


	def __FindWays(self):
		for i in range(self.size):
			for j in range(self.size):
				if(self.graph[i][j] == float('inf')):
					self.paths[i][j] = float('inf')
				else:
					self.paths[i][j] = j
					
	def __FloydShortestPaths(self):
		for k in range(self.size):
			for i in range(self.size):
				for j in range(self.size):
					if ((k != i) and (self.shortest[i][k] != float('inf')) and (k != j) and (self.shortest[k][j] != float('inf')) and (self.shortest[i][j] == float('inf') or (self.shortest[i][j] > self.shortest[i][k] + self.shortest[k][j]))):
						self.paths[i][j] = self.paths[i][k]
						self.shortest[i][j] = self.shortest[i][k] + self.shortest[k][j]
						
	
	def __init__(self, graph: List[List[int]]):
		self.size = len(graph)
		self.graph = graph
		self.shortest = graph
		self.paths = [[0 for _ in range(self.size)] for _ in range(self.size)]

	def solve(self): 
		self.__FindWays()
		self.__FloydShortestPaths()

		dict = {
			"shortest": self.shortest,
			"paths": self.paths
		}

		return dict
