"""Задания к главе 5.1.

Объектная модель Python. Классы, поля и методы.

Хендбук Яндекс "Основы Python".
"""

# A

# +
from typing import Literal, Self


class Point:
    """Точка на плоскости с двумя координатами.

    Предоставляет методы:
    move() - перемещение точки.
    length() - вычисление расстояния до другой точки.

    Attributes:
        x (int): Координата по оси X.
        y (int): Координата по оси Y.
    """

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """Создает точку с заданными координатами.

        Args:
            x_coord (int): Координата по оси X.
            y_coord (int): Координата по оси Y.
        """
        self.x = x_coord
        self.y = y_coord


# -

# B


class PointB:
    """Точка на плоскости с двумя координатами.

    Предоставляет методы:
    move() - перемещение точки.
    length() - вычисление расстояния до другой точки.

    Attributes:
        x (int): Координата по оси X.
        y (int): Координата по оси Y.
    """

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """Создает точку с заданными координатами.

        Args:
            x_coord (int): Координата по оси X.
            y_coord (int): Координата по оси Y.
        """
        self.x = x_coord
        self.y = y_coord

    def move(self, delta_x: int, delta_y: int) -> None:
        """Перемещает точку на указанное расстояние.

        Args:
            delta_x (int): Расстояние по оси X.
            delta_y (int): Расстояние по оси Y.

        Returns:
            None: Функция ничего не возвращает.
        """
        self.x += delta_x
        self.y += delta_y

    def length(self, other: Self) -> float:
        """Возвращает расстояние до другой точки.

        Args:
            other (Self): Другая точка.

        Returns:
            float: Расстояние.
        """
        result = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return float(round(result, 2))


# C


class RedButton:
    """Красная кнопка, которое считает количество нажатий.

    На каждое нажатие вывод сообщение "Тревога!"

    Attributes:
        counter (int): Количество раз, сколько была нажата кнопка.
    """

    counter: int

    def __init__(self) -> None:
        """Создает красную кнопку."""
        self.counter = 0

    def click(self) -> None:
        """Осуществляет клик по кнопке.

        Увеличивает счетчик кликов.
        Выводит сообщение "Тревога!"

        Returns:
            None: Функция ничего не возвращает.
        """
        self.counter += 1

        print("Тревога!")

    def count(self) -> int:
        """Возвращает текущее количество нажатий.

        Returns:
            int: Количество нажатий.
        """
        return self.counter


# D

# +
Coord = tuple[float, float]


class RectangleD:
    """Прямоугольник.

    Attributes:
        top_left (Coord): Координаты верхнего левого угла.
        bottom_left (Coord): Координаты нижнего левого угла.
        top_right (float): Координаты верхнего правого угла.
        bottom_right (float): Координаты нижнего правого угла.
    """

    top_left: Coord
    bottom_left: Coord
    top_right: Coord
    bottom_right: Coord

    def __init__(self, first: Coord, second: Coord) -> None:
        """Создает прямоугольник.

        Args:
            first (Coord): Координаты одного из противоположных углов.
            second (Coord): Координаты второго из противоположных углов.
        """
        (x1, y1), (x2, y2) = first, second

        self.top_left = (min(x1, x2), max(y1, y2))
        self.bottom_left = (min(x1, x2), min(y1, y2))
        self.top_right = (max(x1, x2), max(y1, y2))
        self.bottom_right = (max(x1, x2), min(y1, y2))
        self.second = second

    def perimeter(self) -> float:
        """Возвращает периметр прямоугольника.

        Returns:
            float: Периметр.
        """
        return float(round(self.width * 2 + self.height * 2, 2))

    def area(self) -> float:
        """Возвращает площадь прямоугольника.

        Returns:
            float: Площадь.
        """
        return float(round(self.width * self.height, 2))

    @property
    def width(self) -> float:
        """Геттер, который возвращает ширину прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return self.top_right[0] - self.top_left[0]

    @property
    def height(self) -> float:
        """Геттер, который возвращает высоту прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return self.top_left[1] - self.bottom_left[1]


# -

# E


