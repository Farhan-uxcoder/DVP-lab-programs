import plotly.graph_objects as go
import numpy as np


x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
x,y = np.meshgrid(x,y)
z = np.sin(np.sqrt(x**2+y**2))

fig = go.Figure(data=[go.Surface(z=z,x=x,y=y)])

fig.update_layout(scene=dict(
    xaxis_title="X axis",
    yaxis_title = "Y axis",
    zaxis_title = "Z axis"
    ),
    title = '3D surface plot examples',
    )

fig.show()