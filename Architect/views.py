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


class NotFoundPageView:
    def __init__(self):
        self.template_name = '404.html'

    def __call__(self, request):
        request = {
            'title': '404',
            'header_name': 'Страница не найдена!!!',
        }
        return '400 Not Found', templator.render(self.template_name, content=request)


class ContactPageView:
    def __init__(self):
        self.template_name = 'contacts.html'

    def __call__(self, request):
        print(request)
        if request['method'] == 'POST':
            method = request['method']
            data = request['data']
            text = request['data']['message_text']
            email = request['data']['email']
            name = request['data']['name']
            print(f'Вызван метод {method}. Данные в методе: {data}')
            with open('message.txt', 'a', encoding='utf-8') as file:
                file.write(f'Сообщение от пользователя {name}: {text}\n')
        content = {
            'title': 'Контакты',
        }

        return '200 OK', templator.render(self.template_name, content=content)
