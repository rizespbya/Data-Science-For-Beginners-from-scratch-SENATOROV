# Вычисляем коэффициенты линейной регрессии с помощью QR
import numpy as np

# Матрица признаков
A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])

# Матрица значений y
B = np.array([4, 5, 6])

Q, R = np.linalg.qr(A)

# Решаем систему R @ beta = Q.T @ B

beta = np.linalg.solve(R, Q.T @ B)

print(beta)
