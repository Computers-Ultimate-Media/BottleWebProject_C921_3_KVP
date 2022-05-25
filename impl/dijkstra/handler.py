from bottle import route


@route('/example_get_route', method='get')
def example_get_route():
    return 'TODO'
