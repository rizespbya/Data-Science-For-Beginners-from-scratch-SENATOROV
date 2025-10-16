"""Задания к главе 5.2.

Волшебные методы, переопределение методов. Наследование.

Хендбук Яндекс "Основы Python".

Из-за ограничения на количество строк в файле разбит на несколько частей.
"""

# A

# +
from math import gcd


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

    def length(self, other: "Point") -> float:
        """Возвращает расстояние до другой точки.

        Args:
            other (Self): Другая точка.

        Returns:
            float: Расстояние.
        """
        result = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return float(round(result, 2))


class PatchedPointA(Point):
    """
    Расширенная точка - наследник класса Point.

    Расширяет базовый класс, добавляя возможность передавать координаты
    в виде кортежа или не передавать координаты вовсе
    """

    def __init__(
        self,
        first_coord: tuple[int, int] | int | None = None,
        second_coord: int | None = None,
    ) -> None:
        """Создает расширенную точку.

        Координаты могут быть переданы в виде кортежа или не передаваться
        вовсе.

        Args:
            first_coord (tuple[int, int] | int | None, optional): Кортеж
            координат или координата x.По умолчанию None.
            second_coord (int | None, optional): Координата y.
            По умолчанию None.
        """
        if isinstance(first_coord, tuple):
            x_coord, y_coord = first_coord
            Point.__init__(self, x_coord, y_coord)

        elif first_coord is None or second_coord is None:
            Point.__init__(self, 0, 0)

        else:
            Point.__init__(self, first_coord, second_coord)


# -

# B


class PatchedPointB(Point):
    """
    Расширенная точка - наследник класса Point.

    Расширяет базовый класс, добавляя возможность передавать координаты
    в виде кортежа или не передавать координаты вовсе
    """

    def __init__(
        self,
        first_coord: tuple[int, int] | int | None = None,
        second_coord: int | None = None,
    ) -> None:
        """Создает расширенную точку.

        Координаты могут быть переданы в виде кортежа или не передаваться
        вовсе.

        Args:
            first_coord (tuple[int, int] | int | None, optional): Кортеж
            координат или координата X.По умолчанию None.
            second_coord (int | None, optional): Координата Y.
            По умолчанию None.
        """
        if isinstance(first_coord, tuple):
            x_coord, y_coord = first_coord
            Point.__init__(self, x_coord, y_coord)

        elif first_coord is None or second_coord is None:
            Point.__init__(self, 0, 0)

        else:
            Point.__init__(self, first_coord, second_coord)

    def __str__(self) -> str:
        """Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление объекта.

        Returns:
            str: Репрезентативное представление объекта.
        """
        return f"PatchedPoint({self.x}, {self.y})"


# C


class PatchedPointC(Point):
    """
    Расширенная точка - наследник класса Point.

    Расширяет базовый класс, добавляя возможность передавать координаты
    в виде кортежа или не передавать координаты вовсе
    """

    def __init__(
        self,
        first_coord: tuple[int, int] | int | None = None,
        second_coord: int | None = None,
    ) -> None:
        """Создает расширенную точку.

        Координаты могут быть переданы в виде кортежа или не передаваться
        вовсе.

        Args:
            first_coord (tuple[int, int] | int | None, optional): Кортеж
            координат или координата x.По умолчанию None.
            second_coord (int | None, optional): Координата y.
            По умолчанию None.
        """
        if isinstance(first_coord, tuple):
            x_coord, y_coord = first_coord
            Point.__init__(self, x_coord, y_coord)

        elif first_coord is None or second_coord is None:
            Point.__init__(self, 0, 0)

        else:
            Point.__init__(self, first_coord, second_coord)

    def __str__(self) -> str:
        """Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление объекта.

        Returns:
            str: Репрезентативное представление объекта.
        """
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, deltas: tuple[int, int]) -> "PatchedPointC":
        """Создает новую точку при использовании оператора +.

        Новая точка смещена относительно начальной точки на указанное
        расстояние.

        Args:
            deltas (tuple[int, int]): Расстояние по осям X и Y, на которое
            должна быть смещена новая точка.

        Returns:
            PatchedPoint: Новая расширенная точка PatchedPoint.
        """
        return PatchedPointC(self.x + deltas[0], self.y + deltas[1])

    def __iadd__(self, deltas: tuple[int, int]) -> "PatchedPointC":
        """Перемещает точку при использовании оператора +=.

        Args:
            deltas (tuple[int, int]): Расстояния, на которые надо переместить
            точку.

        Returns:
            PatchedPoint: Перемещенная точка.
        """
        self.move(deltas[0], deltas[1])

        return self


