"""Задания к главе 6.2.

Модуль pandas

Хендбук Яндекс "Основы Python".
"""

# A

# +
from typing import Callable

import numpy as np
import pandas as pd


def length_stats_a(text: str) -> pd.Series:  # type: ignore
    """Функция преобразует текст в Series с длинами слов."""
    words = "".join(char for char in text if char.isalpha() or char.isspace())

    sorted_words = sorted(set(words.lower().split()))

    return pd.Series((len(word) for word in sorted_words), index=sorted_words)


# -

# B


def length_stats_b(text: str) -> tuple[pd.Series, pd.Series]:  # type: ignore
    """Функция преобразует текст в Series с длинами слов.

    Возвращает два объекта: с четными и нечетными длинами слов.
    """
    words = "".join(char for char in text if char.isalpha() or char.isspace())

    sorted_words = sorted(set(words.lower().split()))

    even: dict[str, int] = {}
    odd: dict[str, int] = {}

    for word in sorted_words:
        length = len(word)

        if length % 2 == 0:
            even[word] = length
        else:
            odd[word] = length

    return (pd.Series(odd, dtype="int64"), pd.Series(even, dtype="int64"))


# C

# +
# mypy: ignore-errors


def cheque(price_list: pd.Series, **kwargs: int) -> pd.DataFrame:
    """Формирует DataFrame с данными о продуктах."""
    products: list[str] = sorted(name for name in kwargs)
    prices: list[int] = [price_list[name].item() for name in products]
    numbers: list[int] = [kwargs[name] for name in products]
    costs: list[int] = [
        prices[index] * numbers[index] for index in range(len(products))
    ]

    return pd.DataFrame(
        {
            "product": products,
            "price": prices,
            "number": numbers,
            "cost": costs,
        }
    )


# -

# D


def discount(products: pd.DataFrame) -> pd.DataFrame:
    """Применяет скидку, если товаров больше двух."""
    copy = products.copy()

    mask = copy["number"] > 2
    copy.loc[mask, "cost"] = copy.loc[mask, "cost"] / 2

    return copy


# E

# fmt: off
def get_long(
    words: pd.Series,  # type: ignore
    min_length: int = 5
) -> pd.Series:  # type: ignore
    """Возвращает Series со словами не короче min_length."""
    return words[words >= min_length]
# fmt: on


# F


def best(journal: pd.DataFrame) -> pd.DataFrame:
    """Функция отфильтровывает ударников из переданного DataFrame."""
    columns = ["maths", "physics", "computer science"]

    mask = (journal[columns] > 3).all(axis=1)
    return journal[mask]


# G


def need_to_work_better(journal: pd.DataFrame) -> pd.DataFrame:
    """Функция отфильтровывает тех, у кого есть 2."""
    columns = ["maths", "physics", "computer science"]

    mask = (journal[columns] == 2).any(axis=1)
    return journal.loc[mask]


# H


def update(journal: pd.DataFrame) -> pd.DataFrame:
    """Считает средний балл и сортирует студентов."""
    columns = ["maths", "physics", "computer science"]

    copy = journal.copy()

    copy["average"] = copy[columns].mean(axis=1)

    return copy.sort_values(["average", "name"], ascending=(False, True))


# I

# +
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

max_x = x2
max_y = y1
min_x = x1
min_y = y2

shots = pd.read_csv("data.csv")

filtered = shots[
    all(
        [
            (shots["x"] <= max_x),
            (shots["x"] >= min_x),
            (shots["y"] <= max_y),
            (shots["y"] >= min_y),
        ]
    )
]

print(filtered)


# -

# J


# +
def values(
    func: Callable[[float], float],
    start: float,
    end: float,
    step: float,
) -> pd.Series:  # type: ignore
    """Возвращает Series значений функции в точках диапазона."""
    indexes = np.arange(start, end + step, step)

    stpes = (func(index) for index in indexes)

    return pd.Series(stpes, indexes)


def min_extremum(data: pd.Series) -> float:  # type: ignore
    """Возвращает минимум из Series."""
    return float(data.idxmin())


def max_extremum(data: pd.Series) -> float:  # type: ignore
    """Возвращает максимум из Series."""
    return data[data == data.max()].index.max()
