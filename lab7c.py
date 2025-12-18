# c. KDE Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a KDE plot for petal length
sns.kdeplot(iris["petal_length"], shade=True)
plt.title("KDE Plot of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Density")
plt.show()