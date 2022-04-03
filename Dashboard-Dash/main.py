from turtle import color
import pandas as pd 
import plotly.express as px
import plotly.graph_objs as go

import dash 
from dash import dcc, html 
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#---------------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv('/Users/tom/Documents/Python/My-projects/Dashboard-Dash/bees.csv')
df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)

#---------------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

#---------------------------------------------------------------------------------------
# Connect the plotly graphs with dash components 
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graphs(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year choosen by user was: {}".format(option_slctd)
    
    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]
    
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope='usa',
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
        
    )
    
    fig_2 = px.bar(
        data_frame=dff,
        y='Pct of Colonies Impacted',
        x='State'
    )
    
    return container, fig
    



if __name__ == '__main__':
    app.run_server(debug=True)               
                       
                       
                       
                       
                       
                    