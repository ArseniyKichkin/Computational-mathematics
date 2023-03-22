import matplotlib.pyplot as plt
import numpy as np

N = 100
nodes = np.linspace(0, 1, N)
h = nodes[1] - nodes[0]
l1 = 29
l2 = 30

# matrix = np.zeros(N ** 2).reshape((N, N))
# matrix_2 = np.zeros(N * N).reshape((N, N))
result = np.zeros(N)
tolerance = 1e-5


def matrix_create(lamb):
    matrix = np.zeros(N ** 2).reshape((N, N))
    matrix[0, 0] = -1
    matrix[0, 1] = 1
    matrix[-1, -1] = 1
    matrix[-1, -2] = 0

    for row in range(0, N - 2):
        matrix[row + 1, row + 2] = 2 - nodes[row + 1] - h / 2
        matrix[row + 1, row + 1] = -(2 - nodes[row + 1] - h / 2 + 2 - nodes[row + 1] + h / 2) + lamb * h * h * (nodes[
                                                                                                row + 1] ** 2) / (
                                           nodes[row + 1] + 1)
        matrix[row + 1, row] = 2 - nodes[row + 1] + h / 2
    return matrix


def matrix_2_create(par, matr):
    m = np.zeros(N * N).reshape((N, N))
    m[0, 0] = 1
    m[0, 1] = -par[0]
    m[-1, -1] = matr[-1, -2] * par[-1] + matr[-1, -1]
    m[-1, -2] = 0

    for k in range(0, N - 2):
        m[k + 1, k + 2] = matr[k + 1, k + 2]
        m[k + 1, k + 1] = matr[k + 1, k + 1] + matr[k + 1, k] * par[k]
    return m


r = 1
while abs(r) > tolerance:
    tmp = (l2 + l1) / 2
    matrix = matrix_create(tmp)

    extra_param = []
    pre_param = -matrix[0, 1] / matrix[0, 0]
    extra_param.append(pre_param)

    for i in range(1, N - 1):
        pre_param = -matrix[i, i + 1] / (matrix[i, i - 1] * pre_param + matrix[i, i])
        extra_param.append(pre_param)

    result[-1] = 0
    for i in reversed(range(0, N - 1)):
        result[i] = extra_param[i] * result[i + 1]

    matrix_2 = matrix_2_create(extra_param, matrix)
    if np.linalg.det(matrix) * np.linalg.det(matrix_create(l1)) < 0:
        l2 = tmp
        r = l2 - l1
    else:
        l1 = tmp
        r = l2 - l1
a = matrix_create(30)
ex = []
pre = -a[0, 1] / a[0, 0]
ex.append(pre)

for i in range(1, N - 1):
    pre = -a[i, i + 1] / (a[i, i - 1] * pre + a[i, i])
    ex.append(pre)
print(matrix, matrix_2)
print(np.linalg.det(matrix_2_create(ex, a)))
print(tmp)

fig, ax = plt.subplots()
ax.scatter(nodes, result)
plt.show()
plt.close()
