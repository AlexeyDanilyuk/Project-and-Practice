"""
Запуск приложения
=================
uwsgi --http :8000 --enable-threads --thunder-lock --wsgi-file main.py

или

gunicorn main:application
"""
import quopri

from app import routes


class Application(object):
    def add_route(self, url):
        def inner(view):
            self.routes[url] = view

        return inner

    def decode_value(self, val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('UTF-8')

    def parse_input_data(self, data: str):
        result = {}
        if data:
            # делим параметры через &
            params = data.split('&')
            for item in params:
                # делим ключ и значение через =
                k, v = item.split('=')
                result[k] = self.decode_value(v)
        return result

    def get_wsgi_input_data(self, env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def __init__(self, route):
        self.routes = route

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        if method == 'POST':
            data = self.parse_wsgi_input_data(self.get_wsgi_input_data(environ))
        else:
            data = self.parse_input_data(environ['QUERY_STRING'])

        if not path.endswith('/'):
            path += '/'

        if path in self.routes:
            view = self.routes[path]
            request = {'method': method, 'data': data}
            print(request['data'])
            code, body = view(request)

            start_response(code, [('Content-Type', 'text/html')])
            return [bytes(body, encoding='utf-8')]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'Not Found']


class DebugApplication(Application):

    def __init__(self, route):
        self.application = Application(route)
        super().__init__(route)

    def __call__(self, env, start_response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, start_response)


application = Application(routes.rule)
