# https://new.contest.yandex.ru/contests/85630/start

import numpy as np

#
#
#
#
# 1 Ортонормирование Грама–Шмидта

# порог для определения линейной зависимости
eps = 1e-10


def main1():

    amount = int(input())

    A = np.array([list(map(int, input().split())) for _ in range(amount)])

    Q = []
    for a in A.T:
        for q in Q:
            a = a - np.dot(a, q) * q

        norm = np.linalg.norm(a)

        if norm > eps:
            a = a / norm
            Q.append(a)

    for line in Q:
        print(" ".join(map(lambda x: str(round(x, 4)), line)))


#
#
#
#
# 2 Проекция y на линейную оболочку столбцов X
def main2():
    amount = int(input())

    X = np.array([list(map(float, input().split())) for _ in range(amount)])
    y = np.array(list(map(float, input().split())))

    proj = X @ np.linalg.inv(X.T @ X) @ X.T @ y
    print(" ".join(map(lambda value: str(round(value, 4)), proj)))


#
#
#
#
# 3 Проекция y на линейную оболочку столбцов X


def print_matrix(matrix):
    for line in matrix:
        print(" ".join(map(lambda value: str(round(value, 4)), line)))


def main():
    amount, _ = map(int, input().split())

    A = np.array([list(map(float, input().split())) for _ in range(amount)])

    Q, R = np.linalg.qr(A, mode="complete")

    # qr-разложение можно выполнить по-разному
    # В задаче ожидается R, у которой все элементы на главной диагонали положительные
    # Этого можно добиться, умножая строки с отрицательными элементами на главной диагонали на -1 и умножая соответствующие столбцы Q на -1
    for index in range(R.shape[0]):
        diag_element = R[index][index]

        if diag_element > 0:
            continue

        R[index] = -1 * R[index]
        Q[:, index] = -1 * Q[:, index]

    print_matrix(Q)
    print_matrix(R)


main()
