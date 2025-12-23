'''
write a python pgm to draw a 3d bar graph petal length(x) , petal width(y) ,sapel length(z)
'''
import matplotlib.pyplot as plt
import numpy as np

petal_length = [1.4, 1.5, 1.3, 1.7, 1.6]
petal_width  = [0.2, 0.2, 0.2, 0.4, 0.3]
sepal_length = [5.1, 4.9, 4.7, 4.6, 5.0]

n = len(petal_length)

x = np.arange(n)
y = np.array([0]*n)
y2 = np.array([1]*n)
y3 = np.array([2]*n)

dx = np.ones(n) * 0.5
dy = np.ones(n) * 0.5

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x, y, np.zeros(n), dx, dy, petal_length, color='r', alpha=0.7, label='Petal Length')
ax.bar3d(x, y2, np.zeros(n), dx, dy, petal_width, color='g', alpha=0.7, label='Petal Width')
ax.bar3d(x, y3, np.zeros(n), dx, dy, sepal_length, color='b', alpha=0.7, label='Sepal Length')

ax.set_xlabel('Sample Index')
ax.set_ylabel('Feature')
ax.set_zlabel('Measurement (cm)')
ax.set_title('3D Bar Graph: Petal & Sepal Measurements')

ax.set_yticks([0,1,2])
ax.set_yticklabels(['Petal Length','Petal Width','Sepal Length'])


ax.legend()

plt.show()