import numpy as np

x = np.linspace(1910, 2000, 10)
N = 10  # количество узлов
f = np.array([92228496., 106021537., 123202624., 132164569., 151325798., 179323175.,
              203211926., 226545805., 248709873., 281421906.])  # значения функции
h = 10  # шаг сетки


# матрица коэффициентов сплайна, стоящих при второй степени x
matrix = np.zeros(81, dtype=np.float64).reshape(9, 9)

matrix[0, 0] = 2
matrix[0, 1] = 0.5
matrix[7, 7] = 2
matrix[7, 6] = 0.5

for row in range(0, 6):
    matrix[row + 1, row] = 0.5
    matrix[row + 1, row + 1] = 2
    matrix[row + 1, row + 2] = 0.5

# правая часть СЛАУ (разделенные разности)
right_side = [0 for i in range(8)]
right_side[0] = (f[2] - 2 * f[1] + f[0]) / (2 * h)
right_side[7] = (f[9] - 2 * f[8] + f[7]) / (2 * h)
for i in range(1, 6):
    right_side[i] = (f[i + 2] - 2 * f[i + 1] + f[i]) / (2 * h)

# прогонка
extra_params = []
pre_params = [- matrix[0, 1] / matrix[0, 0], right_side[0] / matrix[0, 0]]
extra_params.append(pre_params)

for i in range(1, 7):
    pre_params = [- matrix[i, i + 1] / (matrix[i, i - 1] * pre_params[0] + matrix[i, i]),
                  (right_side[i] - matrix[i, i - 1] * pre_params[1]) /
                  (matrix[i, i - 1] * pre_params[0] + matrix[i, i])]
    extra_params.append(pre_params)

result = [0 for i in range(8)]
result[7] = (right_side[7] - matrix[7, 6] * extra_params[6][1]) / \
            (matrix[7, 7] * extra_params[6][0] + matrix[7, 7])  # коэффициенты c_n, n = 1, 2, ... , N - 2
i = 6
while i >= 0:
    params = extra_params[i]
    result[i] = params[0] * result[i + 1] + params[1]
    i -= 1


# расчет значения функции через сплайн на последнем отрезке
def spline(t):
    a_n = f[9]
    b_n = result[7] * h / 6 + (f[9] - f[8]) / h
    c_n = 0
    d_n = (0 - result[7]) / h
    spl = a_n + b_n * (t - x[9]) + (c_n * (t - x[9]) ** 2) / 2 + (d_n * (t - x[9]) ** 3) / 6
    return spl


print("Значение функции в точке 2010, полученное интерполяцией сплайном, равно " +
      str(spline(2010.)), end='\n')

