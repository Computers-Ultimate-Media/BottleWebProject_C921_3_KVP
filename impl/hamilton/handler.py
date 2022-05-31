from bottle import route, view, post, request, redirect

import sys
sys.path.append('../')

from utils import isCorrectMatrix
from hamilton import hamilton

@post('/hamilton', method='post')
def hamilton():
    matrix = request.params.matrix
    
    if not isCorrectMatrix(matrix):
        print('Матрица не квадратная')
        return

    path = hamilton(matrix)

    if(len(path) != 0)
        # todo: результат, путь есть
        redirect('/results', path)
    else 
        # todo: результат, пути нет
        redirect('/results')

