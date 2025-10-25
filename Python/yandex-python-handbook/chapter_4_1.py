# %%
"""Задания к главе 4.1.

Функции. Области видимости. Передача параметров в функции.

Хендбук Яндекс "Основы Python".
"""

# A

# %%
from itertools import chain
from typing import Literal, Union


def print_hello(name: str) -> None:
    """Выводит приветственное сообщение с указанным именем.

    Args:
        name (str): Имя пользователя, которое будет включено в приветствие.

    Returns:
        None: Функция ничего не возвращает.
    """
    print(f"Hello, {name}!")


# B


# %%
def gcd(a_value: int, b_value: int) -> int:
    """Фукнция возвращает НОД двух целых чисел.

    Args:
        a_value (int): Первое целое число.
        b_value (int): Второе целое число.

    Returns:
        int: НОД чисел a_value и b_value.
    """
    while b_value:
        a_value, b_value = b_value, a_value % b_value

    return a_value


# C


# %%
def number_length(number: int) -> int:
    """Функция подсчитывает количество цифр в числе.

    Args:
        number (int): Целое число.

    Returns:
        int: Количество цифр в числе number.
    """
    return len(str(abs(number)))


# D


# %%
def take_small(money: list[int]) -> list[int]:
    """Фильтрует список номиналов.

    Функция принимает список номиналов и возвращает список номиналов,
    которые меньше 100.

    Args:
        money (list[int]): Список номиналов.

    Returns:
        list[int]: Список номиналов, которые меньше 100.
    """
    return [num for num in money if num < 100]


# E

# %%
counter = 0


def click() -> None:
    """Функция увеличивает глобальную переменную counter на 1.

    Returns:
        None: Функция ничего не возвращает.
    """
    # Требуется по условию задачи
    # pylint: disable=global-statement
    global counter
    counter += 1


def get_count() -> int:
    """Функция возвращает текущее значение глобальной переменной counter.

    Returns:
        int: Текущее значение глобальной переменной counter.
    """
    return counter


# F

# %%
counter = 0


def move(name: Literal["Ваня", "Петя"], number: int) -> None:
    """Функция изменят глобальную переменную counter на number.

    В зависимости от имени игрока увеличивает или уменьшает counter.

    Returns:
        None: Функция ничего не возвращает.
    """
    # Требуется по условию задачи
    # pylint: disable=global-statement
    global counter

    if name == "Петя":
        counter += number
    else:
        counter -= number


def game_over() -> Literal["Ваня", "Петя", "Ничья"]:
    """Функция возвращает результат игры.

    Returns:
        Literal["Ваня" , "Петя" , "Ничья"]: Имя игрока или 'Ничья'.
    """
    match counter:
        case num if num > 0:
            return "Петя"
        case num if num < 0:
            return "Ваня"
        case _:
            return "Ничья"


# G


# %%
def max_2d(matrix: list[list[int]]) -> int:
    """Функция находит максимальных элемент в матрице.

    Args:
        matrix (list[list[int]]): Двумерная матрица целых чисел.

    Returns:
        int: Максимальных элемент в матрице.
    """
    return max(chain(*matrix))


# H


# %%
def fragments(numbers: list[int]) -> list[list[int]]:
    """Возвращает список возрастающих списков.

    Функция принимает список целых чисел и разбивает его на несколько списков,
    каждый из которых представляет собой возрастающий список элементов

    Args:
        matrix (list[int]): Список целых чисел.

    Returns:
        int: Список списков целых чисел.
    """
    result: list[list[int]] = []

    temp: list[int] = []

    for index, number in enumerate(numbers):
        temp.append(number)
        print(temp)

        if index == len(numbers) - 1 or number >= numbers[index + 1]:
            result.append(temp)
            temp = []

    return result


# I


# %%
def month(number: int, language: Literal["ru", "en"]) -> str:
    """Функция для получения названия месяца.

    Функция возвращает имя месяца в соответствии с переданными номером месяца
    и языком

    Args:
        number (int): Номер месяца от 1 до 12.
        language (Literal["ru", "en"]): Язык.

    Returns:
        str: Название месяца.
    """
    months_dict: dict[str, list[str]] = {
        "en": [
            "January month",
            "February month",
            "March month",
            "April month",
            "May month",
            "June month",
            "July month",
            "August month",
            "September month",
            "October month",
            "November month",
            "December month",
        ],
        "ru": [
            "Январь месяц",
            "Февраль месяц",
            "Март месяц",
            "Апрель месяц",
            "Май месяц",
            "Июнь месяц",
            "Июль месяц",
            "Август месяц",
            "Сентябрь месяц",
            "Октябрь месяц",
            "Ноябрь месяц",
            "Декабрь месяц",
        ],
    }

    return months_dict[language][number - 1]


