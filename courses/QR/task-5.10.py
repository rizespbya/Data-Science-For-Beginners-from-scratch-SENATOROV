import numpy as np

A = np.array([[1, 2], [2, 3], [3, 4]], dtype=float)

Q, R = np.linalg.qr(A, mode="complete")

print(Q)
print(R)
