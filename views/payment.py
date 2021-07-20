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

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()


plans = dbc.Row(
            [
                dbc.Col(dbc.Card(
            dbc.CardBody([
                html.H4("PAYMENT DETAILS", className="card-title"),
                dbc.Button("Continue",
                    type='submit', href="/signup",color="primary"),
                html.P(),
                html.P(
                    "· Industry-first blockchain-secured risk analysis platform",
                    className="card-text",
                ),
                html.P(
                    "· Real-time business information from our data partners",
                    className="card-text",
                ),
            ],style={'background-color':'#C6D9F1'})
        ), width=5,style={'height':'100px'})
            ],
            justify="middle",style={'margin-left':'550px'}
        )

cc_details = dbc.FormGroup(
    [
        dbc.Label("Card Holder's Name"),
        dbc.Input(type="text",style={"width":"5px",'margin-left':'100%'})
    ]
)

layout = html.Div(
    [html.Br(),html.H1("Payment gateway", style={'textAlign': 'center'}
                    ),
                    html.Br(),html.P("text"),plans,
                    cc_details
    ]
    # style={'margin-right':'20px'}
)