# J


# %%
def split_numbers(string: str) -> tuple[int, ...]:
    """Преобразование строки чисел в кортеж чисел.

    Функция принимает строку, представляющую собой целые числа,
    разделенные пробелами.
    Возвращает кортеж этих чисел.

    Args:
        string (str): Строка целых чисел, разделенных пробелами.

    Returns:
        tuple(int): Кортеж чисел из строки string.
    """
    return tuple(map(int, string.split()))


# K


# %%
def find_mountains_k(heights: list[int]) -> tuple[int, ...]:
    """Функция принимает список высот.

    Возвращает кортеж "гор" - высот, которые больше своих ближайших соседей

    Args:
        heights (list[int]): Список высот

    Returns:
        tuple[int, ...]: Список "гор"
    """
    result: list[int] = []

    neighbours = zip(heights, heights[1:], heights[2:])

    for index, currents in enumerate(neighbours):
        left, middle, right = currents

        if left < middle and middle > right:
            result.append(index + 2)

    return tuple(result)


# L


# %%
def find_mountains(heights: list[list[int]]) -> tuple[tuple[int, ...], ...]:
    """
    Функция принимает двумерную матрицу - список высот.

    Возвращает кортеж кортежей "гор" - пар, обозначающих координаты высот
    в матрице, окруженных более низкими соседями

    Args:
        heights (list[list[int]]): Список высот

    Returns:
        tuple[int, ...]: Список "гор"
    """
    result: list[tuple[int, int]] = []

    max_y = len(heights) - 1
    max_x = len(heights[0]) - 1

    for y_coord in range(1, max_y):
        for x_coord in range(1, max_x):
            current = heights[y_coord][x_coord]

            conditions = [
                heights[y_coord - 1][x_coord] < current,
                heights[y_coord + 1][x_coord] < current,
                heights[y_coord][x_coord - 1] < current,
                heights[y_coord][x_coord + 1] < current,
                heights[y_coord + 1][x_coord + 1] < current,
                heights[y_coord + 1][x_coord - 1] < current,
                heights[y_coord - 1][x_coord + 1] < current,
                heights[y_coord - 1][x_coord + 1] < current,
            ]

            if all(conditions):
                result.append((y_coord + 1, x_coord + 1))

    return tuple(result)


# M

# %%
cache: set[str] = set()


def modern_print(text: str) -> None:
    """Печатает текст, только если он ещё не был напечатан.

    Args:
        text (str): Текст, который нужно напечатать.

    Returns:
        None: Функция ничего не возвращает.
    """
    if text in cache:
        return

    print(text)
    cache.add(text)


# N


# %%
def can_eat(horse: tuple[int, int], other: tuple[int, int]) -> bool:
    """Проверят, может ли конь "съесть" другую фигуру.

    Функция получает координаты коня и другой фигуры.
    И проверят, может ли конь съесть другую фигуру,
    исходя из того, что конь ходит на две клетки по горизонтали
    или вертикали. А затем на одну клетку по другому направлению.

    Args:
        horse (tuple[int, int]): Координаты коня.
        other (tuple[int, int]): Координаты другой фигуры.

    Returns:
        bool: True, если конь может съесть фигуру; иначе False.
    """
    (horse_x, horse_y), (other_x, other_y) = horse, other

    conditions: list[bool] = [
        abs(horse_x - other_x) == 1 and (abs(horse_y - other_y)) == 2,
        abs(horse_x - other_x) == 2 and (abs(horse_y - other_y)) == 1,
    ]

    return any(conditions)


# O

# %%
Value = Union[int | float | str]
MyDict = dict[str, Value]


