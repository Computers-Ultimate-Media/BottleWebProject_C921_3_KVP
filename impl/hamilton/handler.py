from impl.algorithm_history import AlgorithmHistory
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

    result = HamiltonianAlgorithm(matrix).solve()

    if(len(result) != 0):
        AlgorithmHistory('Hamilton Algorithm', data, result).save()
        return json_dumps({'status': 'ok', 'result': result})
    else:
        AlgorithmHistory('Hamilton Algorithm', data, 'There is no Hamiltonian cycle in the graph').save()
        return json_dumps({'status': 'error', 'error': 'В графе нет Гамильнонова цикла'})