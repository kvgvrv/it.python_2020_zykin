import numpy as np
import matplotlib.pyplot as plt
t = np.arange(1, 6.01, 0.01)
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p = np.polyfit(x, y, 1)
p_f = np.poly1d(p)
q = np.polyfit(x, y, 2)
q_f = np.poly1d(q)

plt.subplot(121)
plt.scatter(x, y, s=9)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.plot(t, p_f(t), "g")
plt.grid(True)
plt.title("$x$")

plt.subplot(122)
plt.scatter(x, y, s=9)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.plot(t, q_f(t), "r")
plt.grid(True)
plt.title("$x^2$")

plt.show()