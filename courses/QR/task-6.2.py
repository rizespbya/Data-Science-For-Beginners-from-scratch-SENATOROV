# Вычисляем коэффициенты линейной регрессии с помощью QR
import numpy as np
from scipy.linalg import lstsq

X = np.array([[1, 2], [2, 3], [3, 4]], dtype=float)
y = np.array([2, 1, 3], dtype=float)

Q, R = np.linalg.qr(X)

beta_lstsq, residuals, rank, singular_values = lstsq(R, Q.T @ y, lapack_driver="gelsy")

print(beta_lstsq)
