import quopri

from routes import routes


def decode_value(val):
    val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
    val_decode_str = quopri.decodestring(val_b)
    return val_decode_str.decode('UTF-8')


def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = decode_value(v)
    return result


def get_wsgi_input_data(env) -> bytes:
    # получаем длину тела
    content_length_data = env.get('CONTENT_LENGTH')
    # приводим к int
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные если они есть
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        # собираем их в словарь
        result = parse_input_data(data_str)
    return result


class Application:

    def __init__(self, route):
        self.routes = route

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        if method == 'POST':
            data = get_wsgi_input_data(environ)
            data = parse_wsgi_input_data(data)
        else:
            data = parse_input_data(environ['QUERY_STRING'])

        if not path.endswith('/'):
            path += '/'

        if path in self.routes:
            view = self.routes[path]
            request = {'method': method, 'data': data}
            code, body = view(request)

            start_response(code, [('Content-Type', 'text/html')])
            return [bytes(body, encoding='utf-8')]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'Not Found']


application = Application(routes)
