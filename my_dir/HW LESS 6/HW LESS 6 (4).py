import time
from functools import wraps
from typing import Callable


def decorator(func: Callable) -> Callable:
    @wraps(func)  # сохраняет имя и документацию изначальной функции, которую декорируем (в нашем случае это add)
    def inner(*args, **kwargs):
        print('до вызова функции add')
        time1 = time.time()
        result = func(*args, **kwargs)  # вот тут мы вызываем функцию, которую декорируем (в нашем случае это add)
        time2 = time.time()
        print(f'после вызова add, результат = {result}, время выполнения = {time2 - time1}')
        return result
    return inner
