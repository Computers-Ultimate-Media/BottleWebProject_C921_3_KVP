from typing import List
from sys import maxsize


class DijkstraAlgorithm:
    graph: List[List[int]]

    # Creates Dijkstra instance
    def __init__(self, graph: List[List[int]]):
        self.graph = graph

    # Returns count of vertices in graph
    def vertices(self) -> int:
        return len(self.graph[0])

    # A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in the shortest path tree
    def min_distance(self, dist: List[int], spt_set: List[bool]):
        # Initialize minimum distance for next node
        min_val = maxsize
        min_index = -1

        # Search not the nearest vertex not in the shortest path tree
        for u in range(self.vertices()):
            if not spt_set[u] and dist[u] < min_val:
                min_val = dist[u]
                min_index = u

        return min_index

    # Finds the shortest distance from src index
    def solve(self, src: int, dst: int):
        # The output array. dist[i] will hold the shortest distance from src to i
        dist = [maxsize] * self.vertices()
        # spt_set[i] will be true if vertex i is included in the shortest path tree or shortest distance
        # from src to i is finalized
        spt_set = [False] * self.vertices()

        # Distance of source vertex from itself is always 0
        dist[src] = 0

        for _ in range(self.vertices()):
            # Pick the minimum distance vertex from the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.min_distance(dist, spt_set)

            # Put the minimum distance vertex in the shortest path tree
            spt_set[x] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than new distance and the vertex in not in the shortest path tree
            for y in range(self.vertices()):
                if self.graph[x][y] > 0 and not spt_set[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        if any(dist_val == maxsize for dist_val in dist):
            raise ValueError

        return dist[dst]
