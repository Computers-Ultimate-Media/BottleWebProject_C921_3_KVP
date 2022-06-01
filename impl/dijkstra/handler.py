from bottle import route, request
from impl.dijkstra.dijkstra_algorithm import DijkstraAlgorithm


@route('/dijkstra_solver', method='post')
def dijkstra_solver():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    matrix = data['matrix']
    vertex = data['vertex']

    try:
        dijkstra = DijkstraAlgorithm(matrix)
        result = dijkstra.solve(vertex)
    except Exception as e:
        return json_dumps({'error': 'Не удалось найти расстояния от этой вершины до других. Проверьте вашу матрицу'})

    return json_dumps({'status': 'ok', 'result': result})
