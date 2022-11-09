import numpy as np

nodes = np.linspace(0, np.pi / 2, 2455)
step = 0.00064


def expression(x):
    value = np.sin(100 * x) / (1 + x ** 2)
    return value


def newton_cotes():
    result = 0
    for i in range(1, len(nodes)):
        result += (expression(nodes[i - 1]) + 3 * expression((2 * nodes[i - 1] + nodes[i]) / 3) + 3 * expression(
            (nodes[i - 1] + 2 * nodes[i]) / 3) + expression(nodes[i])) * step / 8
    return result


x1_ = np.sqrt(
    (14997 * np.sin(100) - 499700 * np.cos(100)) / (5000 * (np.sin(100) - 100 * np.cos(100))))
x2_ = - np.sqrt(
    (14997 * np.sin(100) - 499700 * np.cos(100)) / (5000 * (np.sin(100) - 100 * np.cos(100))))

x1 = np.pi / 4 + (np.pi / 4) * np.sqrt(
    (14997 * np.sin(100) - 499700 * np.cos(100)) / (5000 * (np.sin(100) - 100 * np.cos(100))))
x2 = np.pi / 4 + (np.pi / 4) * x2_

w1 = (np.sin(100) - 100 * np.cos(100)) / (2 * x1_ * 5000)
w2 = - w1

res = (np.pi / 4) * (w1 * expression(x1) + w2 * expression(x2))

print(res)
