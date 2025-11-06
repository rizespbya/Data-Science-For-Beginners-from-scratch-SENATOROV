"""Макаров.

Классы и объекты в Питоне.
"""

# ## Классы и объекты в Питоне

# ### Создание класса

# #### Создание класса и метод `.__init__()`

# +
# создадим класс CatClass
# нашему классу понадобится Numpy
# массивом Numpy и другими объектами
import numpy as np

# из набора линейных моделей библиотеки sklearn импортируем линейную регрессию
from sklearn.linear_model import LinearRegression


class CatClass:
    """Класс Кот."""

    # и пропишем метод .__init__()
    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        print("Cat initializing")


# -

# #### Создание объекта

# +
# создадим объект Matroskin класса CatClass
Matroskin = CatClass()

# проверим тип данных созданной переменной
type(Matroskin)
# -

# #### Атрибуты класса

# +
# вновь создадим класс CatClass


class CatClass1:
    """Класс Кот."""

    # метод .__init__() на этот раз принимает еще и параметр color
    def __init__(self, color: str) -> None:
        """Инициализация Кота с цветом и типом."""
        # этот параметр будет записан в переменную атрибута self.color
        self.color = color

        # значение атрибута type_ задается внутри класса
        self.type_ = "cat"


# +
# повторно создадим объект класса CatClass, передав ему параметр цвета шерсти
Matroskin1 = CatClass1("gray")

# и выведем атрибуты класса
Matroskin1.color, Matroskin1.type_
# -

# #### Методы класса

# +
# перепишем класс CatClass


class CatClass2:
    """Класс Кот."""

    # метод .__init__() и атрибуты оставим без изменений
    def __init__(self, color: str) -> None:
        """Инициализация Кота с цветом и типом."""
        self.color = color
        self.type_ = "cat"

    # однако добавим метод, который позволит коту мяукать
    def meow(self) -> None:
        """Метод осуществляет мяуканье."""
        for _ in range(3):
            print("Мяу")

    # и метод .info() для вывода информации об объекте
    def info(self) -> None:
        """Метод выводит информацию об экземпляре Кот."""
        print(self.color, self.type_)


# -

# создадим объект
Matroskin2 = CatClass2("gray")

# применим метод .meow()
Matroskin2.meow()

# и метод .info()
Matroskin2.info()

# ### Принципы ООП

# #### Инкапсуляция

# +
# изменим атрибут type_ объекта Matroskin на dog
Matroskin1.type_ = "dog"

# выведем этот атрибут
Matroskin1.type_


# -


class CatClass3:
    """Класс Кот."""

    def __init__(self, color: str) -> None:
        """Инициализация Кота с цветом и типом."""
        self.color = color
        # символ подчеркивания ПЕРЕД названием атрибута указывает,
        # что это частный атрибут и изменять его не стоит
        self._type_ = "cat"


# +
# вновь создадим объект класса CatClass
Matroskin3 = CatClass3("gray")

# и изменим значение атрибута _type_
Matroskin3._type_ = "dog"  # pylint: disable=W0212
Matroskin3._type_  # pylint: disable=W0212


# -


class CatClass4:
    """Класс Кот."""

    def __init__(self, color: str) -> None:
        """Инициализация Кота с цветом и типом."""
        self.color = color
        # символ двойного подчеркивания предотвратит доступ извне
        self.__type_ = "cat"
        print(self.__type_)


# при попытке вызова такого атрибута Питон выдаст ошибку
Matroskin4 = CatClass4("gray")
print(Matroskin4.__type_)  # pylint: disable=W0212

# +
# поставим _CatClass перед __type_
# Matroskin4._CatClass4__type_ = "dog"  C0103

# к сожалению, значение атрибута изменится
# print(Matroskin4._CatClass4__type_)
# -

# #### Наследование классов

# Создание родительского класса и класса-потомка

# +
# создадим класс Animal


class Animal:
    """Базовый класс животное."""

    # пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
    def __init__(self, weight: float, length: float) -> None:
        """Инициализация Животного с весом и длинной."""
        # поместим аргументы этих параметров в соответствующие переменные
        self.weight = weight
        self.length = length

    # объявим методы .eat()
    def eat(self) -> None:
        """Метод осуществляет употребление пищи."""
        print("Eating")

    # и .sleep()
    def sleep(self) -> None:
        """Метод для сна."""
        print("Sleeping")


