# watch list page
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sklearn import datasets
from sklearn.cluster import KMeans

from flask_login import logout_user, current_user
import pathlib

BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()
watchlist_df = pd.read_csv(DATA_PATH.joinpath("my_watchlist.csv"))
watchlist_df.drop_duplicates(inplace=True)

###############################################################################
########### Features ###########
###############################################################################
layout = dbc.Container([html.H1(
                        "My Watch List", style={'textAlign': 'right'}
                    ),
                    html.Hr(),
                    dbc.Table.from_dataframe(watchlist_df, striped=True, bordered=True, hover=True,style={
            'textAlign': 'left', 'margin-left': '30%', 'width': '100px'})
],style={'margin-left':'20%'})

