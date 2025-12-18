# a. Join Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a joint plot for sepal length and sepal width
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="reg")
plt.show()