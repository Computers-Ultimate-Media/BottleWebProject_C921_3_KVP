def convert_list_to_square_matrix(arr:list, size:int) -> list:
    A = []
    for i in range(size):
        A.append(arr[size * i : size * i + size])

    return A

def isCorrectMatrix(matrix:list) -> bool:
    if type(matrix) is not list:
        return False

    if len(matrix) == 0:
        return False
    if type(matrix[0]) is not list:
        return False

    return all (len (row) == len (matrix) for row in matrix)