import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 6.01, 0.01)
plt.figure(figsize=(8, 8))
plt.plot(x, x*x - x - 6)
plt.grid(True)
plt.text(-2, 0, r"$x{1} = -2$")
plt.text(2.5, 0, r"$x{2} = 2,5$")
plt.show()
