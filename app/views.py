from app import templator
from app.logger import debug, MessageWriter


class IndexView:
    def __init__(self):
        self.template_name = 'index.html'

    @debug
    def __call__(self, request):
        content = {
            'title': 'Главная страница',
            'header_name': 'Главная страница',
        }
        return '200 OK', templator.render(self.template_name, content=content)


class AboutView:
    def __init__(self):
        self.template_name = 'about.html'

    @debug
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

    @debug
    def __call__(self, request):
        request = {
            'title': '404',
            'header_name': 'Страница не найдена!!!',
        }
        return '400 Not Found', templator.render(self.template_name, content=request)


class ContactPageView:
    def __init__(self):
        self.template_name = 'contacts.html'

    @debug
    def __call__(self, request):
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


class CoursePageView:
    def __init__(self):
        self.template_name = 'courses.html'
        self.title = 'Учебные курсы'
        self.course_lst = []

    def __call__(self, request):

        if request['method'] == 'POST':
            self.course_lst.append('Новый курс')
        else:
            print(f'{request["method"]}')

        return '200 OK', templator.render(self.template_name, title=self.title, course_lst=self.course_lst)


class RegisterView:
    def __init__(self):
        self.template_name = 'register.html'

    @debug
    def __call__(self, request):
        request = {
            'title': 'Регистрация',
            'header_name': 'Регистрация студента',
        }

        return '200 OK', templator.render(self.template_name, content=request)
