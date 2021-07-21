# Dash packages
from app import app, User
import numpy
import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pathlib
import time


cc_details = dbc.Row(
    [
        dbc.Col(dbc.Card(
            dbc.CardBody([
                html.H3("Payment details", className="card-title"),
                html.H6("Accepted payments", className="card-title"),
                dbc.Col([html.Img(src='/assets/accepted_cards.jpeg', style={'width': '90%'}),
                         html.Img(src='/assets/accepted_cards_alipay_wechat.jpeg', style={'width': '70%'})],
                        style={'textAlign': 'center'}),
                html.P(),
                dbc.RadioItems(
                    options=[
                        {"label": "Personal", "value": 1},
                        {"label": "Business", "value": 2}
                    ],
                    value=1,
                    id="payment-option-input",
                ),
                html.P(),
                dbc.FormGroup(
                    [
                        dbc.Label("Name"),
                        dbc.Input(placeholder="John Doe", type="text"),
                    ]
                ), dbc.FormGroup(
                    [
                        dbc.Label("Card number"),
                        dbc.Input(
                            placeholder="0072 5420 2145 1234", pattern="^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$", type="text"),
                    ]
                ), dbc.FormGroup(
                    [
                        dbc.Label("Expiry date"),
                        dbc.Input(placeholder="07 / 20", type="text"),
                    ]
                ), dbc.FormGroup(
                    [
                        dbc.Label("CCV"),
                        dbc.Input(placeholder="789", type="number"),
                    ]
                ),
                html.Div([dbc.Button("Complete payment",
                           type='submit', id='loading-input',href="/premium_content", 
                           color="primary", style={'width': 'auto'}),
                            dcc.Loading(
                    id="loading",
                    children=[html.Div([html.Div(id="loading-output")])],
                    type="circle",
                )]),
                           html.P()
            ])
        ), width=5, style={'height': '100px'})
    ],
    justify="middle", style={'margin-left': '550px'}
)

layout = html.Div(
    [html.Br(),
     # html.H1("Payment gateway", style={'textAlign': 'center'}),
     html.Br(),
     cc_details
     ]
    # style={'margin-right':'20px'}
)


@app.callback(Output("loading-output", "children"), 
Input("loading-input", "value"))
def input_triggers_nested(value):
    time.sleep(1)
    return value