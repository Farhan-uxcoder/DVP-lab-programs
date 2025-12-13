import matplotlib.pyplot as plt
import numpy as np

plt.title("sales v/s price with profit")

price = np.asarray([2.5, 1.23, 4.02, 3.35, 5.00, 4.44])
sales_per_day = np.asarray([34, 64, 49, 22, 19, 13])
profit = np.asarray([20, 35, 40, 20, 27, 5])  # matched length

plt.scatter(
    x=price,
    y=sales_per_day,
    s=profit * 20,
    c='r',
    edgecolors='b',
    marker='*'   # ⭐ star marker
)
plt.xlabel("chocolates price", fontsize=15)
plt.ylabel("sales per day", fontsize=15)
plt.xticks(price)
plt.yticks(sales_per_day)
plt.show()