# +
# создадим класс Bird
# родительский класс Animal пропишем в скобках


class Bird(Animal):
    """Класс Птица, наследник класса Animal."""

    def __init__(self, weight: float, length: float) -> None:
        """Инициализация Птицы с весом, длинной."""
        # с помощью функции super() вызовем метод .__init__() родительского класса Animal
        Animal.__init__(self, weight, length)

    # внутри класса Bird объявим новый метод .move()
    def move(self) -> None:
        """Осуществляет полет птицы."""
        # для птиц .move() будет означать "летать"
        print("Flying")


# -

# создадим объект pigeon и передадим ему значения веса и длины
pigeon = Bird(0.3, 30)

# посмотрим на унаследованные у класса Animal атрибуты
print(pigeon.weight, pigeon.length)

# и методы
pigeon.eat()

# теперь вызовем метод, свойственный только классу Bird
pigeon.move()

# Функция `super()`

# +
# снова создадим класс Bird


class Bird1(Animal):
    """Класс Птица, наследник класса Animal."""

    # в метод .__init__() добавим параметр скорости полета (км/ч)
    def __init__(self, weight: float, length: float, flying_speed: float) -> None:
        """Инициализация Птицы с весом, длинной и скоростью полета."""
        # с помощью функции super() вызовем метод .__init__() родительского класса Animal
        Animal.__init__(self, weight, length)
        self.flying_speed = flying_speed

    # вновь пропишем метод .move()
    def move(self) -> None:
        """Осуществляет полет птицы."""
        print("Flying")


# -

# вновь создадим объект pigeon класса Bird, но уже с тремя параметрами
pigeon1 = Bird1(0.3, 30, 100)

# вызовем как унаследованные, так и собственные атрибуты класса Bird
print(pigeon1.weight, pigeon1.length, pigeon1.flying_speed)

# вызовем унаследованный метод .sleep()
pigeon1.sleep()

# и собственный метод .move()
pigeon1.move()

# Переопределение класса

# +
# создадим подкласс Flightless класса Bird


class Flightless(Bird):
    """Класс Нелетающая Птица."""

    # метод .__init__() этого подкласса "стирает" .__init__() родительского класса
    def __init__(self, weight: float, length: float, running_speed: float) -> None:
        """Инициализация Нелетающей Птицы со скоростью бега."""
        # таким образом, у нас остается только один атрибут
        Bird.__init__(self, weight, length)

        self.running_speed = running_speed

    # кроме того, результатом метода .move() будет 'Running'
    def move(self) -> None:
        """Осуществляет бег птицы."""
        print("Running")


# -

# создадим объект ostrich класса Flightless
ostrich = Flightless(13, 33, 60)

# посмотрим на значение атрибута скорости
ostrich.running_speed

# и проверим метод .move()
ostrich.move()

# подкласс Flightless сохранил методы всех родительских классов
ostrich.eat()

# Множественное наследование

# +
# создадим родительский класс Fish


class Fish:
    """Класс Рыба."""

    # и метод .swim()
    def swim(self) -> None:
        """Осуществляет плавание."""
        print("Swimming")


# +
# и еще один родительский класс Bird


class Bird2:
    """Класс Птица."""

    # и метод .fly()
    def fly(self) -> None:
        """Осуществляет полет."""
        print("Flying")


# +
# теперь создадим класс-потомок этих двух классов


class SwimmingBird(Bird2, Fish):
    """Класс Плавающая Птица."""

    pass  # pylint: disable=unnecessary-pass


# -

# создадим объект duck класса SwimmingBird
duck = SwimmingBird()

# как мы видим утка умеет как летать,
duck.fly()

# так и плавать
duck.swim()

# #### Полиморфизм

# для чисел '+' является оператором сложения
print(2 + 2)

# для строк - оператором объединения
print("классы" + " и " + "объекты")

# 1. Полиморфизм функций

# функцию len() можно применить к строке
print(len("Программирование на Питоне"))

# кроме того, она способна работать со списком
print(len(["Программирование", "на", "Питоне"]))

# словарем
print(len({0: "Программирование", 1: "на", 2: "Питоне"}))

