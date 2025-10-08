"""Задания к главе 6.1.

Модули math и numpy

Хендбук Яндекс "Основы Python".
"""

# A

# +
import math
import sys
from typing import Literal

import numpy as np
from numpy.typing import NDArray  # type: ignore

x_var = float(input())

a_el = math.log(math.pow(x_var, 3 / 16), 32)
b_el = math.pow(x_var, math.cos(math.pi * x_var / (2 * math.e)))
c_el = math.pow(math.sin(x_var / math.pi), 2)

result = a_el + b_el - c_el

print(result)
# -

# B

for row in sys.stdin:
    array_b = map(int, row[0:-1].split(" "))
    result = math.gcd(*array_b)
    print(result)

# C

# +
members, seats = map(int, input().split(" "))

combinations = math.comb(members, seats)
in_place_combinations = combinations * seats // members

print(in_place_combinations, combinations)
# -

# D

# +
array_d = list(map(float, input().split(" ")))

print(math.pow(math.prod(array_d), 1 / len(array_d)))
# -

# E

# +
x1, y1 = map(float, input().split(" "))

p_x2, p_y2 = map(float, input().split(" "))

x2 = p_x2 * math.cos(p_y2)
y2 = p_x2 * math.sin(p_y2)

distance = math.dist((x1, y2), (x2, y2))

print(distance)


# -

# F


def multiplication_matrix(size: int) -> NDArray[np.int_]:
    """Построение таблицы умножения."""
    numbers = np.arange(1, size + 1)
    matrix: NDArray[np.int_] = np.outer(numbers, numbers)

    return matrix


# G


def make_board(size: int) -> NDArray[np.int8]:
    """Создает шахматную доску размера size * size.

    Белые клетки - 1, чернные - 0.
    В левом верхнем углу белая клетка.
    """
    board = np.zeros((size, size), dtype=np.int8)

    board[::2, ::2] = 1
    board[1::2, 1::2] = 1

    return board


# H


def snake(
    width: int, height: int, direction: Literal["H", "V"] = "H"
) -> NDArray[np.int16]:
    """Создает змейку размера width * height."""
    matrix = np.zeros((height, width), dtype=np.int16)

    if direction == "H":
        for index in range(height):
            matrix[index] = np.arange(
                index * width + 1, index * width + width + 1
            )

        matrix[1::2, ::] = matrix[1::2, ::-1]
    else:
        for index in range(height):
            matrix[index] = np.arange(index + 1, width * height + 1, height)

        matrix[::, 1::2] = matrix[::-1, 1::2]

    return matrix


# I


def rotate(matrix: NDArray[np.int_], degrees: int) -> NDArray[np.int_]:
    """Поворачивает матрицу на заданное число градусов.

    Число градусов должно быть кратно 90. Поворот происходит по часовой стрелке.
    """
    rotated_matrix: NDArray[np.int_] = np.rot90(
        matrix, k=(360 - degrees) // 90
    )

    return rotated_matrix


# J


def stairs(array: NDArray[np.int_]) -> NDArray[np.int_]:
    """Создает матрицу по вектору.

    Каждая строка является копией вектора со смещение.
    """
    size = array.size
    matrix: NDArray[np.int_] = np.tile(array, (size, 1))

    for index in range(1, size):
        matrix[index] = np.roll(matrix[index], index)

    return matrix
