# d. Heat Map

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Calculate the correlation matrix
correlation_matrix = iris.corr()

# Create a heatmap of the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap of Feature Correlations in the Iris Dataset")
plt.show()