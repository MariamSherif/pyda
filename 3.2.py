import numpy as np
import matplotlib.pyplot as plt

from math import sin, exp
from scipy.optimize import differential_evolution


def f(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x / 2.)

X = np.arange(1, 30, .1)
plt.plot(X, [f(x) for x in X])

mini = differential_evolution(f, ((1, 30), ))
minx, ans = mini.x[0], mini.fun

plt.plot(minx, f(minx), 'o')
plt.show()

print mini.nfev

with open('task2.txt', 'w') as answ:
    answ.write('%.2f' % ans)
