def convert_list_to_square_matrix(arr:list, size:int) -> list:
    A = []
    for i in range(size):
        A.append(arr[size * i : size * i + size])

    return A

def isCorrectMatrix(matrix:list) -> bool:
    return all (len (row) == len (matrix) for row in matrix)