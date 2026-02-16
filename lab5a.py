import matplotlib.pyplot as plt
import numpy as np

grades = [70,71,72,78,79,80,88, 92, 95, 97, 85, 90, 93, 99, 100, 91, 94]

plt.hist(
    grades,
    bins=[70, 75, 80, 85, 90, 95, 100],
    edgecolor = 'k'
    )

plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.title("Grades in a Class")

plt.show()