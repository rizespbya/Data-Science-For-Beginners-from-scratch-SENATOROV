import numpy as np

A = np.array([[1, 0], [0, 1], [2, 2]])


U, S, Vt = np.linalg.svd(A)

k = 1  # target rank
U_k = U[:, :k]
S_k = np.diag(S[:k])
Vt_k = Vt[:k, :]

A_k = U_k @ S_k @ Vt_k

print(A_k)
