
from bottle import route, request
from impl.hamilton.hamiltonian_algorithm import HamiltonianAlgorithm

@route('/example_get_route', method='get')
def example_get_route():
    return 'TODO'


@route('/hamilton_solver', method='post')
def hamilton_solver():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    matrix = data['matrix']

    hamilton = HamiltonianAlgorithm(matrix)
    result = hamilton.solve(vertex)

    print(result)

    return json_dumps({'status': 'ok', 'result': result})