# x and y given as array_like objects
import plotly.express as px
import os

if not os.path.exists("images"):
    os.mkdir("images")

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.update_layout(
        paper_bgcolor="rgb(255,255,255)",
        plot_bgcolor='rgb(255,255,255)'
         )

fig.show()
fig.write_image("images/fig1.eps")

