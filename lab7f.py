# f. Box Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Tips dataset
tips = sns.load_dataset("tips")

# Create a box plot for total bill amounts by day
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box Plot: Distribution of Total Bill Amount by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill Amount ($)")
plt.show()