import os
import time


class MessageWriter:
    def __init__(self, flag=False, filename=None):
        self.flag = flag
        self.filename = filename

    def write_log(self, text):
        if self.flag:
            path = 'logs'
            with open(os.path.join(path, 'log_' + self.filename + '.txt'), 'a', encoding='utf-8') as log:
                local_time = time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime())
                log.write(f'{local_time}:{text}\n')
        else:
            print(text)


def debug(func):
    def debug_deco(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__call__}. Содержимое: {kwargs} Время выполнения: {end - start}')
        return result

    return debug_deco