# D


class Fraction:
    """Рациональная дробь.

    Attributes:
        numerator_val (int): Числитель.
        denominator_val (int): Знаменатель.
    """

    numerator_val: int
    denominator_val: int

    def _readuction(self) -> None:
        """Сокращает дробь.

        Высисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod = gcd(self.numerator_val, self.denominator_val)

        if nod != 1:
            self.numerator_val = int(self.numerator_val / nod)
            self.denominator_val = int(self.denominator_val / nod)

    def __init__(self, arg1: str | int, arg2: int | None = None) -> None:
        """Создает рациональную дробь.

        Args:
            arg1 (str | int): Строка, в которой значения числителя и
            знаменателя разедлены символом /, или целое число -
            значение числителя.
            arg2 (int | None, optional): Значение знаменателя.
            По умолчанию None.

        Raises:
            TypeError: Ошибка, которая будет проброшена в случае, если
            аргументы имеют некорректный тип.
        """
        if isinstance(arg1, str):
            numerator, denominator = map(int, arg1.split("/"))

        elif isinstance(arg1, int) and isinstance(arg2, int):
            numerator, denominator = arg1, arg2
        else:
            raise TypeError("Invalid args type")

        self.numerator_val = numerator
        self.denominator_val = denominator

        self._readuction()

    def numerator(self, number: int | None = None) -> int:
        """Возвращает числитель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number (int | None, optional): Новое значение числителя.
            По умолчанию None.

        Returns:
            int: Числитель.
        """
        if number is None:
            return self.numerator_val

        self.numerator_val = number

        self._readuction()

        return self.numerator_val

    def denominator(self, number: int | None = None) -> int:
        """Возвращает знаменатель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number (int | None, optional): Новое значение знаменателя.
            По умолчанию None.

        Returns:
            int: Знаменатель.
        """
        if number is None:
            return self.denominator_val

        self.denominator_val = number

        self._readuction()

        return self.denominator_val

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        return f"{self.numerator_val}/{self.denominator_val}"

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        return f"Fraction({self.numerator_val}, {self.denominator_val})"


# E

# +
MINUS = "-"


class FractionE:
    """Рациональная дробь.

    Attributes:
        numerator_val (int): Числитель.
        denominator_val (int): Знаменатель.
        sign (str): Знак дроби (- или пустая строка).
    """

    numerator_val: int
    denominator_val: int
    sign: str

    def _readuction(self) -> None:
        """Сокращает дробь.

        Вычисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod = gcd(self.numerator_val, self.denominator_val)

        if nod != 1:
            self.numerator_val = int(self.numerator_val / nod)
            self.denominator_val = int(self.denominator_val / nod)

    def __init__(self, arg1: str | int, arg2: int | None = None) -> None:
        """Создает рациональную дробь.

        Args:
            arg1 (str | int): Строка, в которой значения числителя и
            знаменателя разделены символом /, или целое число -
            значение числителя.
            arg2 (int | None, optional): Значение знаменателя.
            По умолчанию None.

        Raises:
            TypeError: Ошибка, которая будет проброшена в случае, если
            аргументы имеют некорректный тип.
        """
        if isinstance(arg1, str):
            numerator, denominator = map(int, arg1.split("/"))

        elif isinstance(arg1, int) and isinstance(arg2, int):
            numerator, denominator = arg1, arg2
        else:
            raise TypeError("Invalid args type")

        self.numerator_val = abs(numerator)
        self.denominator_val = abs(denominator)

        if (numerator < 0) ^ (denominator < 0):
            self.sign = MINUS
        else:
            self.sign = ""

        self._readuction()

    def numerator(self, number: int | None = None) -> int:
        """Возвращает числитель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number (int | None, optional): Новое значение числителя.
            По умолчанию None.

        Returns:
            int: Числитель.
        """
        if number is None:
            return self.numerator_val

        self.numerator_val = abs(number)

        if number < 0:
            self.sign = MINUS if not self.sign else ""

        self._readuction()

        return self.numerator_val

    def denominator(self, number: int | None = None) -> int:
        """Возвращает знаменатель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number (int | None, optional): Новое значение знаменателя.
            По умолчанию None.

        Returns:
            int: Знаменатель.
        """
        if number is None:
            return self.denominator_val

        self.denominator_val = abs(number)

        if number < 0:
            self.sign = MINUS if not self.sign else ""

        self._readuction()

        return self.denominator_val

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        fraction = f"{self.sign}{self.numerator_val}/{self.denominator_val}"

        return fraction

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        fraction = f"{self.sign}{self.numerator_val}/{self.denominator_val}"

        return f"Fraction('{fraction}')"

    def __neg__(self) -> "FractionE":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val

        if self.sign == "":
            numerator *= -1

        return FractionE(numerator, self.denominator_val)


