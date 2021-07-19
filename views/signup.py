import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlLogin', refresh=True),
        html.Div([
            dbc.Container(
                html.Img(
                    src='/assets/finnus_logo_transparent.png',
                    className='center',
                    style={'textAlign': 'center',
                           'height': '20%', 'width': '20%'}
                ),
            ),
            html.H4('Create account',
                    style={'textAlign': 'center',
                           'margin-top': '30px',
                           'border-width': '3px', 'border-color': '#a0a3a2'
                           }),
            dbc.Container(id='loginType', children=[
                dcc.Input(
                    placeholder='Enter your username',
                    type='text',
                    id='usernameBox',
                    className='form-control',
                    n_submit=0,
                    style={'textAlign': 'center', 'margin-left': '28%', 'width': '450px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px', 'border-width': '3px', 'border-color': '#a0a3a2'
                           }
                ),
                html.Br(),
                dcc.Input(
                    placeholder='Enter your password',
                    type='password',
                    id='passwordBox',
                    className='form-control',
                    n_submit=0,
                    style={'textAlign': 'center', 'margin-left': '28%', 'width': '450px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px', 'border-width': '3px', 'border-color': '#a0a3a2'
                           }
                ),
                html.Br(),
                html.Button(
                    children='CREATE ACCOUNT',
                    n_clicks=0,
                    type='submit',
                    id='loginButton',
                    className='btn btn-primary btn-lg',
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '200px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'
                           }
                ),
                html.Br(),
            ], className='form-group')
        ]
        )
    ]
        # , className='jumbotron'
    )
])
