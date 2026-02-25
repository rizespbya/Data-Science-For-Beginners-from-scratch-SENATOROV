import numpy as np
import scipy

A = np.array([[1, 2], [2, 3], [3, 4]], dtype=float)

# Выполняем QR-разложение с поворотом (pivoting=True)

Q, R, P = scipy.linalg.qr(A, pivoting=True)

# P возвращается как массив индексов, преобразуем его в матрицу перестановок
P_matrix = np.eye(A.shape[1])[P]


print(Q)
print(R)
print(P_matrix)