# -

# F


class FractionF:
    """Рациональная дробь.

    Attributes:
        numerator_val (int): Числитель.
        denominator_val (int): Знаменатель.
        sign (str): Знак дроби (- или пустая строка).
    """

    numerator_val: int
    denominator_val: int

    def _readuction(self) -> None:
        """Сокращает дробь.

        Вычисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod = gcd(self.numerator_val, self.denominator_val)

        self.numerator_val = int(self.numerator_val / nod)
        self.denominator_val = int(self.denominator_val / nod)

        if self.denominator_val < 0 and self.numerator_val < 0:
            self.numerator_val = abs(self.numerator_val)
            self.denominator_val = abs(self.denominator_val)
        elif self.denominator_val < 0:
            self.numerator_val = self.numerator_val * (-1)
            self.denominator_val = abs(self.denominator_val)

    def __init__(self, arg1: str | int, arg2: int | None = None) -> None:
        """Создает рациональную дробь.

        Args:
            arg1 (str | int): Строка, в которой значения числителя и
            знаменателя разделены символом /, или целое число -
            значение числителя.
            arg2 (int | None, optional): Значение знаменателя.
            По умолчанию None.

        Raises:
            TypeError: Ошибка, которая будет проброшена в случае, если
            аргументы имеют некорректный тип.
        """
        if isinstance(arg1, str):
            numerator, denominator = map(int, arg1.split("/"))

        elif isinstance(arg1, int) and isinstance(arg2, int):
            numerator, denominator = arg1, arg2
        else:
            raise TypeError("Invalid args type")

        self.numerator_val = numerator
        self.denominator_val = denominator

        self._readuction()

    def numerator(self, number: int | None = None) -> int:
        """Возвращает числитель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number (int | None, optional): Новое значение числителя.
            По умолчанию None.

        Returns:
            int: Числитель.
        """
        if number is None:
            return abs(self.numerator_val)

        self.numerator_val = number

        self._readuction()

        return self.numerator_val

    def denominator(self, number: int | None = None) -> int:
        """Возвращает знаменатель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number (int | None, optional): Новое значение знаменателя.
            По умолчанию None.

        Returns:
            int: Знаменатель.
        """
        if number is None:
            return abs(self.denominator_val)

        self.denominator_val = number

        self._readuction()

        return self.denominator_val

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        fraction = f"{self.numerator_val}/{self.denominator_val}"

        return fraction

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        fraction = f"{self.numerator_val}/{self.denominator_val}"

        return f"Fraction('{fraction}')"

    def __neg__(self) -> "FractionF":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            PatchedPoint: Новая дробь Fraction.
        """
        numerator = self.numerator_val * (-1)

        return FractionF(numerator, self.denominator_val)

    def __add__(self, other: "FractionF") -> "FractionF":
        """Складывает дроби при использовании бинарного +.

        Args:
            other (FractionF): Прибавляемая дробь.

        Returns:
            FractionF: Новая дробь Fraction.
        """
        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        numerator = numerator1 + numerator2
        denominator = self.denominator_val * other.denominator_val

        return FractionF(numerator, denominator)

    def __sub__(self, other: "FractionF") -> "FractionF":
        """Вычитает дроби при использовании бинарного -.

        Args:
            other (FractionF): Вычитаемая дробь.

        Returns:
            FractionF: Новая дробь Fraction.
        """
        return self + (-other)

    def __iadd__(self, other: "FractionF") -> "FractionF":
        """Складывает дроби при использовании +=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionF): Прибавляемая дробь.

        Returns:
            FractionF: Измененная исходная дробь, переданная слева.
        """
        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 + numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __isub__(self, other: "FractionF") -> "FractionF":
        """Вычитает дроби при использовании -=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionF): Вычитаемая дробь.

        Returns:
            FractionF: Измененная исходная дробь, переданная слева.
        """
        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 - numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self
