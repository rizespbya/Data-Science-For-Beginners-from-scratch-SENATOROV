import numpy as np


def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.

    Args:
        A: 2x2 numpy array

    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    # Your code here
    ATA = A.T @ A

    e_values, e_vectors = np.linalg.eig(ATA)

    e_values_sorted = np.sort(e_values)[::-1]  # Сортируем и разворачиваем
    singular_values = np.sqrt(e_values_sorted)

    V = e_vectors

    U = A @ V[:, : len(singular_values)]
    U, _ = np.linalg.qr(U)  # QR даст ортонормальный базис

    Σ = np.zeros_like(A, dtype=float)
    np.fill_diagonal(Σ, singular_values)

    return U, singular_values, V.T


svd_2x2(np.array([[1, 2], [3, 4]]))
