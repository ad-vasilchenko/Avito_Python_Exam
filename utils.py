import time
from typing import Callable


def time_report(str_in: str, str_out: str) -> Callable:
    """
    Этот декоратор выводит выводит комментарий о начале работе функции
    и о времени её работы
    """

    def outer_wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            print(str_in)
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time()
            time_elapsed = t2 - t1
            # Точно помню, что можно делать строки шаблоны, но за 2 минуты не нагуглил, поэтому так
            print(str_out.replace("{}", str(int(time_elapsed))))
            return result

        return inner_wrapper

    return outer_wrapper
