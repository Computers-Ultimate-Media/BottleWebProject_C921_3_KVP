import unittest
from impl.dijkstra.dijkstra_algorithm import DijkstraAlgorithm

class Test_test_dijkstra_algorithm(unittest.TestCase):
    def test_matrix_1(self):
        dijkstra = DijkstraAlgorithm([
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0],
        ])
        self.assertEqual(dijkstra.solve(0), [0, 4, 12, 19, 21, 11, 9, 8, 14])
        self.assertEqual(dijkstra.solve(1), [4, 0, 8, 15, 22, 12, 12, 11, 10])
        self.assertEqual(dijkstra.solve(2), [12, 8, 0, 7, 14, 4, 6, 7, 2])
        self.assertEqual(dijkstra.solve(3), [19, 15, 7, 0, 9, 11, 13, 14, 9])
        self.assertEqual(dijkstra.solve(4), [21, 22, 14, 9, 0, 10, 12, 13, 16])
        self.assertEqual(dijkstra.solve(5), [11, 12, 4, 11, 10, 0, 2, 3, 6])
        self.assertEqual(dijkstra.solve(6), [9, 12, 6, 13, 12, 2, 0, 1, 6])
        self.assertEqual(dijkstra.solve(7), [8, 11, 7, 14, 13, 3, 1, 0, 7])
        self.assertEqual(dijkstra.solve(8), [14, 10, 2, 9, 16, 6, 6, 7, 0])

if __name__ == '__main__':
    unittest.main()
