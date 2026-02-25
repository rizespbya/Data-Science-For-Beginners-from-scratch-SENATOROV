import numpy as np

X = np.array([[2, 1], [1, 3], [0, 1]])
b = np.array([[1], [2], [3]])


U, singular, Vt = np.linalg.svd(X, full_matrices=True)

m, n = X.shape
Sigma = np.zeros((m, n))
np.fill_diagonal(Sigma, singular)

Sigma_plus = np.linalg.pinv(Sigma)


A_pinv = Vt.T @ Sigma_plus @ U.T


weights = A_pinv @ b

print(weights.reshape(-1))
