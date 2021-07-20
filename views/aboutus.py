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
                    html.Hr(),
                    html.P("FinNUS is an integrated one-stop risk evaluation platform that utilises machine learning to provide explainable risk analytics. With data secured using blockchain immutable ledger, you can be assured that our risk evaluation as well as data can be trusted. FinNUS is created with the objective of providing risk analytics and decision support to risk analysts, corporate managers and regulatory authorities. We offer customized pricing plans to meet your business and technical needs.", style={'textAlign': 'center'}),
                    html.H1(
                        "Founders", style={'textAlign': 'center'}
                    ),
                    html.Hr(),
                    html.P("Our founders came from a diverse background with expertise in banking, consulting, finance, and technology. Our combined 20+ years experience in finance and technology have allowed us to a create a world-class risk management platform to serve your diverse business needs.", style={'textAlign': 'center'}),
                    html.Img(src='/assets/team.png', height="500px",style={"margin-left":"100px"})
], className="mt-4")
