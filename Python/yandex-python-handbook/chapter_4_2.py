"""Задания к главе 4.2.

Позиционные и именованные аргументы. Функции высших порядков. Лямбда-функции

Хендбук Яндекс "Основы Python".
"""

# A

# +
import operator
from datetime import datetime
from itertools import cycle
from typing import Callable, Literal, TypeVar


def make_list(length: int, value: int = 0) -> list[int]:
    """Создает список указанной длины, заполненный переданным значением.

    Args:
        length (int): Длина списка.
        value (int): Элемент для заполнения.

    Returns:
        list[int]: Список длины length, заполненный значением value.
    """
    return [value] * length


# -

# B

# +
Size = int | tuple[int, int]
Matrix = list[list[int]]


def make_matrix(size: Size, value: int = 0) -> Matrix:
    """Создает матрицу указанного размера, заполненную переданным значением.

    Args:
        size (int | tuple[int, int]): Размер матрицы. Если кортеж, то
        (ширина, высота). Если одно значение, то создаем квадратную матрицу
        value (int): Элемент для заполнения.

    Returns:
        list[int]: Матрица размера size, заполненная значением value.
    """
    if isinstance(size, int):
        width = size
        height = size
    else:
        width = size[0]
        height = size[1]

    return [[value] * width for _ in range(height)]


# -

# C


def gcd(*numbers: int) -> int:
    """Вычисляет НОД для переданных чисел.

    Args:
        *numbers (int): Одно или более целое число. Не должно быть пустым.

    Returns:
        int: НОД переданных чисел.
    """
    divider = numbers[0]

    for index in range(1, len(numbers), 1):
        next_var = numbers[index]

        while next_var:
            divider, next_var = next_var, divider % next_var

    return divider


# D

# +
months: dict[str, list[str]] = {
    "ru": [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
    ],
    "en": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
}


def month(number: int, language: Literal["ru", "en"] = "ru") -> str:
    """Функция для получения названия месяца.

    Функция возвращает имя месяца в соответствии с переданными номером месяца
    и языком

    Args:
        number (int): Номер месяца от 1 до 12.
        language (Literal["ru", "en"]): Язык.

    Returns:
        str: Название месяца.
    """
    return months[language][number - 1]


# -

# E


def to_string(*items: object, sep: str = " ", end: str = "\n") -> str:
    r"""Функция возвращает строку из переданных элементов.

    Элементы разделены сепаратором sep. Заканчивается строкой end.

    Args:
        *items (object): Элементы, которые надо объединить в строку.
        sep (str, optional): Разделитель элементов в строке. По умолчанию " ".
        end (str, optional): Окончание строки. По умолчанию  "\n".

    Returns:
        str: _description_
    """
    return f"{sep.join(map(str, items))}{end}"


# F

# +
Operator = Literal["+", "-", "*", "//", "**"]
OperatorFn = Callable[[int, int], int]


def get_operator_fn(operator_f: Operator) -> OperatorFn:
    """Возвращает функцию-оператор для двух целых чисел.

    Args:
        operator_f (Operator): Математическая операция.

    Returns:
       OperatorFn: Функция, принимающая два int и возвращающая int.
    """
    match operator_f:
        case "+":
            return lambda operand1, operand2: operand1 + operand2
        case "-":
            return lambda operand1, operand2: operand1 - operand2
        case "*":
            return lambda operand1, operand2: operand1 * operand2
        case "//":
            return lambda operand1, operand2: operand1 // operand2
        case "**":
            return lambda operand1, operand2: operand1**operand2


# -

# G

# +
T = TypeVar("T")

OperatorFnG = Callable[[tuple[object, ...]], str]


def get_formatter(sep: str = " ", end: str = "") -> OperatorFnG:
    """Возвращает функцию, которая объединяет аргументы в строку.

    Args:
        sep (str, optional): Разделитель элементов в строке. По умолчанию " ".
        end (str, optional): Окончание строки. По умолчанию "".

    Returns:
       OperatorFnG: Функция, принимающая не определенное количество аргументов.
       Возвращает строку, объединяющую эти аргументы через sep и оканчивающуюся
       строкой end.
    """
    return lambda *args: f"{sep.join(map(str, args))}{end}"


# -

# H


