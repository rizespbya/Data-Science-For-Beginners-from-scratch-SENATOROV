import numpy as np

A = np.array(
    [
        [1, 2, 4],
        [0, 0, 5],
        [0, 3, 6],
    ]
)

Q, R = np.linalg.qr(A)
print(Q)
print(R)
print(np.allclose(A, np.dot(Q, R)))
