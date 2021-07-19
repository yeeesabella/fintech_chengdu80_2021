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

###############################################################################
########### Features ###########
###############################################################################
layout = dbc.Container([html.H1(
                        "About Us", style={'textAlign': 'center'}
                    ),
                    html.P("FinNUS is an integrated one-stop risk evaluation platform that utilises technology to provide real-time information from companies. With data secured using blockchain immutable ledger, you can be assured that our risk evaluation as well as data can be trusted. FinNUS is created with the objective of xxx", style={'textAlign': 'center'}),
                    html.H1(
                        "What we do", style={'textAlign': 'center'}
                    ),                    
                    html.P("For investors, corporate companies and regulators - we provide risk analytics xxx. Our data providers xxx", style={'textAlign': 'center'}),
                    html.H1(
                        "Founders", style={'textAlign': 'center'}
                    ),
                    html.P("Our founders came from a diversed background with expertise in banking and finance to technology.", style={'textAlign': 'center'}),
                    html.Img(src='/assets/team.png', height="500px",style={"margin-left":"100px"})
], className="mt-4")
