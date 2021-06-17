import csv
import pandas as pd

df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
	x = df.groupby("level")["attempt"].mean(),
	y = ['level 1', 'level 2', 'level 3', 'level 4'],
	orientation = 'h',
	mode = 'markers'
	))

fig.show()
