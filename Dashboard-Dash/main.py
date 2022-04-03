import pandas as pd 
import plotly.express as px
import plotly.graph_objs as go

import dash 
from dash import dcc, html 
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#-----------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv('/Users/tom/Documents/Python/My-projects/Dashboard-Dash/bees.csv')
df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df)

app.layout = html.Div([
    
    html.H1("Web application dashboard with Dash", style={'text-algin': 'center'}),
    
    dcc.Dropdown(id="select year",
                 options=[
                     {"label" : "2015", "value": 2015},
                     {"label" : "2016", "value": 2016},
                     {"label" : "2017", "value": 2017},
                     {"label" : "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width', "40%"}
                ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    dcc.Graph(id='my_bee_map', figure={})
    
])
                    
                       
                       
                       
                       
                       
                       
                       ])