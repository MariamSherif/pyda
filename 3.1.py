import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

from math import sin, exp
from scipy.optimize import minimize


def f(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x / 2.)

X = np.arange(1, 30, .1)

plt.plot(X, [f(x) for x in X])

for start in np.arange(5, 27, 2):
    minx = minimize(f, start).x
    plot, = plt.plot(minx, f(minx), 'o', label='%d-%f' % (start, minx))

plt.legend(handler_map={plot: HandlerLine2D(numpoints=2)})
plt.show()

mini = minimize(f, 2, method='BFGS')
minx1, answ1 = mini.x[0], mini.fun
mini = minimize(f, 30, method='BFGS')
minx2, answ2 = mini.x[0], mini.fun
# plot
plt.plot(X, [f(x) for x in X])
plt.plot(minx1, f(minx1), 'x')
plt.plot(minx2, f(minx2), 'o')
plt.show()

with open('task1.txt', 'w') as answ:
    answ.write('%.2f %.2f' % (answ1, answ2))
