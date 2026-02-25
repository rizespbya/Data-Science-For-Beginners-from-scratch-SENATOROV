import numpy as np


def qr_factorization(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q @ v
            v = v - R[i, j] * q
        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R


A = np.array(
    [
        [60, 91, 26],
        [60, 3, 75],
        [
            45,
            90,
            31,
        ],
    ],
    dtype="float",
)

Q, R = qr_factorization(A)
print(Q)
print(R)

print(np.allclose(A, Q @ R))
