import pandas as pd
import csv 
import plotly.express as px
df=pd.read_csv("project.csv")
fig=px.scatter(x="student_id",y="level",size="attempt")
fig.show()