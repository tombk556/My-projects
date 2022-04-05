from curses import meta
from operator import index
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader as web
import datetime

#----------------------------------------------------------------------------#
# Create the data set from the pandas_datareader API

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 12, 3)

df = web.DataReader(['AMZN', 'GOOGL', 'FB', 'PFE', 'BNTX', 'MRNA'],
                    'stooq', start=start, end=end)

df = df.stack().reset_index()
# print(df[:15])

#df.to_csv('/Users/tom/Documents/Python/My-projects/Dashboard-Dash/Financial Dashboard/mystocks.csv', index=False)

#----------------------------------------------------------------------------#
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width = device-width, intial-scale=1.0'}])

#----------------------------------------------------------------------------#
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Stock Market Dashboard",
                        className='text-center text-primary, mb-4'),
                width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='my-dpdn', multi=False, value='AMZN',
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df['Symbols'].unique())]),
            dcc.Graph(id='line-fig', figure={})
        ], width={'size': 5, 'offset': 1, 'order': 2}),
        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['PFE', 'BNTX'],
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df['Symbols'].unique())],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ], width={'size': 5, 'offset': 1, 'order': 1})
    ], justify='around'),


    dbc.Row([
        dbc.Col([
            html.P("Select Company Stock:",
                   style={"textDecoration": "underline"}),
            dcc.Checklist(id='my-checklist', value=['PFE', 'BNTX', 'AMZN'],
                          options=[{'label': x, 'value': x}
                                   for x in sorted(df['Symbols'].unique())],
                          labelClassName='mr-3 text-success'
                          ),
            dcc.Graph(id='my-hist', figure={})
        ], width={'size': 5, 'offset': 1, 'order': 1})
    ], justify='left')



], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
