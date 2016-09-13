import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

from math import sin, exp
from scipy.optimize import minimize, differential_evolution

def f(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x / 2.)

def h(x):
    return int(f(x))

X = np.arange(1, 30, .1)
plt.plot(X, [f(x) for x in X], label='f(x)')
plot, = plt.plot(X, [h(x) for x in X], label='h(x)')

mini = minimize(h, 30, method='BFGS')
minx1, answ1 = mini.x[0], mini.fun
print mini.nfev

mini = differential_evolution(h, ((1, 30), ))
minx2, answ2 = mini.x[0], mini.fun
print mini.nfev

plt.plot(minx1, answ1, 'o', label='BFGS')
plt.plot(minx2, answ2, 'o', label='EVOL')

plt.legend(handler_map={plot: HandlerLine2D(numpoints=2)})
plt.show()

with open('task3.txt', 'w') as answ:
    answ.write('%.2f %.2f' % (answ1, answ2))
