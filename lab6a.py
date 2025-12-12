import matplotlib.pyplot as plt
import numpy as np 

m = 5
c = 5

x = np.arange(-4, 4)
y = np.arange(-4, 4)

# Draw axes lines
plt.axvline(color='g')   # Vertical line at x=0
plt.axhline(color='g')   # Horizontal line at y=0

plt.title("Linear plotting")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# First line
plt.plot(-x, y, color='k', marker='o', label='Y = -X')

# Second line
plt.plot(x, -m*x + c, color='b', marker='^', label='Y = -5X + 5')

# Add legend and grid
plt.legend()
plt.grid(True)

# Show the plot
plt.show()