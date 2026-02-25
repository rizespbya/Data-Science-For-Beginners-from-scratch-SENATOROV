# Вычисляем коэффициенты линейной регрессии с помощью QR
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4]], dtype=float)
y = np.array([2, 1, 3], dtype=float)

Q, R = np.linalg.qr(X)

# Способ 1: w = R-1 @ Q.T @ y
# трудоемкий из-за необходимости вычислять обратную матрицу R-1
beta1 = np.linalg.inv(R) @ Q.T @ y

# Способ 2: Решить систему R @ w = Q.T @ y
beta2 = np.linalg.solve(R, Q.T @ y)

print(beta2)
print(beta1)
print(np.allclose(beta1, beta2))
