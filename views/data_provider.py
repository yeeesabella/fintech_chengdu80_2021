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
BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()

###############################################################################
########### Features ###########
###############################################################################
layout = dbc.Container([html.H1(
                        "Your Account Summary", style={'textAlign': 'center'}
                    ),
                    html.Img(src='/assets/data_provider_snapshot.png', height="500px",style={"margin-left":"100px"})
], className="mt-4")