def grow(*numbers: int, **kwargs: int) -> tuple[int, ...]:
    """Преобразует позиционные аргументы.

    Функция принимает не определенное количество позиционных аргументов.
    И не определенное количество именованных аргументов.

    Возвращает кортеж, состоящий из по аргументов, увеличенных на значение
    именованных параметров, если значение позиционного аргумента кратно
    длине имени именованного аргумента.

    Args:
        *numbers (int): Целые числа.
        **kwargs (int): Целые числа.

    Returns:
       tuple[int, ...]: Кортеж целых чисел.
    """
    result = []

    for number in numbers:
        updated = number

        for key, value in kwargs.items():
            if number % len(key) == 0:
                updated += value

        result.append(updated)

    return tuple(result)


# I


def product_i(*items: str, **kwargs: int) -> tuple[int, ...]:
    """Заменяет каждую строку на произведение значений именованных параметров.

    Если ни одно имя не найдено — строка игнорируется.

    Args:
        *args (str): Строки, которые нужно обработать.
        **kwargs (int): Именованные параметры.

    Returns:
        tuple[int, ...]: Кортеж произведений для строк, где нашлись совпадения.
    """
    result = []

    for item in items:
        product: None | int = None

        for key, value in kwargs.items():
            if key in item:
                product = product * value if product is not None else value

        if product is not None:
            result.append(product)

    return tuple(result)


# J


def choice(*numbers: int, **kwargs: Callable[[int], int]) -> int:
    """Применяет переданную функцию ко всем позиционным аргументам.

    Если передан именованный параметр min, то возвращает минимальное значение
    из результатов выполнения функции min. Иначе - максимальное из результатов
    выполнения функции max.

    Args:
        *numbers (int): Целые числа.
        **kwargs (Function): Функция. Параметр может иметь имя min или max

    Returns:
        (int): Целое число
    """
    if "min" in kwargs:
        return min(map(kwargs["min"], numbers))

    return max(map(kwargs["max"], numbers))


# K

# +
in_stock: dict[str, int] = {}


def order(*coffees: str) -> str:
    """Функция возвращает название напитка, который можно приготовить.

    Если ни одиннапиток нельзя приготовить, функция возвращает строку:
    "К сожалению, не можем предложить Вам напиток"

    Args:
        *coffees (str): Список напитков.

    Returns:
        (str): Название напитка. Если напиток нельзя приготовить, то строка:
        "К сожалению, не можем предложить Вам напиток"
    """
    ingidients: dict[str, dict[str, int]] = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }

    for coffee in coffees:
        for ingidient, amount in ingidients[coffee].items():
            if in_stock[ingidient] < amount:
                break
        else:
            for ingidient, amount in ingidients[coffee].items():
                in_stock[ingidient] -= amount

            return coffee

    return "К сожалению, не можем предложить Вам напиток"


# -

# L

# +
DATA: dict[Literal["even", "odd"], list[int]] = {"even": [], "odd": []}


def enter_results(*numbers: int) -> None:
    """Функция сохраняет переданные данные в переменную DATA.

    Нечетные числа сохранются в массив DATA['odd'], четные - в DATA['even']

    Args:
        *numbers (int): Список целых чисел.

    Returns:
        None: Функция ничего не возвращает.
    """
    DATA["odd"].extend(numbers[::2])
    DATA["even"].extend(numbers[1::2])


def get_sum() -> tuple[int, int]:
    """Возвращает пару целых чисел: сумма всех нечетных и всех четных чисел.

    Returns:
        tuple[int, int]: Кортеж из двух целых чисел.
    """
    return (sum(DATA["odd"]), sum(DATA["even"]))


def get_average() -> tuple[float, float]:
    """Возвращает пару целых чисел.

    Пара числе - среднее арифметическое всех нечетных и всех четных чисел.

    Returns:
        tuple[int, int]: Кортеж из двух чисел с плавающей точкой.
    """
    average_odd = round(sum(DATA["odd"]) / len(DATA["odd"]), 2)
    average_even = round(sum(DATA["even"]) / len(DATA["even"]), 2)

    return (average_odd, average_even)


# -

# M

# +
FnM = Callable[[str], tuple[int, str]]

fn_m: FnM = lambda string: (len(string), string.lower())

# +
SortFn = Callable[[str], tuple[int, str]]

sort_fn: SortFn = lambda string: (len(string), string.lower())
# -

# N

FilterFn = Callable[[int], bool]
filter_fn: FilterFn = lambda num: sum(map(int, str(num))) % 2 == 0

