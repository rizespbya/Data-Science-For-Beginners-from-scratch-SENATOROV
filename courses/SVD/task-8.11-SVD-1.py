import numpy as np


def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.

    Args:
        A: A 2x2 numpy array

    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    AtA = A.T @ A

    if AtA[0, 0] == AtA[1, 1]:
        theta = np.pi / 4
    else:
        theta = 0.5 * np.arctan2(2 * AtA[0, 1], AtA[0, 0] - AtA[1, 1])

    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])

    D = R.T @ AtA @ R

    V = R

    S = np.sqrt(np.array([D[0, 0], D[1, 1]]))

    S_inv = np.diag([1 / S[0] if S[0] > 1e-10 else 0, 1 / S[1] if S[1] > 1e-10 else 0])
    U = A @ V @ S_inv

    return (U, S, V.T)


svd_2x2_singular_values(np.array([[2, 1], [1, 2]]))