class RectangleE:
    """Прямоугольник.

    Attributes:
        top_left (Coord): Координаты верхнего левого угла.
        bottom_left (Coord): Координаты нижнего левого угла.
        top_right (float): Координаты верхнего правого угла.
        bottom_right (float): Координаты нижнего правого угла.
    """

    top_left: Coord
    bottom_left: Coord
    top_right: Coord
    bottom_right: Coord

    def __init__(self, first: Coord, second: Coord) -> None:
        """Создает прямоугольник.

        Args:
            first (Coord): Координаты одного из противоположных углов.
            second (Coord): Координаты второго из противоположных углов.
        """
        (x1, y1), (x2, y2) = first, second

        self.top_left = (min(x1, x2), max(y1, y2))
        self.bottom_left = (min(x1, x2), min(y1, y2))
        self.top_right = (max(x1, x2), max(y1, y2))
        self.bottom_right = (max(x1, x2), min(y1, y2))
        self.second = second

    def perimeter(self) -> float:
        """Возвращает периметр прямоугольника.

        Returns:
            float: Периметр.
        """
        return float(round(self.width * 2 + self.height * 2, 2))

    def area(self) -> float:
        """Возвращает площадь прямоугольника.

        Returns:
            float: Площадь.
        """
        return float(round(self.width * self.height, 2))

    @property
    def width(self) -> float:
        """Геттер, который возвращает ширину прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return self.top_right[0] - self.top_left[0]

    @property
    def height(self) -> float:
        """Геттер, который возвращает высоту прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return self.top_left[1] - self.bottom_left[1]


# F


class RectangleF:
    """Прямоугольник.

    Attributes:
        top_left (Coord): Координаты верхнего левого угла.
        bottom_left (Coord): Координаты нижнего левого угла.
        top_right (float): Координаты верхнего правого угла.
        bottom_right (float): Координаты нижнего правого угла.
    """

    top_left: Coord
    bottom_left: Coord
    top_right: Coord
    bottom_right: Coord

    def __init__(self, first: Coord, second: Coord) -> None:
        """Создает прямоугольник.

        Args:
            first (Coord): Координаты одного из противоположных углов.
            second (Coord): Координаты второго из противоположных углов.
        """
        (x1, y1), (x2, y2) = first, second

        self.top_left = (min(x1, x2), max(y1, y2))
        self.bottom_left = (min(x1, x2), min(y1, y2))
        self.top_right = (max(x1, x2), max(y1, y2))
        self.bottom_right = (max(x1, x2), min(y1, y2))

    def perimeter(self) -> float:
        """Возвращает периметр прямоугольника.

        Returns:
            float: Периметр.
        """
        return float(round(self.width * 2 + self.height * 2, 2))

    def area(self) -> float:
        """Возвращает площадь прямоугольника.

        Returns:
            float: Площадь.
        """
        return float(round(self.width * self.height, 2))

    @property
    def width(self) -> float:
        """Геттер, который возвращает ширину прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return float(round(self.top_right[0] - self.top_left[0], 2))

    @property
    def height(self) -> float:
        """Геттер, который возвращает высоту прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return float(round(self.top_left[1] - self.bottom_left[1], 2))

    def get_pos(self) -> Coord:
        """Возвращает координаты верхнего левого угла.

        Returns:
            Coord: Координаты верхнего левого угла.
        """
        return round(self.top_left[0], 2), round(self.top_left[1], 2)

    def get_size(self) -> tuple[float, float]:
        """Возвращает ширину и высоту прямоугольника.

        Returns:
            tuple[float, float]: Ширина и высота прямоугольника.
        """
        return (self.width, self.height)

    def move(self, delta_x: float, delta_y: float) -> None:
        """Перемещает прямоугольник на заданные расстояния.

        Args:
            delta_x (float): Расстояние по оси X.
            delta_y (float): Расстояние по оси Y.
        """
        xtl, ytl = self.top_left
        self.top_left = (xtl + delta_x, ytl + delta_y)

        xbl, ybl = self.bottom_left
        self.bottom_left = (xbl + delta_x, ybl + delta_y)

        xtr, ytr = self.top_right
        self.top_right = (xtr + delta_x, ytr + delta_y)

        xbr, ybr = self.bottom_right
        self.bottom_right = (xbr + delta_x, ybr + delta_y)

    def resize(self, width: float, height: float) -> None:
        """Изменяет размеры прямоугольника.

        Оставляет неизменной координаты левого верхнего угла.

        Args:
            width (float): Новая ширина.
            height (float): Новая высота.
        """
        xtl, ytl = self.top_left

        self.bottom_left = (xtl, ytl - height)
        self.top_right = (xtl + width, ytl)
        self.bottom_right = (xtl + width, ytl - height)


# G


