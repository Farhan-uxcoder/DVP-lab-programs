# g. Regression Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Tips dataset
tips = sns.load_dataset("tips")

# Create a linear regression plot
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.title("Linear Regression Plot: Total Bill vs. Tip")
plt.xlabel("Total Bill Amount ($)")
plt.ylabel("Tip Amount ($)")
plt.show()