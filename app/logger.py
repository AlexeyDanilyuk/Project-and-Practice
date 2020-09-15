import os
import time


def write_log(text):
    path = 'logs'
    with open(os.path.join(path, 'log_' + filename + '.txt'), 'a', encoding='utf-8') as log:
        local_time = time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime())
        log.write(f'{local_time}:{text}\n')


def debug(func):
    def debug_deco(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__call__}. Содержимое: {kwargs} Время выполнения: {end - start}')
        return result

    return debug_deco
