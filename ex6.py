import numpy as np
import matplotlib.pyplot as plt


def ver(x):
    n = 0
    Q = 0
    while n < 301:
        y = (1/5)**n * np.cos(7**n * np.pi * x)
        Q += y
        n += 1
    return Q


x = np.arange(-2, 2.01, 0.01)
plt.plot(x, ver(x))
plt.grid(True)
plt.show()