print(len(np.array([1, 2, 3])))

# 2. Полиморфизм классов

# Создадим объекты с одинаковыми атрибутами и методами

# +
# создадим класс котов


class CatClass5:
    """Класс Кот."""

    # определим атрибуты клички, типа и цвета шерсти
    def __init__(self, name: str, color: str) -> None:
        """Инициализация Кота с именем, цветом и типом."""
        self.name = name
        self._type_ = "кот"
        self.color = color

    # создадим метод .info() для вывода этих атрибутов
    def info(self) -> None:
        """Выводит информацию о коте."""
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # и метод .sound(), показывающий, что коты умеют мяукать
    def sound(self) -> None:
        """Метод сообщает, что коты умеют мяукать."""
        print("Я умею мяукать")


# +
# создадим класс собак


class DogClass5:
    """Класс Пес."""

    # с такими же атрибутами
    def __init__(self, name: str, color: str) -> None:
        """Инициализация Пса с именем, цветом и типом."""
        self.name = name
        self._type_ = "пес"
        self.color = color

    # и методами
    def info(self) -> None:
        """Выводит информацию о коте."""
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # хотя, обратите внимание, действия внутри методов отличаются
    def sound(self) -> None:
        """Метод сообщает, что псы умеют лаять."""
        print("Я умею лаять")


# -

# Создадим объекты этих классов

cat5 = CatClass5("Бегемот", "черный")
dog5 = DogClass5("Барбос", "серый")

# В цикле `for` вызовем атрибуты и методы каждого из классов

for animal in (cat5, dog5):
    animal.info()
    animal.sound()
    print()

# ### Парадигмы программирования

patients: list[dict[str, str | int]] = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]

# #### Процедурное программирование

# +
# создадим переменные для общего роста и количества пациентов
total, count = 0, 0

# в цикле for пройдемся по пациентам (отдельным словарям)
for patient in patients:
    # достанем значение роста и прибавим к текущему значению переменной total
    total += int(patient["height"])
    # на каждой итерации будем увеличивать счетчик пациентов на один
    count += 1

# разделим общий рост на количество пациентов,
# чтобы получить среднее значение
print(total / count)
# -

# #### Объектно-ориентированное программирование

# +
# создадим класс для работы с данными DataClass


class DataClass:
    """Класс для работы с данными."""

    # при создании объекта будем передавать ему данные для анализа
    def __init__(self, data: list[dict[str, str | int]]) -> None:
        """Инициализация экземпляра класса."""
        self.data = data
        self.metric: str | None = None
        self.__total: int | None = None
        self.__count: int | None = None

    # кроме того, создадим метод для расчета среднего значения
    def count_average(self, metric: str) -> float:
        """Расчет среднего значения по переданной метрике."""
        # параметр metric определит, по какому столбцу считать среднее
        self.metric = metric

        # объявим два частных атрибута
        self.__total = 0
        self.__count = 0

        # в цикле for пройдемся по списку словарей
        for item in self.data:

            # рассчитаем общую сумму по указанному в metric
            # значению каждого словаря
            self.__total += int(item[self.metric])

            # и количество таких записей
            self.__count += 1

        # разделим общую сумму показателя на количество записей
        return self.__total / self.__count


# +
# создадим объект класса DataClass и передадим ему данные о пациентах
data_object = DataClass(patients)

# вызовем метод .count_average() с метрикой 'height'
data_object.count_average("height")
# -

# #### Функциональное программирование

# Функция map()

# lambda-функция достанет значение по ключу height
# функция map() применит lambda-функцию к каждому вложенному в patients словарю
# функция list() преобразует результат в список
heights: list[int] = list(map(lambda patient: int(patient["height"]), patients))
heights

# воспользуемся функциями sum() и len() для нахождения среднего значения
print(sum(heights) / len(heights))

# Функция einsum()

# +
# возьмем два двумерных массива
a_np_array = np.array([[0, 1, 2], [3, 4, 5]])

b_np_array = np.array([[5, 4], [3, 2], [1, 0]])
# -

# перемножим a и b по индексу j через функцию np.einsum()
einsum_result = np.einsum("ij, jk -> ik", a_np_array, b_np_array)

