import views

routes = {
    '/': views.IndexView(),
    '/about/': views.AboutView(),
}


class Application:

    def __init__(self, route):
        self.routes = route

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path += '/'
        view = views.NotFoundPage()

        if path in self.routes:
            view = self.routes[path]
        request = {}

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [bytes(body, encoding='utf-8')]


application = Application(routes)
