import templator


class IndexView:
    def __init__(self):
        self.template_name = 'index.html'

    def __call__(self, request):
        request = {
            'title': 'Стартовая страница',
            'header_name': 'Стартовая страница',
        }
        return '200 OK', templator.render(self.template_name, content=request)


class AboutView:
    def __init__(self):
        self.template_name = 'about.html'

    def __call__(self, request):
        request = {
            'title': 'О проекте',
            'header_name': 'Информация о проекте',
            'name': 'Алексей',
        }
        return '200 OK', templator.render(self.template_name, content=request)


class NotFoundPage:
    def __init__(self):
        self.template_name = '404.html'

    def __call__(self, request):
        request = {
            'title': '404',
            'header_name': 'Страница не найдена!!!',
        }
        return '400 Not Found', templator.render(self.template_name, content=request)
