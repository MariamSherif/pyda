import numpy as np
import matplotlib.pyplot as plt

from matplotlib.legend_handler import HandlerLine2D
from math import sin, exp
from scipy.linalg import solve


def f(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x / 2.)

def fn(W):
    def fx(x):
        return sum(w * x ** n for n, w in enumerate(W))
    return fx

X = np.arange(1, 15, 0.1)

# matrix 1
A = np.array([
    (1, 1, ),
    (1, 15, ),
])

p = np.array([
    f(1),
    f(15),
])

W = solve(A, p)
f1 = fn(W)

# matrix 2
A = np.array([
    (1, 1, 1, ),
    (1, 8, 8**2, ),
    (1, 15, 15**2, ),
])

p = np.array([
    f(1),
    f(8),
    f(15),
])

W = solve(A, p)
f2 = fn(W)

# matrix 3
A = np.array([
    (1, 1, 1, 1),
    (1, 4, 4**2, 4**3),
    (1, 10, 10**2, 10**3),
    (1, 15, 15**2, 15**3),
])

p = np.array([
    f(1),
    f(4),
    f(10),
    f(15),
])

W = solve(A, p)
f3 = fn(W)

for index, fun in enumerate((f, f1, f2, f3)):
    plot, = plt.plot(X, [fun(x) for x in X], label='f%s(x)' % (index or ''))

plt.legend(handler_map={plot: HandlerLine2D(numpoints=4)})

with open('task2.txt', 'w') as answ:
    answ.write(('%.2f ' * 4).strip() % tuple(W))
