
from typing import List

class FloydAlgorithm:
	graph:		List[List[int]]
	shortest: 	List[List[int]]
	paths: 		List[List[int]]
	size:		int
	
	def __FindWays(self):
		for i in range(self.size):
			for j in range(self.size):
				if(self.graph[i][j] == -1):
					self.paths[i][j] = -1
				else:
					self.paths[i][j] = j
					
	def __FloydShortestPaths(self):
		for k in range(self.size):
			for i in range(self.size):
				for j in range(self.size):
					if ((k != i) and (self.shortest[i][k] != -1) and (k != j) and (self.shortest[k][j] != -1) and (self.shortest[i][j] == -1 or (self.shortest[i][j] > self.shortest[i][k] + self.shortest[k][j]))):
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
