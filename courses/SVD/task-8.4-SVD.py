import numpy as np

# # Пример матрицы
A = np.array([[-1.0, -3.0], [-3.0, -1.0]])

# # Шаг 1: A^T A
# ATA := транспонировать A и умножить на     A
ATA = A.T @ A

# # Шаг 2: Собственные значения
# eigvals, V = спектральное разложение(ATA)
e_values, e_vectors = np.linalg.eig(ATA)

# # Шаг 3: Сингулярные значения
# singular_vals = Я_КОРЕНЬ(np.maximum(eigvals, 0))[::-1]  # Упорядочим по
# убыванию
# Σ = np.zeros_like(A, dtype=float)
# np.fill_diagonal(Σ, singular_vals)
e_values_sorted = np.sort(e_values)[::-1]  # Сортируем и разворачиваем
singular_values = np.sqrt(e_values_sorted)
Σ = np.zeros_like(A, dtype=float)
np.fill_diagonal(Σ, singular_values)


# # Шаг 4–5: Матрица V (нормированные собственные векторы)
# V = V[:, ::-1]  # тоже упорядочить
V = e_vectors


# # Шаг 6–7: Построим U
# U = (A @ V[:, :len(singular_vals)]) / σᵢ # A × vᵢ / σᵢ
U = A @ V[:, : len(singular_values)]


# # Шаг 8–9: Если нужно — дополнить U до ортонормированной матрицы
# U, _ = np.linalg.qr(U)  # QR даст ортонормальный базис
U, _ = np.linalg.qr(U)  # QR даст ортонормальный базис

# # Готовое разложение
# A_reconstructed = U × Σ × Vᵗ
A_reconstructed = U @ Σ @ V.T


print(U)
print(Σ)
print(V.T)
print(A_reconstructed)

U1, s1, Vt1 = np.linalg.svd(A)
print("____________")
print(U1)
print(s1)
print(Vt1)

# # Пример 2
# A = np.array(
#     [
#         [-1, 1, 0],
#         [-1, -1, 1],
#     ]
# )

# # Выполняем SVD: A = U @ Σ @ Vt
# U, s, Vt = np.linalg.svd(A)

# # Преобразуем s (вектор сингулярных значений) в диагональную матрицу Σ
# Sigma = np.zeros((len(A), len(A[0])))
# for i in range(len(s)):
#     Sigma[i, i] = s[i]


# print("U:\n", U)
# print("Σ:\n", Sigma)
# print("V^T:\n", Vt)

# # Проверка восстановления исходной матрицы
# A_reconstructed = U @ Sigma @ Vt
# print("Восстановленная A:\n", A_reconstructed)

# print(np.allclose(A, A_reconstructed))
