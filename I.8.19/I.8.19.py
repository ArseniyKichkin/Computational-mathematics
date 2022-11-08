import math

import sympy as sp
import numpy as np


t = np.linspace(10, 11, 100)

x = sp.Symbol('x')
f = sp.sin(x)
r = [0 for i in range(100)]
delta = [1 for i in range(100)]
p = 1


def coefficient(f, n):
    return (f.diff(x, n).subs(x, 0)) / math.factorial(n)


def mclaurent(x, n):
    return sum([coefficient(f, i) * x ** i for i in range(n + 1)])


while max(delta) > 1E-3:
    p += 1
    y = mclaurent(x, p)
    for i in range(len(t)):
        delta[i] = abs(y.subs(x, t[i]) - f.subs(x, t[i]))


print(p, end='\n')
print(abs(mclaurent(10, p) - f.subs(x, 10)))




