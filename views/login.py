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
            html.H4('Log In',
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
                    children='Login',
                    n_clicks=0,
                    type='submit',
                    id='loginButton',
                    className='btn btn-primary btn-lg',
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '200px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'
                           }
                ),
                html.Br(),
            ], className='form-group'),
            html.P('New to FinNUS? Create an account for free 🎉',
                   style={'textAlign': 'center'}
                   ),
                   dbc.Button(
                    children='Sign Up',
                    type='submit',
                    color='warning',
                    href='/signup',
                    id='signupbutton',
                    className='btn btn-primary btn-lg',
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '200px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'
                           }
                ),
        ]
        )
    ]
        # , className='jumbotron'
    )
])


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - REDIRECT TO WATCHLIST IF LOGIN DETAILS ARE CORRECT
################################################################################
@app.callback(Output('urlLogin', 'pathname'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def sucess(n_clicks, usernameSubmit, passwordSubmit, username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            return '/'
        else:
            pass
    else:
        pass


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('usernameBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('passwordBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'
