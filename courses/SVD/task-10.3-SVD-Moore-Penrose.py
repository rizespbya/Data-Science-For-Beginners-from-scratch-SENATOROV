import numpy as np

arr = np.array([[2, 4], [1, 3], [0, 0], [0, 0]])


U, S, VT = np.linalg.svd(arr)


Sigma = np.diag(S)
Sigma_inverse = np.linalg.inv(Sigma)

Sigma_plus = np.concatenate((Sigma_inverse, np.array([[0, 0], [0, 0]]).T), axis=1)

A_plus = VT.T @ Sigma_plus @ U.T

print(A_plus)
