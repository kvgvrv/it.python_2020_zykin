import numpy as np
x = 1
while x != 10000:
    y = np.log((1 / (np.exp(np.sin(x) + 1))) / (5 / 4 + 1 / x**15)) / np.log(1 + x**2)
    if x != 100:
        print(y)
    x *= 10