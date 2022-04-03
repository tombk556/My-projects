import pandas as pd 
import plotly.express as px
import plotly.graph_objs as go

import dash 
from dash import dcc, html 
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#-----------------------------------------------------
# Import and clean data (importing csv into pandas)
