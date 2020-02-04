# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

from joblib import load
mypipeline = load('assets/mypipeline.joblib')


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting Oscars for Best Motion Picture

            This web app is using data about Oscar Awards for the Best Motion Pictue since 1942 as attempt to demystify the magic of cinematography, and predict future winners. 
            
            It's a great tool to consider factors that make an award-winning movie - those we can measure and those we can't quantify, and what it tells about our culture. 
            
            Movie buffs should enjoy! 
  

            """
        ),
        dcc.Link(dbc.Button('Predict awards', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])