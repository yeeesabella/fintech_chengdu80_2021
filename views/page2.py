
# Dash packages
from app import app
import numpy

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pathlib

# Path
BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()
fin_data = pd.read_csv(DATA_PATH.joinpath("stocks_price_sample.csv"))

###############################################################################
########### PAGE 2 LAYOUT ###########
###############################################################################
layout = dbc.Container([
        
        html.Div(dbc.Row(dbc.Alert("⛔️ This page is accessible to paid users only. ", color="warning",style={"left": "150px","width":"1100px",'textAlign': 'center',}))),
        # html.Hr(),


], className="mt-4")
