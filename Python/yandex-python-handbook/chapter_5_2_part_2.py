# %%
"""Задания к главе 5.2.

Волшебные методы, переопределение методов. Наследование.

Хендбук Яндекс "Основы Python".

Из-за ограничения на количество строк в файле разбит на несколько частей.
"""

# G

# %%
from math import gcd


class FractionG:
    """Рациональная дробь.

    Attributes:
        numerator_val__ (int): Числитель.
        denominator_val__ (int): Знаменатель.
    """

    numerator_val__: int
    denominator_val__: int

    def _readuction(self) -> None:
        """Сокращает дробь.

        Вычисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod = gcd(self.numerator_val__, self.denominator_val__)

        self.numerator_val__ = int(self.numerator_val__ / nod)
        self.denominator_val__ = int(self.denominator_val__ / nod)

        if self.denominator_val__ < 0 and self.numerator_val__ < 0:
            self.numerator_val__ = abs(self.numerator_val__)
            self.denominator_val__ = abs(self.denominator_val__)
        elif self.denominator_val__ < 0:
            self.numerator_val__ = self.numerator_val__ * (-1)
            self.denominator_val__ = abs(self.denominator_val__)

    def __init__(self, arg_1: str | int, arg_2: int | None = None) -> None:
        """Создает рациональную дробь.

        Args:
            arg_1 (str | int): Строка, в которой значения числителя и
            знаменателя разделены символом /, или целое число -
            значение числителя.
            arg_2 (int | None, optional): Значение знаменателя.
            По умолчанию None.

        Raises:
            TypeError: Ошибка, которая будет проброшена в случае, если
            аргументы имеют некорректный тип.
        """
        if isinstance(arg_1, str):
            numerator, denominator = map(int, arg_1.split("/"))

            self.numerator_val__ = numerator
            self.denominator_val__ = denominator

            self._readuction()

            return

        if isinstance(arg_1, int) and isinstance(arg_2, int):
            numerator, denominator = arg_1, arg_2

            self.numerator_val__ = numerator
            self.denominator_val__ = denominator

            self._readuction()

            return

        raise TypeError("Invalid args type")

    def numerator(self, number_arg: int | None = None) -> int:
        """Возвращает числитель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number_arg (int | None, optional): Новое значение числителя.
            По умолчанию None.

        Returns:
            int: Числитель.
        """
        if number_arg is None:
            return abs(self.numerator_val__)

        self.numerator_val__ = number_arg

        self._readuction()

        return self.numerator_val__

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
            return abs(self.denominator_val__)

        self.denominator_val__ = number

        self._readuction()

        return self.denominator_val__

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        fraction = f"{self.numerator_val__}/{self.denominator_val__}"

        return fraction

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        fraction = f"{self.numerator_val__}/{self.denominator_val__}"

        return f"Fraction('{fraction}')"

    def __neg__(self) -> "FractionG":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val__ * (-1)

        return FractionG(numerator, self.denominator_val__)

    def __add__(self, other: "FractionG") -> "FractionG":
        """Складывает дроби при использовании бинарного +.

        Args:
            other (FractionG): Прибавляемая дробь.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator1 = self.numerator_val__ * other.denominator_val__
        numerator2 = other.numerator_val__ * self.denominator_val__
        numerator = numerator1 + numerator2
        denominator = self.denominator_val__ * other.denominator_val__

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
        numerator1 = self.numerator_val__ * other.denominator_val__
        numerator2 = other.numerator_val__ * self.denominator_val__
        self.numerator_val__ = numerator1 + numerator2
        self.denominator_val__ = (
            self.denominator_val__ * other.denominator_val__
        )

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
        numerator1 = self.numerator_val__ * other.denominator_val__
        numerator2 = other.numerator_val__ * self.denominator_val__
        self.numerator_val__ = numerator1 - numerator2
        self.denominator_val__ = (
            self.denominator_val__ * other.denominator_val__
        )

        self._readuction()

        return self

    def __mul__(self, other: "FractionG") -> "FractionG":
        """Умножает дроби при использовании *.

        Args:
            other (FractionG): Второй множитель.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val__ * other.numerator_val__
        denominator = self.denominator_val__ * other.denominator_val__

        return FractionG(numerator, denominator)

    def __truediv__(self, other: "FractionG") -> "FractionG":
        """Вычисляет частное от деления дробей при использовании /.

        Args:
            other (FractionG): Делитель.

        Returns:
            FractionG: Новая дробь Fraction.
        """
        numerator = self.numerator_val__ * other.denominator_val__
        denominator = self.denominator_val__ * other.numerator_val__

        return FractionG(numerator, denominator)

    def __imul__(self, other: "FractionG") -> "FractionG":
        """Умножает дроби при использовании *=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionG): Второй множитель.

        Returns:
            FractionG: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val__ = self.numerator_val__ * other.numerator_val__
        self.denominator_val__ = (
            self.denominator_val__ * other.denominator_val__
        )

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
        self.numerator_val__ = self.numerator_val__ * other.denominator_val__
        self.denominator_val__ = self.denominator_val__ * other.numerator_val__

        self._readuction()

        return self

    def reverse(self) -> "FractionG":
        """Возвращает дробь, обратную текущей."""
        return FractionG(self.denominator_val__, self.numerator_val__)


