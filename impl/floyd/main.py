from typing import List
from dijkstra_algorithm import DijkstraAlgorithm

def isHereWay(src: List[List[int]]) -> List[List[int]]:
	size = len(src[0])
	new = [[0 for _ in range(size)] for _ in range(size)]
	
	for i in range(size):
		for j in range(size):
			if (src[i][j] != float('inf')):
				new[i][j] = 1
	return new
	
	
test = [
[0,3,1,float('inf')],
[3,0,1,2],
[1,1,0,1],
[float('inf'),2,1,0],
]

print(test)
print(isHereWay(test))

n = 4

d = test
getMin = DijkstraAlgorithm(d)
s = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	for j in range(n):
		s[i][j] = j if d[i][j] == getMin.solve(i, j) else float('inf')

for k in range(n):
	for i in range(n):
		for j in range(n):
			if (d[i][k] < float('inf') and d[k][j] < float('inf')):
				#print(k+1,i+1,j+1, ": MIN <-", d[i][j], "vs (", d[i][k], "+", d[k][j], ") =", min(d[i][j], d[i][k] + d[k][j]))
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])
				

print(d)
print(s)