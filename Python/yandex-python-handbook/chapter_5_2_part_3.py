# %%
"""Задания к главе 5.2.

Волшебные методы, переопределение методов. Наследование.

Хендбук Яндекс "Основы Python".

Из-за ограничения на количество строк в файле разбит на несколько частей.
"""

# I

# %%
from math import gcd
from typing import Union


class FractionI:
    """Рациональная дробь.

    Attributes:
        numerator_val (int): Числитель.
        denominator_val (int): Знаменатель.
    """

    _OtherArg = Union["FractionI", str, int]

    numerator_val: int
    denominator_val: int

    def _readuction(self) -> None:
        """Сокращает дробь.

        Вычисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod_ = gcd(self.numerator_val, self.denominator_val)

        self.numerator_val = int(self.numerator_val / nod_)
        self.denominator_val = int(self.denominator_val / nod_)

        if self.denominator_val < 0 and self.numerator_val < 0:
            self.numerator_val = abs(self.numerator_val)
            self.denominator_val = abs(self.denominator_val)
        elif self.denominator_val < 0:
            self.numerator_val = self.numerator_val * (-1)
            self.denominator_val = abs(self.denominator_val)

    def __init__(self, arg1_: str | int, arg2_: int = 1) -> None:
        """Создает рациональную дробь.

        Args:
            arg1_ (str | int): Строка, в которой значения числителя и
            знаменателя разделены символом /, или целое число -
            значение числителя.
            arg2_ (int | None, optional): Значение знаменателя.
            По умолчанию None.

        Raises:
            TypeError: Ошибка, которая будет проброшена в случае, если
            аргументы имеют некорректный тип.
        """
        if isinstance(arg1_, str) and "/" in arg1_:
            numerator_, denominator_ = map(int, arg1_.split("/"))

        # elif isinstance(arg1_, str):
        #     numerator_, denominator_ = map(int, arg1_.split("/"))

        # elif isinstance(arg1_, int) and isinstance(arg2_, int):
        #     numerator_, denominator_ = arg1_, arg2_
        else:
            numerator_, denominator_ = int(arg1_), int(arg2_)

        self.numerator_val = numerator_
        self.denominator_val = denominator_

        self._readuction()

    def numerator(self, number_: int | None = None) -> int:
        """Возвращает числитель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number_ (int | None, optional): Новое значение числителя.
            По умолчанию None.

        Returns:
            int: Числитель.
        """
        if number_ is None:
            return abs(self.numerator_val)

        self.numerator_val = number_

        self._readuction()

        return self.numerator_val

    def denominator(self, number_: int | None = None) -> int:
        """Возвращает знаменатель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number_ (int | None, optional): Новое значение знаменателя.
            По умолчанию None.

        Returns:
            int: Знаменатель.
        """
        if number_ is None:
            return abs(self.denominator_val)

        self.denominator_val = number_

        self._readuction()

        return self.denominator_val

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        fraction_ = f"{self.numerator_val}/{self.denominator_val}"

        return fraction_

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        fraction_ = f"{self.numerator_val}/{self.denominator_val}"

        return f"FractionI('{fraction_}')"

    def __neg__(self) -> "FractionI":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            FractionI: Новая дробь FractionI.
        """
        numerator = self.numerator_val * (-1)

        return FractionI(numerator, self.denominator_val)

    def __add__(self, other: _OtherArg) -> "FractionI":
        """Складывает дроби при использовании бинарного +.

        Args:
            other (FractionI): Прибавляемая дробь.

        Returns:
            FractionI: Новая дробь FractionI.
        """
        other = self._convert_other_to_fraction(other)

        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        numerator = numerator1 + numerator2
        denominator = self.denominator_val * other.denominator_val

        return FractionI(numerator, denominator)

    def __iadd__(self, other: _OtherArg) -> "FractionI":
        """Складывает дроби при использовании +=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionI): Прибавляемая дробь.

        Returns:
            FractionI: Измененная исходная дробь, переданная слева.
        """
        other = self._convert_other_to_fraction(other)

        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 + numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __sub__(self, other: _OtherArg) -> "FractionI":
        """Вычитает дроби при использовании бинарного -.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Новая дробь FractionI.
        """
        other = self._convert_other_to_fraction(other)

        return self + (-other)

    def __isub__(self, other: _OtherArg) -> "FractionI":
        """Вычитает дроби при использовании -=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionI): Вычитаемая дробь.

        Returns:
            FractionI: Измененная исходная дробь, переданная слева.
        """
        other = self._convert_other_to_fraction(other)

        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 - numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __mul__(self, other: "FractionI") -> "FractionI":
        """Умножает дроби при использовании *.

        Args:
            other (FractionI): Второй множитель.

        Returns:
            FractionI: Новая дробь FractionI.
        """
        numerator = self.numerator_val * other.numerator_val
        denominator = self.denominator_val * other.denominator_val

        return FractionI(numerator, denominator)

    def __truediv__(self, other: "FractionI") -> "FractionI":
        """Вычисляет частное от деления дробей при использовании /.

        Args:
            other (FractionI): Делитель.

        Returns:
            FractionI: Новая дробь FractionI.
        """
        numerator = self.numerator_val * other.denominator_val
        denominator = self.denominator_val * other.numerator_val

        return FractionI(numerator, denominator)

    def __imul__(self, other: "FractionI") -> "FractionI":
        """Умножает дроби при использовании *=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionI): Вычитаемая дробь.

        Returns:
            FractionI: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val = self.numerator_val * other.numerator_val
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __itruediv__(self, other: "FractionI") -> "FractionI":
        """Вычисляет частное при делении дробей с использованием /=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (FractionI): Делитель.

        Returns:
            FractionI: Измененная исходная дробь, переданная слева.
        """
        self.numerator_val = self.numerator_val * other.denominator_val
        self.denominator_val = self.denominator_val * other.numerator_val

        self._readuction()

        return self

    def reverse(self) -> "FractionI":
        """Возвращает дробь, обратную текущей."""
        return FractionI(self.denominator_val, self.numerator_val)

    def __eq__(self, other: object) -> bool:
        """Проверяет равенство дроби переданному аргументу.

        Args:
            other (object): Объект, с которым сравнивается дробь.

        Returns:
            bool: Возращает True, если переданный аргумент равен текущей дроби.
        Иначе возвращает False.
        """
        if isinstance(other, FractionI):
            is_numerators_equal = self.numerator_val == other.numerator_val
            is_denominators_equal = (
                self.denominator_val == other.denominator_val
            )

            return is_numerators_equal and is_denominators_equal

        return False

    def __lt__(self, other: _OtherArg) -> bool:
        """Определяет, меньше ли текущая дробь другого аргумента.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь строго меньше other. Иначе False.
        """
        other = self._convert_other_to_fraction(other)

        mul1_ = self.numerator_val * other.denominator_val
        mul2_ = other.numerator_val * self.denominator_val

        return mul1_ < mul2_

    def __le__(self, other_: "FractionI") -> bool:
        """Определяет, меньше ли текущая дробь или равна другой дроби.

        Args:
            other_ (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь меньше или равна other_. Иначе False.
        """
        return self < other_ or self == other_

    def __gt__(self, other_: "FractionI") -> bool:
        """Определяет, больше ли текущая дробь другой дроби.

        Args:
            other_ (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь строго больше other_. Иначе False.
        """
        return not self < other_ and not self == other_

    def __ge__(self, other_: "FractionI") -> bool:
        """Определяет, больше ли текущая дробь или равна другой дроби.

        Args:
            other_ (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь больше или равна other_. Иначе False.
        """
        return self > other_ or self == other_

    def __ne__(self, other_: object) -> bool:
        """Определяет, не равны ли два объекта.

        Args:
            other_ (object): Объект для сравнения.

        Returns:
            bool: True, если объекты не равны. Иначе False.
        """
        return not self == other_

    @staticmethod
    def _convert_other_to_fraction(
        arg: _OtherArg,
    ) -> "FractionI":
        """Конвертирует переданный аргумент в дробь.

        Args:
            arg (_OtherArg): дробь, число или строка, представляющая дробь или
            число.

        Returns:
            FractionI: Дробь, экземпляр класса FractionI
        """
        if isinstance(arg, FractionI):
            return arg

        return FractionI(arg)


# J


# %%
class FractionJ:
    """Рациональная дробь.

    Attributes:
        numerator_val (int): Числитель.
        denominator_val (int): Знаменатель.
    """

    _OtherArg = Union["FractionJ", str, int]

    numerator_val: int
    denominator_val: int

    def _readuction(self) -> None:
        """Сокращает дробь.

        Вычисляет НОД числителя и знаменателя. Если НОД не равен 1, уменьшает числитель и
        знаменатель в НОД раз.
        """
        nod_ = gcd(self.numerator_val, self.denominator_val)

        self.numerator_val = int(self.numerator_val / nod_)
        self.denominator_val = int(self.denominator_val / nod_)

        if self.denominator_val < 0 and self.numerator_val < 0:
            self.numerator_val = abs(self.numerator_val)
            self.denominator_val = abs(self.denominator_val)
        elif self.denominator_val < 0:
            self.numerator_val = self.numerator_val * (-1)
            self.denominator_val = abs(self.denominator_val)

    def __init__(self, arg1_: str | int, arg2_: int = 1) -> None:
        """Создает рациональную дробь.

        Args:
            arg1_ (str | int): Строка, в которой значения числителя и
            знаменателя разделены символом /, или целое число -
            значение числителя.
            arg2_ (int | None, optional): Значение знаменателя.
            По умолчанию None.

        Raises:
            TypeError: Ошибка, которая будет проброшена в случае, если
            аргументы имеют некорректный тип.
        """
        if isinstance(arg1_, str) and "/" in arg1_:
            numerator, denominator = map(int, arg1_.split("/"))

        # elif isinstance(arg1_, str):
        #     numerator, denominator = map(int, arg1_.split("/"))

        # elif isinstance(arg1_, int) and isinstance(arg2_, int):
        #     numerator, denominator = arg1_, arg2_
        else:
            numerator, denominator = int(arg1_), int(arg2_)

        self.numerator_val = numerator
        self.denominator_val = denominator

        self._readuction()

    def numerator(self, number_: int | None = None) -> int:
        """Возвращает числитель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number_ (int | None, optional): Новое значение числителя.
            По умолчанию None.

        Returns:
            int: Числитель.
        """
        if number_ is None:
            return abs(self.numerator_val)

        self.numerator_val = number_

        self._readuction()

        return self.numerator_val

    def denominator(self, number_: int | None = None) -> int:
        """Возвращает знаменатель.

        Если передано значение, то меняет числитель на новое значение,
        при необходимости сокращая дробь.

        Args:
            number_ (int | None, optional): Новое значение знаменателя.
            По умолчанию None.

        Returns:
            int: Знаменатель.
        """
        if number_ is None:
            return abs(self.denominator_val)

        self.denominator_val = number_

        self._readuction()

        return self.denominator_val

    def __str__(self) -> str:
        """Возвращает строковое представление дроби.

        Returns:
            str: Строковое представление дроби.
        """
        fraction_ = f"{self.numerator_val}/{self.denominator_val}"

        return fraction_

    def __repr__(self) -> str:
        """Возвращает репрезентативное представление дроби.

        Returns:
            str: Репрезентативное представление дроби.
        """
        fraction_ = f"{self.numerator_val}/{self.denominator_val}"

        return f"FractionJ('{fraction_}')"

    def __neg__(self) -> "FractionJ":
        """Создает новую дробь при использовании унарного минуса -.

        Новая дробь имеет обратный знак.

        Returns:
            FractionJ: Новая дробь FractionJ.
        """
        numerator = self.numerator_val * (-1)

        return FractionJ(numerator, self.denominator_val)

    def __add__(self, other: _OtherArg) -> "FractionJ":
        """Складывает дроби при использовании бинарного +.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Новая дробь FractionI.
        """
        other = self._convert_other_to_fraction(other)

        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        numerator = numerator1 + numerator2
        denominator = self.denominator_val * other.denominator_val

        return FractionJ(numerator, denominator)

    def __radd__(self, other: _OtherArg) -> "FractionJ":
        """Складывает дроби при использовании бинарного + (справа).

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Новая дробь FractionI.
        """
        other = self._convert_other_to_fraction(other)

        return self + other

    def __iadd__(self, other: _OtherArg) -> "FractionJ":
        """Складывает дроби при использовании +=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Измененная исходная дробь, переданная слева.
        """
        other = self._convert_other_to_fraction(other)

        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 + numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __sub__(self, other: _OtherArg) -> "FractionJ":
        """Вычитает дроби при использовании бинарного -.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Новая дробь FractionI.
        """
        other = self._convert_other_to_fraction(other)

        return self + (-other)

    def __rsub__(self, other: _OtherArg) -> "FractionJ":
        """
        Вычитает дроби при использовании бинарного - (справа).

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Новая дробь FractionI.
        """
        return -self + other

    def __isub__(self, other: _OtherArg) -> "FractionJ":
        """Вычитает дроби при использовании -=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionI: Измененная исходная дробь, переданная слева.
        """
        other = self._convert_other_to_fraction(other)

        numerator1 = self.numerator_val * other.denominator_val
        numerator2 = other.numerator_val * self.denominator_val
        self.numerator_val = numerator1 - numerator2
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __mul__(self, other: _OtherArg) -> "FractionJ":
        """Умножает дроби при использовании *.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionJ: Новая дробь FractionJ.
        """
        other = self._convert_other_to_fraction(other)

        numerator = self.numerator_val * other.numerator_val
        denominator = self.denominator_val * other.denominator_val

        return FractionJ(numerator, denominator)

    def __rmul__(self, other: _OtherArg) -> "FractionJ":
        """Умножает дроби при использовании * (справа).

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionJ: Новая дробь FractionJ.
        """
        return self * other

    def __imul__(self, other: _OtherArg) -> "FractionJ":
        """Умножает дроби при использовании *=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionJ: Измененная исходная дробь, переданная слева.
        """
        other = self._convert_other_to_fraction(other)

        self.numerator_val = self.numerator_val * other.numerator_val
        self.denominator_val = self.denominator_val * other.denominator_val

        self._readuction()

        return self

    def __truediv__(self, other: _OtherArg) -> "FractionJ":
        """Вычисляет частное от деления дробей при использовании /.

        Args:
            other (_OtherArg): Делитель - другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionJ: Новая дробь FractionJ.
        """
        other = self._convert_other_to_fraction(other)

        numerator = self.numerator_val * other.denominator_val
        denominator = self.denominator_val * other.numerator_val

        return FractionJ(numerator, denominator)

    def __rtruediv__(self, other: _OtherArg) -> "FractionJ":
        """Вычисляет частное от деления дробей при использовании / (справа).

        Args:
            other (_OtherArg): Делимое - другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionJ: Новая дробь FractionJ.
        """
        other = self._convert_other_to_fraction(other)

        return self.reverse() * other

    def __itruediv__(self, other: _OtherArg) -> "FractionJ":
        """Вычисляет частное при делении дробей с использованием /=.

        Изменяет исходную дробь, переданную слева.

        Args:
            other (_OtherArg): Делитель - другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            FractionJ: Измененная исходная дробь, переданная слева.
        """
        other = self._convert_other_to_fraction(other)

        self.numerator_val = self.numerator_val * other.denominator_val
        self.denominator_val = self.denominator_val * other.numerator_val

        self._readuction()

        return self

    def reverse(self) -> "FractionJ":
        """Возвращает дробь, обратную текущей."""
        return FractionJ(self.denominator_val, self.numerator_val)

    def __eq__(self, other: object) -> bool:
        """Проверяет равенство дроби переданному аргументу.

        Args:
            other (object): Объект, с которым сравнивается дробь.

        Returns:
            bool: Возращает True, если переданный аргумент равен текущей дроби.
        Иначе возвращает False.
        """
        if isinstance(other, FractionJ):
            is_numerators_equal = self.numerator_val == other.numerator_val
            is_denominators_equal = (
                self.denominator_val == other.denominator_val
            )

            return is_numerators_equal and is_denominators_equal

        return False

    def __lt__(self, other: _OtherArg) -> bool:
        """Определяет, меньше ли текущая дробь другого аргумента.

        Args:
            other (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь строго меньше other. Иначе False.
        """
        other = self._convert_other_to_fraction(other)

        mul1_ = self.numerator_val * other.denominator_val
        mul2_ = other.numerator_val * self.denominator_val

        return mul1_ < mul2_

    def __le__(self, other_: _OtherArg) -> bool:
        """Определяет, меньше ли текущая дробь или равна другой дроби.

        Args:
            other_ (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь меньше или равна other_. Иначе False.
        """
        other_ = self._convert_other_to_fraction(other_)

        return self < other_ or self == other_

    def __gt__(self, other_: _OtherArg) -> bool:
        """Определяет, больше ли текущая дробь другой дроби.

        Args:
            other_ (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь строго больше other_. Иначе False.
        """
        other_ = self._convert_other_to_fraction(other_)

        return not (self < other_ or self == other_)

    def __ge__(self, other_: _OtherArg) -> bool:
        """Определяет, больше ли текущая дробь или равна другой дроби.

        Args:
            other_ (_OtherArg): Другой аргумент
            (дробь, число или строка, представляющая дробь или число).

        Returns:
            bool: True, если текущая дробь больше или равна other_. Иначе False.
        """
        other_ = self._convert_other_to_fraction(other_)

        return self > other_ or self == other_

    def __ne__(self, other_: object) -> bool:
        """Определяет, не равны ли два объекта.

        Args:
            other_ (object): Объект для сравнения.

        Returns:
            bool: True, если объекты не равны. Иначе False.
        """
        return not self == other_

    @staticmethod
    def _convert_other_to_fraction(
        other: _OtherArg,
    ) -> "FractionJ":
        """Конвертирует переданный аргумент в дробь.

        Args:
            arg (_OtherArg): дробь, число или строка, представляющая дробь или
            число.

        Returns:
            FractionI: Дробь, экземпляр класса FractionI
        """
        if isinstance(other, FractionJ):
            return other

        return FractionJ(other)
