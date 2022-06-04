from impl.algorithm_history import AlgorithmHistory
from bottle import route, request
from impl.hamilton.hamiltonian_algorithm import HamiltonianAlgorithm

# post request handler for hamilton algorithm
@route('/hamilton_solver', method='post')
def hamilton_solver():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    matrix = data['matrix']

    # algorithm result 
    result = HamiltonianAlgorithm(matrix).solve()

    if(len(result) != 0):
        # history save
        AlgorithmHistory('Hamilton Algorithm', data, result).save()
        # response send
        return json_dumps({'status': 'ok', 'result': result})
    else:
        # history save
        AlgorithmHistory('Hamilton Algorithm', data, 'There is no Hamiltonian cycle in the graph').save()
        # response send
        return json_dumps({'status': 'error', 'error': 'В графе нет Гамильнонова цикла'})