import numpy as np

# Для матрицы A
# 4 1
# 2 3
# Посчитать:
# собственные значения
# собственные векторы
# диагональную матрицу собственных значений
# обратную матрицу собственных векторов
# Из полученного разложения реконструировать матрицу A
# Убедиться, что матрица A_reconstructed совпадает с начальной матрицей  A

A = np.array([[4, 1], [2, 3]])
e_values, e_vectors = np.linalg.eig(A)

P = e_vectors
Diag = np.diag(e_values)
P_inv = np.linalg.inv(P)

A_reconstructed = P @ Diag @ P_inv

print(e_values)
print(e_vectors)
print(A_reconstructed)
