import numpy as np


def gram_schmidt(A):
    """Perform QR factorization using the Gram-Schmidt process."""
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        # Orthogonalization
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]

        # Forming Q and R matrices
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R


A = np.array([[1, 2, 4], [3, 4, 7], [5, 6, 8]])
Q, R = gram_schmidt(A)

print(Q)
print(R)
print((Q @ R) == A)
