import matplotlib.pyplot as plt

categories = ["maths","science","social"]
value = [100,78,56]

plt.bar(categories,value)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()