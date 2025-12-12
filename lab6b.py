import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(0,10,100)

y1 = x
y2 = x**2
y3 = np.sin(x)

plt.figure(figsize=(8,6))   # corrected argument name

# Linear line
plt.plot(x, y1, label='Linear', color='blue', linestyle='-', linewidth=2)

# Quadratic line
plt.plot(x, y2, label='Quadratic', color='red', linestyle='--', linewidth=2)

# Sine line
plt.plot(x, y3, label='Sine', color='green', linestyle=':', marker='^', markersize=4, linewidth=2)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Linear, Quadratic, and Sine Plot with Formatting")
plt.legend()
plt.grid(True)
plt.show()