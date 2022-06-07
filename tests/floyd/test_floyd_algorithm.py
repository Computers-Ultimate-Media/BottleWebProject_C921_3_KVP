import unittest
from impl.floyd.floyd_algorithm import FloydAlgorithm
from impl.utils import convert_list_to_square_matrix

test_example_1 = [
[0,2,3,-1],
[2,0,-1,-1],
[3,-1,0,1],
[-1,-1,1,0],
]

result_example_1_sh = [
[0,2,3,4],
[2,0,5,6],
[3,5,0,1],
[4,6,1,0],
]

result_example_1_ps = [
[0,1,2,2],
[0,1,0,0],
[0,0,2,3],
[2,2,2,3],
]

class Test_test_floyd_algorithm(unittest.TestCase):
    def test_shortests(self):
        result = FloydAlgorithm(test_example_1)
        result.solve()
        self.assertEqual(result.shortest, result_example_1_sh)

    def test_paths(self):
        result = FloydAlgorithm(test_example_1)
        result.solve()
        self.assertEqual(result.paths, result_example_1_ps)

if __name__ == '__main__':
    unittest.main()
