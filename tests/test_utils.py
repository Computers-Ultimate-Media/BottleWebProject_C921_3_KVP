import unittest
from impl.utils import convert_list_to_square_matrix, isCorrectMatrix

# error matrix
class Test_error_input_isCorrectMatrix(unittest.TestCase):
    # not matrix
    def test_not_matrix_int(self):
        self.assertEqual(isCorrectMatrix(1), False)

    # not matrix
    def test_not_matrix_str(self):
        self.assertEqual(isCorrectMatrix(''), False)

    # not matrix
    def test_empty_list(self):
        self.assertEqual(isCorrectMatrix([]), False)

    # not sqaure
    def test_not_square_matrix(self):
        self.assertEqual(isCorrectMatrix([[]]), False)


# mini matrix 
class Test_minimum_nodes_isCorrectMatrix(unittest.TestCase):

    # empty matrix
    def test_one_node_matrix(self):
        self.assertEqual(isCorrectMatrix([[]]), False)

    # 2 nodes, none sqaure
    def test_two_nodes_none_sqaure_1(self):
        self.assertEqual(isCorrectMatrix([[1, 0]]), False)

    # 2 nodes, none sqaure
    def test_two_nodes_none_sqaure_2(self):
        self.assertEqual(isCorrectMatrix([[1],[0]]), False)

# three nodes matrix
class Test_three_nodes_isCorrectMatrix(unittest.TestCase):

    # empty matrix, no cycel
    def test_emply_matrix(self):
        self.assertEqual(isCorrectMatrix(
            [[0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0]]), True)


# matrix convertation 
class Test_three_nodes_convert_list_to_square_matrix(unittest.TestCase):

    # matrix convert
    def test_three_matrix_convert_1(self):
        self.assertEqual(
            convert_list_to_square_matrix(
                                        [0, 0, 0, 
                                        0, 0, 0, 
                                        0, 0, 0], 3) ==
                                        [[0, 0, 0], 
                                        [0, 0, 0],
                                        [0, 0, 0]], True)
    # matrix convert
    def test_three_matrix_convert_2(self):
        self.assertEqual(
            convert_list_to_square_matrix(
                                        [0, 0, 
                                        0, 0], 2) ==
                                        [[0, 0], 
                                        [0, 0]], True)