import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
sns.jointplot(x="sepal_length",y="sepal_width",data=iris,kind="reg")
plt.show()