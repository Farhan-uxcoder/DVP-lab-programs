import matplotlib.pyplot as plt
import numpy as np

grades = [70,71,72,78,79,80,88, 92, 95, 97, 85, 90, 93, 99, 100, 91, 94]

plt.figure(figsize=(8, 6))
plt.hist(
    grades,
    bins=[70, 75, 80, 85, 90, 95, 100],
    edgecolor='black',
    alpha=0.7,
    color='skyblue'
)

plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.title("Grades in a Class")
plt.xlim(70, 100)
plt.show()