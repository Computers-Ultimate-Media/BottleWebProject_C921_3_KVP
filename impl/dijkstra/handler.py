from bottle import route, request
from impl.dijkstra.dijkstra_algorithm import DijkstraAlgorithm


@route('/dijkstra_solver', method='post')
def dijkstra_solver():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    matrix = data['matrix']
    vertex = data['vertex']

    dijkstra = DijkstraAlgorithm(matrix)
    result = dijkstra.solve(vertex)

    return json_dumps({'status': 'ok', 'result': result})
