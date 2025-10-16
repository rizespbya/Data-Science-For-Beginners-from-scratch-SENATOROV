"""Задания к главе 4.3.

Рекурсия. Декораторы. Генераторы

Хендбук Яндекс "Основы Python".
"""

# A

from collections.abc import Generator

# +
from typing import Union


def recursive_sum(*nums: int) -> int:
    """Возвращает рекурсивную сумму переданных аргументов.

    Args:
    *nums (int): Целые числа.

    Returns:
        int: Сумма.
    """
    if len(nums) == 0:
        return 0

    return nums[-1] + recursive_sum(*nums[:-1])


# -

# B


def recursive_digit_sum(num: int) -> int:
    """Возвращает сумму цифр переданного числа.

    Args:
        num (int): Целое число.

    Returns:
        int: Сумма цифр переданного числа.
    """
    if num == 0:
        return 0

    return num % 10 + recursive_digit_sum(num // 10)


# C


def make_equation(*nums: int) -> str:
    """Возвращает многочлен N-ой степени.

    Для построения используются переданные коэффициенты.

    Args:
        *num (int): Целые числа.

    Returns:
        int: Многочлен N-ой степени.
    """
    if len(nums) == 1:
        return f"{nums[0]}"

    return f"({make_equation(*nums[:-1])}) * x + {nums[-1]}"


# D

# T = TypeVar("T")
# AnyFunction = Callable[..., T]
#
#
# def answer(fn: AnyFunction) -> Callable[[int,...], str]:
#     """
#     Декоратор, который оборачивает функцию.
#
#     Возвращает строку с результатом ее выполнения.
#
#     Добавляет префикс "Результат функции: " к строковому представлению
#     возвращаемого значения декорируемой функции.
#
#     Args:
#         fn (AnyFunction): Функция, которую нужно обернуть. Может принимать
#         любые позиционные и именованные аргументы (*args, **kwargs) и
#         возвращать значение любого типа.
#
#     Returns:
#         Callable[..., str]: Функция-обёртка.
#     """
#
#     def inner(*args, **kwargs):
#         return f"Результат функции: {fn(*args, **kwargs)}"
#
#     return inner

# E

# Method = Literal["accumulate", "drop"]
#
#
# def result_accumulator[Result](
#     fn: Callable[..., Result],
# ) -> Callable[..., list[Result] | None]:
#     """
#     Декоратор, который позволяет функции аккумулировать значения.
#
#     Args:
#         fn (Callable[..., Result]): Обрачиваемая функция.
#     Returns:
#         _type_: Функция, которая может аккумулировать значения.
#     """
#     queue: list[Result] = []
#
#     @wraps(fn)
#     def inner(
#         *args,
#         method: Method = "accumulate",
#         **kwargs,
#     ):
#         """
#         Функция, которая может аккумулировать значения.
#
#         Args:
#             method (Method, optional): Если передано 'accumulate', функция
#             накапливает значения. Если передано 'drop' - возвращает
#             массив накопленных значений и очищает накопленные результаты.
#             Defaults to "accumulate".
#
#         Returns:
#             _type_: Массив результатов.
#         """
#         if method == "accumulate":
#             queue.append(fn(*args, **kwargs))
#         if method == "drop":
#             queue.append(fn(*args, **kwargs))
#             result = list(queue)
#             queue.clear()
#
#             return result
#
#     return inner

# F


# +
def merge(left: list[int], right: list[int]) -> list[int]:
    """Функция для слияния двух отсортированных списков.

    Args:
        left (list[int]): Первый отсортированный список целых чисел.
        right (list[int]): Второй отсортированный список целых чисел.

    Returns:
        list[int]: Отсортированный список целых чисел.
    """
    result: list[int] = []
    pos_left = pos_right = 0

    while pos_left < len(left) and pos_right < len(right):
        if left[pos_left] < right[pos_right]:
            result.append(left[pos_left])
            pos_left += 1
        else:
            result.append(right[pos_right])
            pos_right += 1

    result += left[pos_left:]
    result += right[pos_right:]

    return result


def merge_sort(nums: list[int]) -> list[int]:
    """Функция для сортировки списка слиянием.

    Использует вспомогательную функцию merge, которая объединяет два
    отсортированных списка.

    Args:
        nums (list[int]): Несортированный список целых чисел.

    Returns:
        list[int]: Отсортированный список целых чисел.
    """
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2

    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    return merge(left, right)


# -

# G

# def same_type(fn):
#     """
#     Декоратор, который проверяет аргументы оборачиваемой функции.
#
#     Если аргументы одного типа, возвращает результат выполнения функции.
#     Если аргументы разного типа, выподит строку:
#     "Обнаружены различные типы данных"
#
#     Args:
#         fn (function): Оборачиваемая функция, которая принимает неограниченное
#         количество аргументов
#     """
#
#     def inner(*args):
#         if all(isinstance(arg, type(args[0])) for arg in args):
#             return fn(*args)
#
#         print("Обнаружены различные типы данных")
#
#     return inner

# H


def fibonacci(num: int) -> Generator[int, None, None]:
    """Функция возвращает num первых членов последовательности Фибоначчи.

    Первый член последовательности равен 0.

    Args:
        num (int): Целое число.

    Yields:
        Generator[int, None, None]: Целое число.
    """
    prev_prev = 0
    prev = 1

    for _ in range(num):
        yield prev_prev
        prev_prev, prev = prev, prev + prev_prev


# I


def cycle(nums: list[int]) -> Generator[int, None, None]:
    """Генератор зацикливает переданный список.

    Бесконечно возвращает следующий элемент списка.
    Если список закончился, начинает возвращать элементы с начала списка

    Args:
        nums (list[int]): Список целых чисел.

    Yields:
        Generator[int, None, None]: Целое число, элемент списка.
    """
    index = 0

    while True:
        yield nums[index]

        index = index + 1 if index < len(nums) - 1 else 0


# J

# +
IntList = Union[int, list["IntList"]]


def make_linear(items: list[IntList]) -> list[int]:
    """Распаковывает переданный список.

    Args:
        nums (list[list | int]): Список, состоящий из целых чисел или
        других списков.

    Yields:
        list[int]: Список целых чисел.
    """
    result: list[int] = []

    for item in items:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)

    return result
