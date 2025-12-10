import matplotlib.pyplot as plt
categories = ["Science", "Commerce", "Arts","Literature"]
value = [12,25,15,30]
plt.bar(categories,value,color='m')
plt.xlabel("Categories")
plt.ylabel("Value")
plt.title("Bar plot example")
plt.show()