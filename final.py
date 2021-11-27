import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("Student Marks vs Days Present.csv")
fig = ff.create_distplot([df["Marks In Percentage"].tolist()], ["Marks In Percentage"], show_hist=False)
fig.show()
