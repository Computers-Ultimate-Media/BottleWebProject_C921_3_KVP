from bottle import route, request
from impl.algorithm_history import AlgorithmHistory
from impl.floyd.floyd_algorithm import FloydAlgorithm

@route('/floyd_solver', method='post')
def floyd_solver():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    matrix = data['matrix']
    #vertex = data['vertex']

    try:
        floyd = FloydAlgorithm(matrix)
        result = floyd.solve()
    except ValueError:
        return json_dumps({'error': 'Не удалось найти расстояния от этой вершины до других. Проверьте вашу матрицу'})

    AlgorithmHistory('floyd', data, result).save()

    return json_dumps({'status': 'ok', 'result': result})
