import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.set_palette("pastel")
sns.barplot(x="day",y="total_bill",data=data,ci=None)

plt.title("Costomised bar plot with color pallete")
plt.xlabel("Day of the week")
plt.ylabel("Day of the week")

plt.show()