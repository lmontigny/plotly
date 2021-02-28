import plotly
import plotly.graph_objs as G
 
 
import numpy
 
num = 15
x = numpy.random.randn(num)
y = numpy.random.randn(num)
 
# Create a trace
follow = G.Scatter(
    x = x,
    y = y,
    mode = 'lines'
)
output = [follow]
 
 
plotly.offline.plot(output, filename='lines.html')
