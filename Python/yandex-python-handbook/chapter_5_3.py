"""Задания к главе 5.3.

Модель исключений Python. Try, except, else, finally. Модули

Хендбук Яндекс "Основы Python".
"""

# A

# +
from hashlib import sha256
from re import fullmatch
from typing import Any, Callable


def func(*args: Any) -> None:  # type: ignore
    """Функция-заглушка."""
    print(args)


try:
    func()
except ValueError:
    print(ValueError.__name__)
except TypeError:
    print(TypeError.__name__)
except SystemError:
    print(SystemError.__name__)
else:
    print("No Exceptions")
# -

# B

# Предложите вызов функции, который гарантированно породит ошибку внутри функции.
func(1, None)


# C


# +
class EmptyClass:
    """Класс-заглушка.

    Генерирует ошибку при попытке приведения к строке
    """

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта.

        Raises:
            TypeError: Всегда вызывается, чтобы сигнализировать, что метод
            не реализован в текущем классе.
        """
        raise TypeError()


obj = EmptyClass()
func(obj)


# -

# D


def only_positive_even_sum(num1: int, num2: int) -> int:
    """Функция возвращает сумму двух переданных аргументов.

    Ожидает целые положительные четные числа.

    Args:
        num1 (int): Целое число.
        num2 (int): Целое число.

    Returns:
        int: Сумма аргументов.

    Raises:
        TypeError: Если один из параметров не является целым числом.
        ValueError: Если один из параметров не является положительным
        чётным числом.
    """
    args = [num1, num2]

    if any(not isinstance(arg, int) for arg in args):
        raise TypeError()

    if any(arg % 2 == 1 or arg <= 0 for arg in args):
        raise ValueError()

    return num1 + num2


# E


def merge(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple[int, ...]:
    """Объединяет два отсортированных кортежа в один отсортированный.

    Args:
        tuple1 (tuple[int, ...]): Первый кортеж отсортированных чисел.
        tuple1 (tuple[int, ...]): Второй кортеж отсортированных чисел.

    Returns:
        tuple[int, ...]: Отсортированный по возрастанию Кортеж целых чисел,
        содержащий все числа из первого и второго кортежа

    Raises:
        StopIteration: Если один из параметров не является итерируемым
        объектом.
        TypeError: Если значения входных параметров содержат «неоднородные»
        данные.
        ValueError: Если один из параметров не отсортирован.
    """
    args = [tuple1, tuple2]
    if any(not hasattr(arg, "__iter__") for arg in args):
        raise StopIteration()

    if any(sorted(arg) != list(arg) for arg in args):
        raise ValueError()

    list1 = list(tuple1)
    list2 = list(tuple2)

    result: list[int] = []

    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

    result.extend(list1)
    result.extend(list2)

    expected_type = type(result[0])
    if any(not isinstance(item, expected_type) for item in result):
        raise TypeError()

    return tuple(result)


# F


# +
class NoSolutionsError(Exception):
    """Ошибка отсутствия корней квадратного уравнения."""


class InfiniteSolutionsError(Exception):
    """Ошибка: бесконечное количество корней квадратного уравнения."""


def find_roots(
    a_coef: float | int,
    b_coef: float | int,
    c_coef: float | int,
) -> tuple[float, ...]:
    """Функция для поиска корней квадратного уравнения.

    Принимает коэффициенты квадратного уравнения.

    Args:
        a_coef (float | int): коэффициент a.
        b_coef (float | int): коэффициент b.
        c_coef (float | int): коэффициент c.

    Raises:
        TypeError: Если переданные коэффициенты не являются рациональными
        числами.
        InfiniteSolutionsError: Бесконечное количества решений.
        NoSolutionsError: Отсутствие решений.

    Returns:
        tuple[float, ...]: Отсортированный кортеж корней квадратного уравнения.
    """
    args = [a_coef, b_coef, c_coef]
    if not all(type(arg) in (int, float) for arg in args):
        raise TypeError()

    if a_coef == b_coef == c_coef == 0:
        raise InfiniteSolutionsError()

    if a_coef == 0 and b_coef != 0 and c_coef != 0:
        root = -c_coef / b_coef

        return (root, root)

    discriminant = b_coef**2 - 4 * a_coef * c_coef

    if discriminant < 0 or a_coef == b_coef == 0:
        raise NoSolutionsError()

    if discriminant == 0:
        root = -b_coef / (2 * a_coef)

        return (root, root)

    result1 = (-b_coef + discriminant**0.5) / (2 * a_coef)
    result2 = (-b_coef - discriminant**0.5) / (2 * a_coef)

    min_result = min(result1, result2)
    max_result = max(result1, result2)

    return (min_result, max_result)


# -

# G


# +
class CyrillicError(Exception):
    """Ошибка: если строка состоит не только из кириллицы."""


class CapitalError(Exception):
    """Ошибка: заглавной буквы.

    Если значение не начинается с заглавной буквы или найдена заглавная буква не в начале
    значения.
    """


def name_validation(value: str) -> str:
    """Функция валидации имени пользователя."""
    if not isinstance(value, str):
        raise TypeError

    if not fullmatch(r"[а-яА-ЯёЁ]+", value):
        raise CyrillicError

    if not value[0].isupper() or any(char.isupper() for char in value[1::]):
        raise CapitalError

    return value


# -

# H


# +
class BadCharacterError(Exception):
    """Ошибка: неправильный символ.

    Если значение состоит не только из латинских букв, цифр и символа нижнего
    подчёркивания.
    """


class StartsWithDigitError(Exception):
    """Ошибка: если значение начинается с цифры."""


def username_validation(value: str) -> str:
    """Функция валидации имени пользователя."""
    if not isinstance(value, str):
        raise TypeError

    if not fullmatch(r"[a-zA-Z0-9_]+$", value):
        raise BadCharacterError

    if value[0].isdigit():
        raise StartsWithDigitError

    return value


# -

# I

# +
valid_keys = ["last_name", "first_name", "username"]


def user_validation(**kwargs: str) -> object:
    """Функция валидации данных пользователя."""
    if sorted(valid_keys) != sorted(kwargs.keys()):
        raise KeyError

    if not all(kwargs.values()):
        raise KeyError

    name_validation(kwargs["last_name"])
    name_validation(kwargs["first_name"])
    username_validation(kwargs["username"])

    return kwargs


# -

# J


# +
class MinLengthError(Exception):
    """Ошибка: если пароль меньше заданной длины."""


class PossibleCharError(Exception):
    """Ошибка: в пароле используется недопустимый символ."""


class NeedCharError(Exception):
    """Ошибка: в пароле не найдено ни одного обязательного символа."""


default_valid_chars = "abcdefzhiklmnopqrstvxABCDEFZHIKLMNOPQRSTVX0123456789"


def password_validation(
    password: str,
    min_length: int = 8,
    possible_chars: str = default_valid_chars,
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    """Функция валидации пароля пользователя."""
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if any(char not in possible_chars for char in password):
        raise PossibleCharError

    if all(not at_least_one(char) for char in password):
        raise NeedCharError

    hash_object = sha256()
    hash_object.update(password.encode())
    hex_hash = hash_object.hexdigest()

    return hex_hash


print(password_validation("Hello12345"))