class RectangleG:
    """Прямоугольник.

    Attributes:
        top_left (Coord): Координаты верхнего левого угла.
        bottom_left (Coord): Координаты нижнего левого угла.
        top_right (float): Координаты верхнего правого угла.
        bottom_right (float): Координаты нижнего правого угла.
    """

    top_left: Coord
    bottom_left: Coord
    top_right: Coord
    bottom_right: Coord

    def __init__(self, first: Coord, second: Coord) -> None:
        """Создает прямоугольник.

        Args:
            first (Coord): Координаты одного из противоположных углов.
            second (Coord): Координаты второго из противоположных углов.
        """
        (x1, y1), (x2, y2) = first, second

        self.top_left = (min(x1, x2), max(y1, y2))
        self.bottom_left = (min(x1, x2), min(y1, y2))
        self.top_right = (max(x1, x2), max(y1, y2))
        self.bottom_right = (max(x1, x2), min(y1, y2))

    def perimeter(self) -> float:
        """Возвращает периметр прямоугольника.

        Returns:
            float: Периметр.
        """
        return float(round(self.width * 2 + self.height * 2, 2))

    def area(self) -> float:
        """Возвращает площадь прямоугольника.

        Returns:
            float: Площадь.
        """
        return float(round(self.width * self.height, 2))

    @property
    def width(self) -> float:
        """Геттер, который возвращает ширину прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return float(round(self.top_right[0] - self.top_left[0], 2))

    @property
    def height(self) -> float:
        """Геттер, который возвращает высоту прямоугольника.

        Returns:
            float: Ширина прямоугольника
        """
        return float(round(self.top_left[1] - self.bottom_left[1], 2))

    def get_pos(self) -> Coord:
        """Возвращает координаты верхнего левого угла.

        Returns:
            Coord: Координаты верхнего левого угла.
        """
        return round(self.top_left[0], 2), round(self.top_left[1], 2)

    def get_size(self) -> tuple[float, float]:
        """Возвращает ширину и высоту прямоугольника.

        Returns:
            tuple[float, float]: Ширина и высота прямоугольника.
        """
        return (self.width, self.height)

    def move(self, delta_x: float, delta_y: float) -> None:
        """Перемещает прямоугольник на заданные расстояния.

        Args:
            delta_x (float): Расстояние по оси X.
            delta_y (float): Расстояние по оси Y.
        """
        xtl, ytl = self.top_left
        self.top_left = (xtl + delta_x, ytl + delta_y)

        xbl, ybl = self.bottom_left
        self.bottom_left = (xbl + delta_x, ybl + delta_y)

        xtr, ytr = self.top_right
        self.top_right = (xtr + delta_x, ytr + delta_y)

        xbr, ybr = self.bottom_right
        self.bottom_right = (xbr + delta_x, ybr + delta_y)

    def resize(self, width: float, height: float) -> None:
        """Изменяет размеры прямоугольника.

        Оставляет неизменной координаты левого верхнего угла.

        Args:
            width (float): Новая ширина.
            height (float): Новая высота.
        """
        xtl, ytl = self.top_left

        self.bottom_left = (xtl, ytl - height)
        self.top_right = (xtl + width, ytl)
        self.bottom_right = (xtl + width, ytl - height)

    @property
    def center(self) -> Coord:
        """Вычисляет центр прямоугольника.

        Returns:
            Coord: Центр прямоугольника.
        """
        xtr, ytr = self.top_right

        center_x = float(round(xtr - self.width / 2, 2))
        center_y = float(round(ytr - self.height / 2, 2))

        return center_x, center_y

    def turn(self) -> None:
        """Поворачивает прямоугольник на 90 градусов."""
        center_x, center_y = self.center

        half_width = self.width / 2
        half_height = self.height / 2

        self.top_left = (center_x - half_height, center_y + half_width)
        self.top_right = (center_x + half_height, center_y + half_width)
        self.bottom_left = (center_x - half_height, center_y - half_width)
        self.bottom_right = (center_x + half_height, center_y - half_width)

    def scale(self, factor: float) -> None:
        """Изменяет размер прямоугольника в указанное количество раз.

        Изменения происходят относительно центра

        Args:
            factor (_type_): _description_
        """
        new_width = round(self.width * factor, 2)
        new_height = round(self.height * factor, 2)

        half_width = new_width / 2
        half_height = new_height / 2

        center_x, center_y = self.center

        self.top_left = (center_x - half_width, center_y + half_height)
        self.top_right = (center_x + half_width, center_y + half_height)
        self.bottom_left = (center_x - half_width, center_y - half_height)
        self.bottom_right = (center_x + half_width, center_y - half_height)


# H

# +
CellState = Literal["W", "B", "X"]


class Cell:
    """Клетка игральной доски.

    Attributes:
        state (CellState): Текущее состояние:
            W - белая шашка
            B - черная шашка
            X - пустая клетка
    """

    state: CellState

    def __init__(self, state: CellState) -> None:
        """Создает клетку.

        Args:
            state (CellState): Начальное состояние клетки.
        """
        self.change_status(state)

    def status(self) -> CellState:
        """Возвращает текущее состояние клетки.

        Returns:
            CellState: Текущее состояние клетки.
        """
        return self.state

    def change_status(self, state: CellState) -> None:
        """Изменяет текущее состояние клетки.

        Args:
            state (CellState): Новое состояние.
        """
        self.state = state


class Checkers:
    """Игральная доска.

    Attributes:
        matrix: list[list[Cell]]: Матрица 8х8, в которой хранятся объекты Cell.
    """

    columns: dict[str, int] = {char: index for index, char in enumerate("ABCDEFGH")}

    rows: dict[str, int] = {char: index for index, char in enumerate("12345678")}

    matrix: list[list[Cell]]

    def __init__(self) -> None:
        """Создает игральную доску и заполняет ее."""
        self.matrix = []

        self.fill_row("W", "even")
        self.fill_row("W", "odd")
        self.fill_row("W", "even")
        self.fill_row()
        self.fill_row()
        self.fill_row("B", "odd")
        self.fill_row("B", "even")
        self.fill_row("B", "odd")

    def fill_row(
        self,
        state: CellState = "X",
        cell_type: Literal["even", "odd"] | None = None,
    ) -> None:
        """Добавляет ряд и заполняет его.

        Если состояние передано, то заполняет четные/нечетные координаты
        ячейками с указанным состоянием. В остальных случаях заполняет
        координаты ячейкой с состоянием Х.

        Args:
            state (CellState, optional): Состояние ячейки. олчанию X.
            cell_type (Literal["even", "odd"] | None, optional): Тип столбца
            (четный / нечетный). По умолчанию None.
        """
        self.matrix.append([])

        row_num = len(self.matrix) - 1

        for index in range(8):
            if cell_type == "even" and index % 2 == 0:
                self.matrix[row_num].append(Cell(state))

                continue
            if cell_type == "odd" and index % 2 == 1:
                self.matrix[row_num].append(Cell(state))

                continue

            self.matrix[row_num].append(Cell("X"))

    def get_cell(self, coords: str) -> Cell:
        """Возвращает ячейку по указанным координатам.

        Args:
            coords (str): Координаты.

        Returns:
            Cell: Ячейка.
        """
        row = self.rows[coords[1]]
        column = self.columns[coords[0]]

        return self.matrix[row][column]

    def move(self, start: str, finish: str) -> None:
        """Сделать ход.

        Args:
            start (str): Начальные координаты.
            finish (str): Конечные координаты.
        """
        start_row = self.rows[start[1]]
        start_column = self.columns[start[0]]

        finish_row = self.rows[finish[1]]
        finish_column = self.columns[finish[0]]

        start_cell = self.matrix[start_row][start_column]
        finish_cell = self.matrix[finish_row][finish_column]

        state = start_cell.status()
        start_cell.change_status("X")

        finish_cell.change_status(state)


# -

# I


class Queue:
    """Очередь.

    Attributes:
        queue (list[object]): Список, который обеспечивает хранение элементов
        очереди.
    """

    queue: list[object]

    def __init__(self) -> None:
        """Создает очередь."""
        self.queue = []

    def is_empty(self) -> bool:
        """Проверяет, пустая ли очередь.

        Returns:
            bool: True, если очередь пустая. Иначе False.
        """
        return len(self.queue) == 0

    def push(self, item: object) -> None:
        """Добавить элемент в конец очереди.

        Args:
            item (object): Добавляемый элемент.
        """
        self.queue.append(item)

    def pop(self) -> object:
        """Вернуть элемент из начала очереди.

        Удаляет элемент из очереди.

        Returns:
            object: Элемент из начала очереди.
        """
        return self.queue.pop(0)


# J


class Stack:
    """Стэк.

    Attributes:
        stack (list[object]): Список, который обеспечивает хранение элементов
        стэка.
    """

    stack: list[object]

    def __init__(self) -> None:
        """Создает стэк."""
        self.stack = []

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стэк.

        Returns:
            bool: True, если стэк пуст. Иначе False.
        """
        return len(self.stack) == 0

    def push(self, item: object) -> None:
        """Добавить элемент в конец стэка.

        Args:
            item (object): Добавляемый элемент.
        """
        self.stack.append(item)

    def pop(self) -> object:
        """Вернуть последний элемент из стэка.

        Удаляет элемент из стэка.

        Returns:
            object: Последний элемент из стэка.
        """
        return self.stack.pop()