# ### Классы и объекты в машинном обучении

# #### Готовые классы в библиотеке sklearn

# возьмем данные роста и обхвата шеи
X_np_array = np.array(
    [
        1.48,
        1.49,
        1.49,
        1.50,
        1.51,
        1.52,
        1.52,
        1.53,
        1.53,
        1.54,
        1.55,
        1.56,
        1.57,
        1.57,
        1.58,
        1.58,
        1.59,
        1.60,
        1.61,
        1.62,
        1.63,
        1.64,
        1.65,
        1.65,
        1.66,
        1.67,
        1.67,
        1.68,
        1.68,
        1.69,
        1.70,
        1.70,
        1.71,
        1.71,
        1.71,
        1.74,
        1.75,
        1.76,
        1.77,
        1.77,
        1.78,
    ]
)
y_np_array = np.array(
    [
        29.1,
        30.0,
        30.1,
        30.2,
        30.4,
        30.6,
        30.8,
        30.9,
        31.0,
        30.6,
        30.7,
        30.9,
        31.0,
        31.2,
        31.3,
        32.0,
        31.4,
        31.9,
        32.4,
        32.8,
        32.8,
        33.3,
        33.6,
        33.0,
        33.9,
        33.8,
        35.0,
        34.5,
        34.7,
        34.6,
        34.2,
        34.8,
        35.5,
        36.0,
        36.2,
        36.3,
        36.6,
        36.8,
        36.8,
        37.0,
        38.5,
    ]
)

# преобразуем данные роста в двумерный массив
X_2D = X_np_array.reshape(-1, 1)

# +
# создадим объект этого класса и запишем в переменную model
model = LinearRegression()

# обучим модель с помощью метода .fit(), которому передадим наши данные
model.fit(X_2D, y_np_array)

# на выходе получим коэффициенты линейной регрессии
model.coef_, model.intercept_
# -

# # +
# построим прогноз и выведем первые пять значений
y_pred = model.predict(X_2D)
print(y_pred[:5])

# #### Пример ООП: собственный класс линейной регрессии

# +
# создадим класс SimpleLinearRegression


class SimpleLinearRegression:
    """Класс SimpleLinearRegression."""

    # в методе .__init__() объявим переменные наклона и сдвига
    def __init__(self) -> None:
        """Инициализация экземпляра класса."""
        self.slope_: float = 0.0
        self.intercept_: float = 0.0

    # создадим метод .fit()
    def fit(self, x_arg: list[float], y_arg: list[float]) -> None:
        """Метод для вычисления наклона и сдвига."""
        # найдем среднее значение X и y
        x_mean = self.find_mean(x_arg)
        y_mean = self.find_mean(y_arg)

        # объявим переменные для числителя и знаменателя
        numerator: float = 0
        denominator: float = 0

        # в цикле пройдемся по данным
        for index, value_x in enumerate(x_arg):

            # вычислим значения числителя и знаменателя по формуле выше
            numerator += (value_x - x_mean) * (y_arg[index] - y_mean)
            denominator += (value_x - x_mean) ** 2

        # найдем наклон и сдвиг
        slope_ = numerator / denominator
        intercept_ = y_mean - slope_ * x_mean

        # сохраним получившиеся коэффициенты в виде атрибутов
        self.slope_ = slope_
        self.intercept_ = intercept_

    # метод .predict() просто умножит через скалярное произведение
    # вектор данных на наклон и прибавит сдвиг
    def predict(self, x_arg: list[float]):  # type: ignore
        """Вычисляет склярное произведение."""
        # на выходе мы получим вектор прогнозных значений
        return np.dot(self.slope_, x_arg) + self.intercept_

    # служебный метод: расчет среднего
    def find_mean(self, nums: list[float]) -> float:
        """Расчет среднего."""
        return sum(nums) / len(nums)


# -

# создадим объект класса SimpleLinearRegression
model = SimpleLinearRegression()

# +
# применим метод .fit()
model.fit(X_np_array.tolist(), y_np_array.tolist())

# посмотрим на коэффициенты
print(model.slope_, model.intercept_)

# +
# сделаем прогноз через .predict()
y_pred = model.predict(X_np_array.tolist())

# и выведем первые пять коэффициентов
print(y_pred[:5])
