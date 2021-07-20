# Dash packages
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sklearn import datasets
from sklearn.cluster import KMeans

from flask_login import logout_user, current_user
import plotly.express as px
import pathlib
from dash.exceptions import PreventUpdate


BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()
entity_df = pd.read_csv(DATA_PATH.joinpath("full_search_list.csv"))
entity_df['Entity ID'] = entity_df['Entity ID'].astype(int).astype(str)

controls = dbc.Container(
    dbc.Col([
        dbc.Row(
    [
        dbc.Label("Entity ID"),
        dcc.Dropdown(
            id="x1",
            options=[
                {"label": col, "value": col} for col in entity_df['Entity ID'].unique()
            ],
            style={"width": "300px"}
        ),
        dbc.Label("Industry"),
        dcc.Dropdown(
            id="x2",
            options=[
                {"label": col, "value": col} for col in entity_df['Industry'].unique()
            ],
            style={"width": "300px"}
        )],
    justify="between"), 
    html.Br(),
    dbc.Row([
        dbc.Label("Province"), dcc.Dropdown(
            id="x3",
            options=[
                {"label": col, "value": col} for col in entity_df['Province'].unique()
            ],
            style={"width": "200px"}
        ),
        dbc.Label("Enterprise Type"),
        dcc.Dropdown(
            id="x4",
            options=[
                {"label": col, "value": col} for col in entity_df['Enterprise Type'].unique()
            ],
            style={"width": "200px"}
        ),
        dbc.Label("Main Risk"),
        dcc.Dropdown(
            id="x5",
            options=[
                {"label": col, "value": col} for col in entity_df['Main Risk'].unique()
            ],
            style={"width": "200px"}
        )],
    justify="between")],
    )
    ) 

show_entity=dbc.Row([html.H4("List of Companies",style={'margin-left':'40px'})])


table=html.Div(id='list-of-search-results', style={'textAlign': 'left', 'width': '1000px'})

layout=dbc.Container(
    [
        html.H1("Entity Search", style={"textAlign": "right"}),
        html.Hr(),
        dbc.Col(controls,align="left"),
        html.Br(),
        show_entity,
        html.P(),
        table,
        html.P()
    ], style={'margin-left': '20%'}
)

link=[html.A(html.P('View details'),href="/premium_content")]


@ app.callback(
    Output("list-of-search-results", "children"),
    [Input("x1", "value"),Input("x2", "value"),Input("x3", "value"),Input("x4", "value"),Input("x5", "value")]
)

def make_all_table(entity_id, industry, province, enterprise_type, main_risk):
    if entity_id is None and industry is None and province is None and enterprise_type is None and main_risk is None:
        raise PreventUpdate
    else:
        df_list = entity_df[(entity_df['Entity ID'] == entity_id)|(entity_df['Industry'] == industry)|(entity_df['Province'] == province)|(entity_df['Enterprise Type'] == enterprise_type)|(entity_df['Main Risk'] == main_risk)]
        df_list = df_list[df_list['is_latest']==1][['Entity ID', 'Industry','Province','Enterprise Type','Main Risk']]
        df_list['Details'] = link
        return dbc.Table.from_dataframe(df_list)
