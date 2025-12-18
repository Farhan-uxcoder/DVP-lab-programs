# h. Bar Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data
data = sns.load_dataset("tips")

# Customize the color palette
sns.set_palette("pastel")

# Create a bar plot
sns.barplot(x="day", y="total_bill", data=data, ci=None)
plt.title("Customized Bar Plot with Color Palette")
plt.xlabel("Day of the Week")
plt.ylabel("TotalBillAmount($)")
plt.show()