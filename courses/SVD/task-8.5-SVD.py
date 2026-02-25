import numpy as np
from scipy.linalg import svd

X = np.array([[3, 3, 2], [2, 3, -2]])

U, singular, V_transpose = svd(X)

print(U)
print(singular)
print(V_transpose)
