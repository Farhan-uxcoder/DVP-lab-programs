import matplotlib.pyplot as plt
import numpy as np

m = 5
c = 5

x = np.arange(-4, 4)
y = np.arange(-4, 4)

plt.axvline(color='g')
plt.axhline(color='g')

plt.title("Linear plotting")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(-x, y, color='k', marker='o', label='Y = -X')
plt.plot(x, -m*x + c, color='b', marker='^', label='Y = -5X + 5')

plt.legend()
plt.grid(True)
plt.show()