import plotly
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

plotly.offline.plot(fig,filename='positives.html',config={'displayModeBar': False})