# O

# +
Repeater = Callable[[int], int]


def get_repeater(func: Callable[[int], int], count: int) -> Repeater:
    """Возвращает функцию, которая вызовет func count раз.

    Args:
        func (Callable[[int], int]): Функция, которую надо вызывать.
        count (int): Количество раз вывзова функции.

    Returns:
        Repeater: Функция, которая вызовет func count раз.
    """

    def repeater(num: int) -> int:
        current: int = num

        for _ in range(count):
            current = func(current)

        return current

    return repeater


# -

# P

# +
Cb = Callable[[str], None]


def login(name: str, password: str, on_login: Cb, on_fail: Cb) -> None:
    """
        Вызывает on_login в случае успешной авторизации, иначе - on_fail.

    Args:
        name (str): Имя пользователя.
        password (str): Пароль.
        on_login (Cb): Функция, вызываемая в случае успешной авторизации.
        on_fail (Cb): Функция, вызываемая в случае неуспешной авторизации.
    Returns:
        None: Функция ничего не возвращает.
    """
    expected = f"{sum(ord(char) for char in name) * len(name):x}"

    if expected[::-1].lower() == password.lower():
        on_login(name)
    else:
        on_fail(name)


# -

# Q

# +
FilterFnQ = Callable[[tuple[str, list[int]]], bool]

filter_fn_q: FilterFnQ = lambda item: isinstance(item[1], list) and any(
    num % 2 == 0 for num in item[1]
)
# -

# R

# +
Fn = Callable[[tuple[str, object]], tuple[str, object]]

fn: Fn = lambda item: (
    "".join([char.lower() for char in item[0] if char.isalpha()]),
    sum(item[1]) if hasattr(item[1], "__iter__") else item[1],
)


# -

# S


def secret_replace(text: str, **kwargs: tuple[str, ...]) -> str:
    """Возвращает строку, зашифрованную на основе переданных параметров.

    Args:
        text (str): Строка, которую надо зашифровать.
        **kwargs (tuple[str, ...]): Параметры шифрования
    Returns:
        str: Зашифрованная строка.
    """
    my_dict = {key: cycle(value) for key, value in kwargs.items()}

    result = "".join(
        [next(my_dict[char]) if char in my_dict else char for char in text]
    )

    return result


# T

# +
User = dict[str, str | datetime | int]


DATA_BASE: list[User] = []


def insert(*users: User) -> None:
    """Функция добавляет пользователя в базу данных DATA_BASE.

    Args:
        *users (User): Произвольное количество пользователей.

    Returns:
        None: Функция ничего не возвращает.
    """
    for user in users:
        formatted_user: User = {**user}

        if isinstance(user["birth"], str):
            formatted_date = datetime.strptime(user["birth"], "%d.%m.%Y")
            formatted_user["date"] = formatted_date

        DATA_BASE.append(formatted_user)


def delete_date(users: list[User]) -> list[User]:
    """Создает копию массива пользователей.

    У каждого пользователя удаляет ключ date

    Args:
        users (list[User]): Массив пользователей.

    Returns:
        list[User]: Массив пользователей, у которых удален ключ date.
    """
    result: list[User] = []

    for user in users:
        copy: User = {key: val for key, val in user.items() if key != "date"}
        result.append(copy)

    return result


Comparator = Callable[[str | datetime | int, str | datetime | int], bool]

operators: dict[str, Comparator] = {
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge,
}


def select(request: str | None = None) -> list[User]:
    """Возвращает массив пользователей, удовлетворяющих запросу request.

    Args:
        request (str | None, optional): Строка запроса.
        Имеет формат "<ключ> <оператор> <значение>" По умолчанию None.

    Returns:
        list[User]: Список пользователей, удовлетворяющий переданной строке
        запроса
    """
    if request is None:
        return delete_date(DATA_BASE)

    key, operator_sign, condition = request.split()

    formatted_condition: str | datetime | int

    if key == "birth":
        formatted_condition = datetime.strptime(condition, "%d.%m.%Y")
    elif condition.isdigit():
        formatted_condition = int(condition)
    else:
        formatted_condition = condition

    result: list[User] = []

    for user in DATA_BASE:
        compare_key = "date" if key == "birth" else key

        if operators[operator_sign](user[compare_key], formatted_condition):
            result.append(user)

    return sorted(
        delete_date(result),
        key=lambda user: user["id"],
    )
