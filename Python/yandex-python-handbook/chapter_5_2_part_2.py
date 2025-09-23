"""Задания к главе 5.2.

Волшебные методы, переопределение методов. Наследование.

Хендбук Яндекс "Основы Python".

Из-за ограничения на количество строк в файле разбит на несколько частей.
"""

# G

# +
from math import gcd


class FractionG:
    """Рациональная дробь.

    Attributes:
        numerator_val (int): Числитель.
        denominator_val (int): Знаменатель.
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

    def __neg__(self) -> "FractionG":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val * (-1)

        return FractionG(numerator, self.denominator_val)

    def __add__(self, other: "FractionG") -> "FractionG":
        """Складывает дроби при использовании бинарного +.

        Args:
            other (FractionG): Прибавляемая дробь.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        numerator = numerator1 + numerator2
        denominator = self.denominator_val * other.denominator_val

        return FractionG(numerator, denominator)

    def __sub__(self, other: "FractionG") -> "FractionG":
        """Вычитает дроби при использовании бинарного -.

        Args:
            other (FractionG): Вычитаемая дробь.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        return self + (-other)

    def __iadd__(self, other: "FractionG") -> "FractionG":
        """Складывает дроби при использовании +=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionG): Прибавляемая дробь.

        Returns:
            FractionG: Измененная исходная дробь, переданная слева.
        """
        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 + numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __isub__(self, other: "FractionG") -> "FractionG":
        """Вычитает дроби при использовании -=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionG): Вычитаемая дробь.

        Returns:
            FractionG: Измененная исходная дробь, переданная слева.
        """
        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 - numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __mul__(self, other: "FractionG") -> "FractionG":
        """Умножает дроби при использовании *.

        Args:
            other (FractionG): Второй множитель.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val * other.numerator_val
        denominator = self.denominator_val * other.denominator_val

        return FractionG(numerator, denominator)

    def __truediv__(self, other: "FractionG") -> "FractionG":
        """Вычисляет частное от деления дробей при использовании /.

        Args:
            other (FractionG): Делитель.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val * other.denominator_val
        denominator = self.denominator_val * other.numerator_val

        return FractionG(numerator, denominator)

    def __imul__(self, other: "FractionG") -> "FractionG":
        """Умножает дроби при использовании *=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionG): Вычитаемая дробь.

        Returns:
            FractionG: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val = self.numerator_val * other.numerator_val
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __itruediv__(self, other: "FractionG") -> "FractionG":
        """Вычисляет частное при делении дробей с использованием /=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionG): Делитель.

        Returns:
            FractionG: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val = self.numerator_val * other.denominator_val
        self.denominator_val = self.denominator_val * other.numerator_val

        self._readuction()

        return self

    def reverse(self) -> "FractionG":
        """Возвращает дробь, обратную текущей."""
        return FractionG(self.denominator_val, self.numerator_val)


# -

# H


# I


# J
