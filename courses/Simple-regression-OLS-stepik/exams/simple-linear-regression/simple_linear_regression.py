"""Тестирование к курсу."""

import os

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from numpy.typing import NDArray  # type: ignore


class SimpleLinearRegression:
    """Simple Linear Regression class."""

    coef = 0
    intercept = 0
    r_squared = 0

    def fit(
        self,
        x_train_arg: NDArray[np.generic],
        y_train_arg: NDArray[np.generic],
    ) -> None:
        """Вычисляет коэффициенты регрессии."""
        sum_of_x = sum(x_train_arg)
        sum_of_y = sum(y_train_arg)

        sum_of_x2 = np.sum(np.square(x_train_arg))
        sum_of_y2 = np.sum(np.square(y_train_arg))
        dot_product = np.dot(x_train_arg, y_train_arg)

        length = len(x_train_arg)

        dif_x = sum_of_x2 - sum_of_x * sum_of_x / length
        # dif_y = sum_of_y2 - sum_of_y * sum_of_y / length

        numerator = length * dot_product - sum_of_x * sum_of_y
        denom = (length * sum_of_x2 - sum_of_x * sum_of_x) * (
            length * sum_of_y2 - (sum_of_y * sum_of_y)
        )

        co = dot_product - sum_of_x * sum_of_y / length

        self.r_squared = np.square(numerator / np.sqrt(denom))
        self.intercept = sum_of_y / length - ((co / dif_x) * sum_of_x / length)
        self.coef = co / dif_x

    def predict(self, x_test: NDArray[np.generic]) -> object:  #
        """Предсказывает значение."""
        return x_test * self.coef + self.intercept


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "tvmarketing.csv")
data_set = pd.read_csv(file_path)

x_train = np.array(data_set[["TV"]])
y_train = np.array(data_set[["Sales"]])

# Сейчас x_train имеет вид
# [[230.1]
#  [ 44.5]
# [ 17.2]
# ...
# [232.1]]
# Обычно метод fit в классе LinearRegression ожидает двумерный массив
# (как выглядит x сейчас)
# Но fit из нашего кастомного класса SimpleLinearRegression
# ожидает одномерный массив.
# Поэтому преобразуем x_train в одномерный массив
x_train = x_train.ravel()
y_train = y_train.ravel()

simple_linear_regression = SimpleLinearRegression()

simple_linear_regression.fit(x_train, y_train)

print(simple_linear_regression.coef)
print(simple_linear_regression.intercept)
print(simple_linear_regression.r_squared)
