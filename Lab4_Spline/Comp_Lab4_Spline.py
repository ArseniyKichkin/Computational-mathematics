import numpy as np
import sympy

x = sympy.Symbol('x')

args = [0.0, 1.0, 2.0, 3.0, 4.0]
vals = [2.0, 4.0, 20.0, 86.0, 262.0]

a3 = np.zeros(4)
a2 = np.zeros(4)
a1 = np.zeros(4)
a0 = np.zeros(4)

N = 4


def lagrange(x_, f_, t, n):  # функция вычисления интерполянта Лагранжа
    y = sympy.Symbol('y')
    y = 0
    for j in range(n):
        p1 = 1
        p2 = 1
        for i in range(n):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x_[i])
                p2 = p2 * (x_[j] - x_[i])
        y = y + f_[j] * p1 / p2
    return y


polynomial = lagrange(args, vals, x, N + 1).simplify()

for i in range(N):
    a3[i] = (polynomial.diff(x).subs(x, args[i + 1]) * (args[i + 1] - args[i]) - 2 * (
            vals[i + 1] - vals[i]) + polynomial.diff(x).subs(x, args[i]) * (args[i + 1] - args[i])) / (
                    args[i + 1] - args[i]) ** 3
    a2[i] = (-polynomial.diff(x).subs(x, args[i + 1]) * (args[i + 1] - args[i]) * (args[i + 1] + 2 * args[i]) + 3 * (
            vals[i + 1] - vals[i]) * (args[i + 1] + args[i])) / (args[i + 1] - args[i]) ** 3 - (
                    polynomial.diff(x).subs(x, args[i]) * (args[i + 1] - args[i]) * (
                    args[i] + 2 * args[i + 1])) / (args[i + 1] - args[i]) ** 3
    a1[i] = (polynomial.diff(x).subs(x, args[i + 1]) * args[i] * (args[i + 1] - args[i]) * (
            2 * args[i + 1] + args[i]) - 6 * (vals[i + 1] - vals[i]) * args[i] * args[i + 1]) / (
                    args[i + 1] - args[i]) ** 3 + (
                    polynomial.diff(x).subs(x, args[i]) * args[i + 1] * (args[i + 1] + 2 * args[i]) * (
                    args[i + 1] - args[i])) / (
                    args[i + 1] - args[i]) ** 3
    a0[i] = (-polynomial.diff(x).subs(x, args[i + 1]) * args[i] ** 2 * args[i + 1] * (args[i + 1] - args[i]) + vals[
        i + 1] * args[i] ** 2 * (3 * args[i + 1] - args[i]) + vals[i] * args[i + 1] ** 2 * (
                         args[i + 1] - 3 * args[i]) - polynomial.diff(x).subs(x, args[i]) * args[i] * args[
                 i + 1] ** 2 * (args[i + 1] - args[i])) / (args[i + 1] - args[i]) ** 3


poly0 = x ** 3 * a3[0] + x ** 2 * a2[0] + x * a1[0] + a0[0]
poly1 = x ** 3 * a3[1] + x ** 2 * a2[1] + x * a1[1] + a0[1]
poly2 = x ** 3 * a3[2] + x ** 2 * a2[2] + x * a1[2] + a0[2]
poly3 = x ** 3 * a3[3] + x ** 2 * a2[3] + x * a1[3] + a0[3]


print(a3, '\n')
print(a2, '\n')
print(a1, '\n')
print(a0, '\n')

print(poly0, '\n')
print(poly1, '\n')
print(poly2, '\n')
print(poly3, '\n')


print(polynomial)
#print(poly3, '\n')
#print(poly3.subs(x, 1.8))
