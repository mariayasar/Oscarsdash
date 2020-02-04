# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Imports from this application
from app import app

from joblib import load
mypipeline = load('assets/mypipeline.joblib')

# 3 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('### Predictions', className='mb-5'), 
        dcc.Markdown('###### Metascore'),
        dcc.Slider(
            id='metascore', 
            min=0, 
            max=100, 
            step=1, 
            value=85, 
            marks={n: str(n) for n in range(0,101,10)}, 
            className='mb-5', 
        ), 
        
        dcc.Markdown('###### Average IMDB rating'), 
        dcc.Slider(
            id='averagerating', 
            min=5, 
            max=10, 
            step=0.1, 
            value=8.5, 
            marks={n: str(n) for n in range(5,11,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('###### IMDB Number of votes'), 
        dcc.Slider(
            id='numvotes', 
            min=78000, 
            max=2000000, 
            step=250000, 
            value=1000000, 
            marks={n: str(n) for n in range(500000,2000001,500000)}, 
            className='mb-5', 
        ), 

        
        dcc.Markdown('###### Rating'), 
        dcc.Dropdown(
            id='rating', 
            options= [
                {'label': 'R', 'value': 1},
                {'label': 'PG-13', 'value': 2},
                {'label': 'PG', 'value': 3},
                {'label': 'G', 'value': 4},
          
            ],
            className = 'mb-5',
            value=1,
            placeholder='Select movie rating' 
        ),
   
      
        
 ],
    md=4,
)


column2 = dbc.Col(
    [
        dcc.Markdown('###  ', className='mb-5'), 


        dcc.Markdown('###### Best director nomination'), 
        dcc.Dropdown(
        id='directing_nomination', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ),
        
         dcc.Markdown('###### Best lead actor nomination'), 
        dcc.Dropdown(
        id='actor_in_a_leading_role_nomination', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ),
        
         dcc.Markdown('###### Best lead actress nomination'), 
        dcc.Dropdown(
        id='actress_in_a_leading_role_nomination', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ),  
        
         dcc.Markdown('###### Best suporting actress nomination'), 
        dcc.Dropdown(
        id='actor_in_a_supporting_role_nomination', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ),  
        
         dcc.Markdown('###### Best supporting actor nomination'), 
        dcc.Dropdown(
        id='actress_in_a_supporting_role_nomination', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ),  
        
         
        dcc.Markdown('###### Best cinematography nomination'), 
        dcc.Dropdown(
        id='cinematography_nomination', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ), 
        
         
        dcc.Markdown('###### Opening weekend boxoffice'), 
        dcc.Slider(
            id='opening_wk', 
            min=50000, 
            max=20000000, 
            step=10000000, 
            value=1500000, 
            marks={n: str(n) for n in range(50000,20000010,19950000)}, 
            className='mb-5', 
        ), 
        
             
        dcc.Markdown('###### Is Director female?'), 
        dcc.Dropdown(
        id='is_woman', 
        options=[
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0},
            ],
            multi=False,
            value=0
        ),  
        
         dcc.Markdown('###### Director age'), 
        dcc.Slider(
            id='dir_age', 
            min=20, 
            max=80, 
            step=10, 
            value=50, 
            marks={n: str(n) for n in range(20,85,10)}, 
            className='mb-5', 
        ), 
        
        
    ],
    
    md=4,
)





column3 = dbc.Col(
    
        
          [
        html.H2('Probability of Winning Best Picture', className= 'mb-3'),
        html.Div(id='prediction-content', className='lead')
#        html.Div(id='image')
          ]
)
        
        
layout = dbc.Row([column1, column2, column3])
        
        
@app.callback(
    Output('prediction-content', 'children'),
    [
    Input('actor_in_a_leading_role_nomination', 'value'),
    Input('actor_in_a_supporting_role_nomination', 'value'),
    Input('actress_in_a_leading_role_nomination', 'value'),
    Input('actress_in_a_supporting_role_nomination', 'value'),
    Input('directing_nomination', 'value'),
    Input('cinematography_nomination', 'value'),
    Input('averagerating', 'value'),
    Input('numvotes', 'value'),
    Input('dir_age', 'value'),
    Input('is_woman', 'value'),
    Input('rating', 'value'),
    Input('metascore', 'value'),
    Input('opening_wk', 'value')
    ],
)
        
        
def predict(actor_in_a_leading_role_nomination,
       actor_in_a_supporting_role_nomination,
       actress_in_a_leading_role_nomination,
       actress_in_a_supporting_role_nomination, directing_nomination,
       cinematography_nomination,  averagerating,
       numvotes, dir_age, is_woman, rating, metascore, 
       opening_wk 
      ):
    df = pd.DataFrame(
    columns=['actor_in_a_leading_role_nomination',
    'actor_in_a_supporting_role_nomination',
    'actress_in_a_leading_role_nomination',
    'actress_in_a_supporting_role_nomination', 'directing_nomination',
    'cinematography_nomination',  'averagerating',
    'numvotes', 'dir_age', 'is_woman', 'rating', 'metascore', 
    'opening_wk'
          ],
        data=[[actor_in_a_leading_role_nomination,
           actor_in_a_supporting_role_nomination,
           actress_in_a_leading_role_nomination,
           actress_in_a_supporting_role_nomination, directing_nomination,
           cinematography_nomination, averagerating,
           numvotes, dir_age, is_woman, rating, metascore,
           opening_wk,
           ]]
    )
    
    y_pred=mypipeline.predict(df)[0]
    y_pred_proba=mypipeline.predict_proba(df)[0]
    return f'Probability of winning the Best Picture is {y_pred_proba[1]}' #f'{y_pred_proba*100:.0f}% chance of {y_pred}'

#
   
        
       


