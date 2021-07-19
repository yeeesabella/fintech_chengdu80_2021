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


features = html.Div([html.Br(),
    dbc.Row(
            [   dbc.Col(
                    html.H6("Curate your watch list"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),
        dbc.Row(
            [   dbc.Col(
                    html.H6("Receive timely alerts on risk changes"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),dbc.Row(
            [dbc.Col(
                    html.H6("Downloadable historical data as csv"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,style={'height':'10px'}
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),dbc.Row(
            [dbc.Col(
                    html.H6("Insights into risk scores"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("𝗫"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),dbc.Row(
            [dbc.Col(
                    html.H6("Visualised charts for ease of interpretability"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("𝗫"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),dbc.Row(
            [dbc.Col(
                    html.H6("Comparison with other risk score providers for enhanced due diligence"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("𝗫"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("✔️"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),dbc.Row(
            [dbc.Col(
                    html.H6("Users per account"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("Up to 1 user"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("Min 10 users"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("Min 10 users"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        ),dbc.Row(
            [dbc.Col(
                    html.H6("Price per month (USD)"),
                    width=3,style={'height':'80px','verticalAlign':"middle","padding-bottom":"2"}
                ),
                dbc.Col(
                    html.H4("$5.99"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("$59.99"),
                    width=3,
                ),
                dbc.Col(
                    html.H4("Contact us! ☎️"),
                    width=3,
                ),
            ],
            justify="end",style={'textAlign':'center','margin-right':'10px'}
        )])


plans = dbc.Row(
            [
                dbc.Col(dbc.Card(
            dbc.CardBody([
                html.H4("Personal Plan", className="card-title"),
                html.P(
                    "The basics for the everyday investors.",
                    className="card-text",
                ),
                dbc.Button("Sign up free 🎉",
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
        ), width=3),
                dbc.Col(dbc.Card(
            dbc.CardBody([
                html.H4("Business Plan", className="card-title"),
                html.P(
                    "All your financial due diligence you need.",
                    className="card-text",
                ),
                dbc.Button("Request a free trial", color="primary"),
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
        ), width=3),
        dbc.Col(dbc.Card(
            dbc.CardBody([
                html.H4("Enterprise Plan", className="card-title"),
                html.P(
                    "Customisable solutions at your service.",
                    className="card-text",
                ),
                dbc.Button("Schedule a demo 💼", color="primary"),
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
        ), width=3),
            ],
            justify="end",style={'margin-right':'10px'}
        )

layout = html.Div(
    [html.Br(),html.H1(
                        "Pricing", style={'textAlign': 'right'}
                    ),
                    html.Br(),
        plans,features
    ],style={'margin-right':'20px'}
)