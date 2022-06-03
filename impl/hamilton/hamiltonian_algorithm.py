from typing import List
from impl.utils import isCorrectMatrix

class HamiltonianAlgorithm:
    graph: List[List[int]]

    # Creates Hamiltonian instance
    def __init__(self, graph: List[List[int]]):
        self.graph = graph

    # Returns count of vertices in graph
    def vertices(self) -> int:
        return len(self.graph[0])

    # Finds distance by all vertices
    def solve(self):
        if(not isCorrectMatrix(self.graph)):
            return []
        # if matrix size is 2, it can't has a cycle
        if(len(self.graph) == 2):
            return []

        visited = [False] * self.vertices()
        path = []

        def hasHamiltonianCycle(start_node_num: int) -> bool:
            path.append(start_node_num)
            if len(path) == self.vertices():
                if self.graph[path[0]][path[-1]] == 1:
                    return True 
                else: 
                    path.pop() 
                    return False 
            visited[start_node_num] = True
            for next in range(self.vertices()): 
                if self.graph[start_node_num][next] == 1 and not visited[next]: 
                    if hasHamiltonianCycle(next): 
                        return True 
            visited[start_node_num] = False 
            path.pop()
            return False

        hasHamiltonianCycle(0)
        path = [x+1 for x in path]
        return path