from typing import List
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
        visited = [False] * self.vertices()
        path = []

        def hasHamiltonianCycle(start_edge_num: int) -> bool:
            path.append(start_edge_num)
            if len(path) == self.vertices():
                if A[path[0]][path[-1]] == 1:
                    return True 
                else: 
                    path.pop() 
                    return False 
            visited[start_edge_num] = True
            for next in range(self.vertices()): 
                if A[start_edge_num][next] == 1 and not visited[next]: 
                    if hasHamiltonianCycle(next): 
                        return True 
            visited[start_edge_num] = False 
            path.pop()
            return False

        hasHamiltonianCycle(0)
        return path