def get_dict(text: str) -> dict[str, int | float | str]:
    """Преобразует переданную строку текста в словарь.

    Разбивает переданную строку по символу ;.
    Получившиеся строки разбивает по символу =.
    Первый элемент списка становится ключом, второй - значением.
    Если возможно, значение будет преобразовано к int или float.

    Args:
        text (str): Входная строка для преобразования.

    Returns:
        dict[str, int | float | str]: Словарь, полученный после трансформации
        строки.
    """
    my_dict: MyDict = {}
    for string in text.split(";"):
        key, value = string.split("=")

        float_conditions: list[bool] = [
            value.count(".") == 1,
            value.lstrip("+-").replace(".", "").isdigit(),
        ]

        if value.lstrip("+-").isdigit():
            formatted: Value = int(value)
        elif all(float_conditions):
            formatted = float(value)
        else:
            formatted = value

        my_dict[key] = formatted

    return my_dict


# P


# %%
def is_palindrome(value: str | int | list[int] | tuple[int]) -> bool:
    """Преобразует переданную строку текста в словарь.

    Разбивает переданную строку по символу ;.
    Получившиеся строки разбивает по символу =.
    Первый элемент списка становится ключом, второй - значением.
    Если возможно, значение будет преобразовано к int или float.

    Args:
        text (str): Входная строка для преобразования.

    Returns:
        dict[str, int | float | str]: Словарь, полученный после трансформации
        строки.
    """

    def is_alpha_or_digit(char: str) -> bool:
        """Проверят, является ли переданный символ буквой или цифрой.

        Args:
            char (str): Символ для проверки.

        Returns:
            bool: True, если символ буква или цифра. Иначе False.
        """
        return any([char.isalpha(), char.isdigit()])

    if isinstance(value, (list, tuple)):
        text = ""

        for item in value:
            text += str(item)

    else:
        text = str(value)

    sanitized_text = [char for char in text if is_alpha_or_digit(char)]

    return sanitized_text == sanitized_text[::-1]


# Q


# %%
def is_prime(number: int) -> bool:
    """Проверяет, является ли переданное число простым.

    Args:
        number (int): Число для проверки.

    Returns:
        bool: True, если число простое. Иначе False.
    """
    if number < 2:
        return False

    for divider in range(2, int(number**0.5) + 1):
        if number % divider == 0:
            return False

    return True


# R


# %%
def merge(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple[int, ...]:
    """Объединяет два отсортированных кортежа в один отсортированный.

    Args:
        tuple1 (tuple[int, ...]): Первый кортеж отсортированных чисел.
        tuple1 (tuple[int, ...]): Второй кортеж отсортированных чисел.

    Returns:
        tuple[int, ...]: Отсортированный по возрастанию Кортеж целых чисел,
        содержащий все числа из первого и второго кортежа
    """
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

    return tuple(result)


print(merge((), (1, 2)))


# S


# %%
def swap(list1: list[int], list2: list[int]) -> None:
    """Меняет местами содержимое двух массивов.

    Args:
        list1 (list): Первый массив.
        list2 (list): Второй массив.

    Returns:
        None: Функция ничего не возвращает.
    """
    len1 = len(list1)
    len2 = len(list2)

    list1.extend(list2)
    list2.extend(list1[:len1])

    del list1[:len1]
    del list2[:len2]


# T


# %%
def convert_to_roman(num: int) -> str:
    """Конвертирует натуральное число в римское.

    Функция конвертирует переданное натуральное число,
    записанное арабскими цифрами, в римское.

    Args:
        num1 (int): Натуральное число.

    Returns:
        str: Римское представление переданного числа.
    """
    romans: list[tuple[int, str]] = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""

    for arabic, roman_char in romans:
        if arabic > num:
            continue

        repeat = num // arabic
        result += roman_char * repeat
        num = num - arabic * repeat

        if num == 0:
            break

    return result


def roman(num1: int, num2: int) -> str:
    """Вычисляет римскую сумму двух чисел.

    Фунция принимает два натуральных числа.
    Возвращает их сумму в строке вида:
    РИМСКОЕ_А + РИМСКОЕ_B = РИМСКАЯ_СУММА


    Args:
        num1 (int): Первое натуральное число.
        num1 (int): Второе натуральное число.

    Returns:
        str: Римская сумма двух чисел
    """
    roman1 = convert_to_roman(num1)
    roman2 = convert_to_roman(num2)
    result = convert_to_roman(num1 + num2)

    return f"{roman1} + {roman2} = {result}"
