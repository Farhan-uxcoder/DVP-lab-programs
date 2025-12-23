import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import webbrowser


# Force Plotly to use browser renderer
pio.renderers.default = "browser"   # or "vscode" if you have Jupyter extension

# Generate random data
np.random.seed(42)
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

scatter3d = go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=z,
        colorscale='Viridis',
        opacity=0.8
    )
)

fig = go.Figure(data=[scatter3d])
fig.show()