import os
import time


def logger(filename, data):
    path = 'logs'
    with open(os.path.join(path, 'log_' + filename + '.txt'), 'a', encoding='utf-8') as log:
        local_time = time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime())
        log.write(f'{local_time}: {data}\n')


class Course:
    def __init__(self, coursename, description='Без описания'):
        self.coursename = coursename
        self.description = description

    @staticmethod
    def create_course(data):
        print('Метод создания учебного курса')
        logger(filename='create', data=f'Создана тема учебного курса \'{data}\'')

    @staticmethod
    def select_course(data):
        print('Метод выбора учебного курса')
        logger(filename='select', data=f'Выбран учебный курс \'{data}\'')