# H


# %%
class FractionH:
    """Рациональная дробь.

    Attributes:
        numerator_val__ (int): Числитель.
        denominator_val__ (int): Знаменатель.
    """

    numerator_val__: int
    denominator_val__: int

    def _readuction(self) -> None:
        """Сокращает дробь.

        Вычисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod = gcd(self.numerator_val__, self.denominator_val__)

        self.numerator_val__ = int(self.numerator_val__ / nod)
        self.denominator_val__ = int(self.denominator_val__ / nod)

        if self.denominator_val__ < 0 and self.numerator_val__ < 0:
            self.numerator_val__ = abs(self.numerator_val__)
            self.denominator_val__ = abs(self.denominator_val__)
        elif self.denominator_val__ < 0:
            self.numerator_val__ = self.numerator_val__ * (-1)
            self.denominator_val__ = abs(self.denominator_val__)

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
            numerator_, denominator_ = map(int, arg1.split("/"))

        elif isinstance(arg1, int) and isinstance(arg2, int):
            numerator_, denominator_ = arg1, arg2
        else:
            raise TypeError("Invalid args type")

        self.numerator_val__ = numerator_
        self.denominator_val__ = denominator_

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
            return abs(self.numerator_val__)

        self.numerator_val__ = number

        self._readuction()

        return self.numerator_val__

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
            return abs(self.denominator_val__)

        self.denominator_val__ = number

        self._readuction()

        return self.denominator_val__

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        fraction = f"{self.numerator_val__}/{self.denominator_val__}"

        return fraction

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        fraction = f"{self.numerator_val__}/{self.denominator_val__}"

        return f"Fraction('{fraction}')"

    def __neg__(self) -> "FractionH":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            FractionH: Новая дробь Fraction.
        """
        numerator = self.numerator_val__ * (-1)

        return FractionH(numerator, self.denominator_val__)

    def __add__(self, other: "FractionH") -> "FractionH":
        """Складывает дроби при использовании бинарного +.

        Args:
            other (FractionH): Прибавляемая дробь.

        Returns:
            FractionH: Новая дробь Fraction.
        """
        numerator1 = self.numerator_val__ * other.denominator_val__
        numerator2 = other.numerator_val__ * self.denominator_val__
        numerator = numerator1 + numerator2
        denominator = self.denominator_val__ * other.denominator_val__

        return FractionH(numerator, denominator)

    def __sub__(self, other: "FractionH") -> "FractionH":
        """Вычитает дроби при использовании бинарного -.

        Args:
            other (FractionH): Вычитаемая дробь.

        Returns:
            FractionH: Новая дробь Fraction.
        """
        return self + (-other)

    def __iadd__(self, other: "FractionH") -> "FractionH":
        """Складывает дроби при использовании +=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionH): Прибавляемая дробь.

        Returns:
            FractionH: Измененная исходная дробь, переданная слева.
        """
        numerator1 = self.numerator_val__ * other.denominator_val__
        numerator2 = other.numerator_val__ * self.denominator_val__
        self.numerator_val__ = numerator1 + numerator2
        self.denominator_val__ = (
            self.denominator_val__ * other.denominator_val__
        )

        self._readuction()

        return self

    def __isub__(self, other: "FractionH") -> "FractionH":
        """Вычитает дроби при использовании -=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionH): Вычитаемая дробь.

        Returns:
            FractionH: Измененная исходная дробь, переданная слева.
        """
        numerator1 = self.numerator_val__ * other.denominator_val__
        numerator2 = other.numerator_val__ * self.denominator_val__
        self.numerator_val__ = numerator1 - numerator2
        self.denominator_val__ = (
            self.denominator_val__ * other.denominator_val__
        )

        self._readuction()

        return self

    def __mul__(self, other: "FractionH") -> "FractionH":
        """Умножает дроби при использовании *.

        Args:
            other (FractionH): Второй множитель.

        Returns:
            FractionH: Новая дробь Fraction.
        """
        numerator = self.numerator_val__ * other.numerator_val__
        denominator = self.denominator_val__ * other.denominator_val__

        return FractionH(numerator, denominator)

    def __truediv__(self, other: "FractionH") -> "FractionH":
        """Вычисляет частное от деления дробей при использовании /.

        Args:
            other (FractionH): Делитель.

        Returns:
            FractionH: Новая дробь Fraction.
        """
        numerator = self.numerator_val__ * other.denominator_val__
        denominator = self.denominator_val__ * other.numerator_val__

        return FractionH(numerator, denominator)

    def __imul__(self, other: "FractionH") -> "FractionH":
        """Умножает дроби при использовании *=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionH): Второй множитель.

        Returns:
            FractionH: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val__ = self.numerator_val__ * other.numerator_val__
        self.denominator_val__ = (
            self.denominator_val__ * other.denominator_val__
        )

        self._readuction()

        return self

    def __itruediv__(self, other: "FractionH") -> "FractionH":
        """Вычисляет частное при делении дробей с использованием /=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionH): Делитель.

        Returns:
            FractionH: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val__ = self.numerator_val__ * other.denominator_val__
        self.denominator_val__ = self.denominator_val__ * other.numerator_val__

        self._readuction()

        return self

    def reverse(self) -> "FractionH":
        """Возвращает дробь, обратную текущей."""
        return FractionH(self.denominator_val__, self.numerator_val__)

    def __eq__(self, other: object) -> bool:
        """Проверяет равенство дроби переданному аргументу.

        Args:
            other (object): Объект, с которым сравнивается дробь.

        Returns:
            bool: Возращает True, если переданный аргумент равен текущей дроби.
        Иначе возвращает False.
        """
        if isinstance(other, FractionH):
            is_numerator_equal = self.numerator_val__ == other.numerator_val__
            is_denominator_equal = (
                self.denominator_val__ == other.denominator_val__
            )

            return is_numerator_equal and is_denominator_equal

        return False

    def __lt__(self, other: "FractionH") -> bool:
        """Определяет, меньше ли текущая дробь другой дроби.

        Args:
            other (FractionH): Другая дробь для сравнения.

        Returns:
            bool: True, если текущая дробь строго меньше other. Иначе False.
        """
        mul1 = self.numerator_val__ * other.denominator_val__
        mul2 = other.numerator_val__ * self.denominator_val__

        return mul1 < mul2

    def __le__(self, other: "FractionH") -> bool:
        """Определяет, меньше ли текущая дробь или равна другой дроби.

        Args:
            other (FractionH): Другая дробь для сравнения.

        Returns:
            bool: True, если текущая дробь меньше или равна other. Иначе False.
        """
        return self < other or self == other

    def __gt__(self, other: "FractionH") -> bool:
        """Определяет, больше ли текущая дробь другой дроби.

        Args:
            other (FractionH): Другая дробь для сравнения.

        Returns:
            bool: True, если текущая дробь строго больше other. Иначе False.
        """
        return not self < other and not self == other

    def __ge__(self, other: "FractionH") -> bool:
        """Определяет, больше ли текущая дробь или равна другой дроби.

        Args:
            other (FractionH): Другая дробь для сравнения.

        Returns:
            bool: True, если текущая дробь больше или равна other. Иначе False.
        """
        return self > other or self == other

    def __ne__(self, other: object) -> bool:
        """Определяет, не равны ли два объекта.

        Args:
            other (object): Объект для сравнения.

        Returns:
            bool: True, если объекты не равны. Иначе False.
        """
        return not self == other
