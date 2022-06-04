import unittest
from impl.hamilton.hamiltonian_algorithm import HamiltonianAlgorithm
from impl.utils import convert_list_to_square_matrix


# error matrix, has no cycel
class Test_error_input_hamilton_algorithm(unittest.TestCase):
    # not matrix
    def test_not_matrix_int(self):
        hamilton = HamiltonianAlgorithm(1)
        self.assertEqual(hamilton.solve(), [])

    # not matrix
    def test_not_matrix_str(self):
        hamilton = HamiltonianAlgorithm('')
        self.assertEqual(hamilton.solve(), [])


    # not matrix
    def test_empty_list(self):
        hamilton = HamiltonianAlgorithm(
            []
            )
        self.assertEqual(hamilton.solve(), [])


    # not square, no cycel
    def test_not_square_matrix(self):
        hamilton = HamiltonianAlgorithm(
            [[]]
            )
        self.assertEqual(hamilton.solve(), [])


# mini matrix 
class Test_minimum_nodes_hamilton_algorithm(unittest.TestCase):

    # empty matrix, no cycel
    def test_emply_matrix(self):
        hamilton = HamiltonianAlgorithm(
            [[0, 0],
            [0, 0]
            ])
        self.assertEqual(hamilton.solve(), [])

    # 2 nodes can't forms cycel
    def test_two_nodes(self):
        hamilton = HamiltonianAlgorithm(
            [[0, 1],
            [1, 0]
            ])
        self.assertEqual(hamilton.solve(), [])

    # single node forms cycel
    def test_one_node(self):
        hamilton = HamiltonianAlgorithm(
            [[1]]
            )
        self.assertEqual(hamilton.solve(), [1])

# three nodes matrix
class Test_three_nodes_hamilton_algorithm(unittest.TestCase):

    # empty matrix, no cycel
    def test_emply_matrix(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 0, 0, 
            0, 0, 0, 
            0, 0, 0], 3))
        self.assertEqual(hamilton.solve(), [])

    # no cycel
    def test_no_cycel_1(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 1, 0, 
            0, 0, 1, 
            0, 0, 0], 3))
        self.assertEqual(hamilton.solve(), [])

    # 2 of 3 vertices have a connection, no cycel
    def test_one_node(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 1, 0, 
            1, 0, 1, 
            0, 1, 0], 3))
        self.assertEqual(hamilton.solve(), [])

    # 3 of 3 vertices have a connection, cycel
    def test_three_nodes(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 1, 1, 
            1, 0, 1, 
            1, 1, 0], 3))
        self.assertEqual(hamilton.solve(), [1, 2, 3])


# five nodes matrix
class Test_five_nodes_hamilton_algorithm(unittest.TestCase):
    # empty matrix, no cycel
    def test_empty_matrix(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0], 5))
        self.assertEqual(hamilton.solve(), [])

    # no cycel
    def test_no_cycle_1(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 0, 1, 0, 0, 
            0, 0, 0, 0, 0, 
            1, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 
            0, 0, 1, 0, 0], 5))
        self.assertEqual(hamilton.solve(), [])

    # no cycel
    def test_no_cycle_2(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 0, 1, 0, 0, 
            0, 0, 0, 1, 0, 
            1, 1, 0, 1, 1, 
            0, 1, 0, 0, 0, 
            0, 0, 1, 0, 0], 5))
        self.assertEqual(hamilton.solve(), [])

    # all nodes has a two connections, cycel
    def test_minimum_nodes_consistent_way(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 1, 0, 0, 1, 
            1, 0, 1, 0, 0, 
            0, 1, 0, 1, 0, 
            0, 0, 1, 0, 1, 
            1, 0, 0, 1, 0], 5))
        self.assertEqual(hamilton.solve(), [1, 2, 3, 4, 5])

    # all nodes has a two random connections, cycel
    def test_minimum_nodes_complicated_way(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 0, 1, 1, 0, 
            0, 0, 0, 1, 1, 
            1, 0, 0, 0, 1, 
            1, 1, 0, 0, 0, 
            0, 1, 1, 0, 0], 5))
        self.assertEqual(hamilton.solve(), [1, 3, 5, 2, 4])

    # all nodes has several random connections, cycel
    def test_default_one_way(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 1, 0, 1, 0, 
            1, 0, 1, 0, 0, 
            0, 1, 0, 0, 1, 
            1, 0, 0, 0, 1, 
            0, 0, 1, 1, 0], 5))
        self.assertEqual(hamilton.solve(), [1, 2, 3, 5, 4])

    # all nodes has several random connections, cycel
    def test_default_several_way(self):
        hamilton = HamiltonianAlgorithm(
            convert_list_to_square_matrix(
            [0, 1, 0, 1, 0, 
            1, 0, 1, 0, 0, 
            0, 1, 0, 0, 1, 
            1, 0, 0, 0, 1, 
            0, 0, 1, 1, 0], 5))
        self.assertEqual(hamilton.solve(), [1, 2, 3, 5, 4])


if __name__ == '__main__':
    unittest.main()