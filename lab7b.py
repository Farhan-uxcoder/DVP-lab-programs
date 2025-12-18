# b. Hexagon distribution.

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a hexbin distribution plot for sepal length and sepal width
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="hex", color="b")
plt.title("Hexagon Distribution: Sepal Length vs. Sepal Width")
plt.show()