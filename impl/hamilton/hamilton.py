import sys
sys.path.append('../')

from utils import convert_list_to_square_matrix

def hamilton(matrix: list) -> list:
	n = len(matrix)
	Visited = [False] * n
	Path = []

	def hasHamiltonianCycle(start_edge_num: int) -> bool:
	    Path.append(start_edge_num)
	    if len(Path) == n:
	        if A[Path[0]][Path[-1]] == 1:
	            return True 
	        else: 
	            Path.pop() 
	            return False 
	    Visited[start_edge_num] = True
	    for next in range(n): 
	        if A[start_edge_num][next] == 1 and not Visited[next]: 
	            if hasHamiltonianCycle(next): 
	                return True 
	    Visited[start_edge_num] = False 
	    Path.pop()
	    return False

	hasHamiltonianCycle(0)
	return Path