from functools import wraps
from typing import Any, Callable

def loggerr(filename: str | None = None) -> Callable:
    def deco(func: Callable) -> Callable:

        def write_log(msg: str):
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(msg + "\n")
            else:
                print(msg)

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """ohsadla"""
            try:
                result = func(*args, **kwargs)
                msg = f"Функция {func.__name__} выполнена!"
                write_log(msg)
                return result
            except Exception as e:
                msg = (f"Функция {func.__name__} не выполнена! Произошла ошибка {type(e).__name__}: {e},"
                       f"входные параметры: {args, kwargs}.")
                write_log(msg)
                raise
        return wrapper
    return deco

@loggerr()
def foo(a: int, b: int):
    """Складывает два числа a и b"""
    return a + b

print(foo.__name__)