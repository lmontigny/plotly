import plotly.express as px
import pandas as pd 
import numpy
 
num = 15
x = list(range(0,15))
y = list(range(0,15))

df = pd.DataFrame({'x':x, 'y':y})
 
fig = px.line(df, x="x", y="y", title="A Plotly Express Figure")
fig.update_layout(xaxis_title = 'X', yaxis_title = 'Y')
fig.show()



