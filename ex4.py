import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
a = input()
with plt.xkcd():
    plt.plot(x, eval(a))
    plt.title("Ваша функция")
plt.show()
