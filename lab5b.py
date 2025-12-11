import matplotlib.pyplot as plt

# Forest area data (in sq km, sample values)
states = ["Madhya Pradesh", "Arunachal Pradesh", "Chhattisgarh", "Odisha", "Maharashtra"]
forest_area = [77482, 66464, 55547, 51345, 50682]

# Highlight one state (e.g., Madhya Pradesh)
explode = [0.1, 0, 0, 0, 0]  # only the first slice is "exploded"

plt.figure(figsize=(8, 6))
plt.pie(
    forest_area,
    labels=states,
    autopct="%1.1f%%",
    startangle=140,
    explode=explode,
    shadow=True
)

plt.title("Forest Area in 5 Indian States")
plt.legend(states, title="States", loc="best")
plt.show()