import plotly.express as px 
import pandas as pd 
import numpy as np 

# Get some data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Plot 
fig = px.line(df, x='Date', y='AAPL.High')

# Only thing I figured is - I could do this 
fig.add_scatter(x=df['Date'], y=df['AAPL.Low']) # Not what is desired - need a line 

# Show plot 
fig.show()
