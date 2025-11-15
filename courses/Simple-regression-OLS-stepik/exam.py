"""Тестирование к курсу."""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

x_array = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y_array = np.array([10, 12, 15, 20, 22, 24])

model = LinearRegression()
model.fit(x_array, y_array)


y_pred = model.predict(x_array)

# если R2_Score - коэффициент близок к 1, то мы имеем
# сильную линейную зависимость
r2 = r2_score(y_array, y_pred)

print(mean_squared_error(y_array, y_pred))
print(mean_absolute_error(y_array, y_pred))
print(model.coef_[0])  # Наклон
print(model.intercept_)  # Смещение - чему равен y при x=0


y_true = np.array([10, 10.5, 11])

y_pred = np.array([10.2, 10.4, 11.1])

errors = y_true - y_pred
print(errors)
abs_errors = np.abs(errors)
print(abs_errors)
squared_errors = errors**2

print(sum(abs_errors) / len(y_true))  # Mean Absolute Error (MAE)
print(sum(squared_errors) / len(y_true))  # Mean Squared Error (MSE)
