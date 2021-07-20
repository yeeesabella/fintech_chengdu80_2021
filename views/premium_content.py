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
import networkx as nx
from colour import Color
from datetime import datetime
from textwrap import dedent as d
import json
import pathlib
from views import search
import plotly.express as px


BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()
entity_df = pd.read_csv(DATA_PATH.joinpath("full_search_list.csv"))
variables = ['Total Assets',
'Total Liabilities',
'Total Equity',
'Debt to Equity (DE) Ratio',	
'Debt Ratio',
'Return on Assets (ROA)',
'Return on Equity (ROE)',
'Net Income',
'Profit Margin',
'Total Number Of Employees']

timeseries_controls = dbc.Container(dbc.Row(
    [
        dbc.Label("Variable of interest", style={"margin-right": "20px","verticalAlign":'middle'}),
        dcc.Dropdown(
            id="variable-of-interest",
            options=[{"label": col, "value": col} for col in variables],
            value='Total Assets', style={"width": "20rem", "margin-right": "20px"}
        )]))

scatter_controls = dbc.Container(dbc.Row(
    [
        dbc.Label("X-axis", style={"margin-right": "20px","verticalAlign":'middle'}),
        dcc.Dropdown(
            id="x1",
            options=[{"label": col, "value": col} for col in variables],
            value='Total Assets', style={"width": "20rem", "margin-right": "20px"}
        ),
        dbc.Label("Y-axis", style={"margin-right": "20px","verticalAlign":'middle'}),
        dcc.Dropdown(
            id="x2",
            options=[{"label": col, "value": col} for col in variables],
            value='Total Liabilities', style={"width": "20rem", "margin-right": "20px"}
        ),
        ]))


card_tabs=dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Financial Overview", tab_id="tab-1"),
                    dbc.Tab(label="Risk Scores Insights", tab_id="tab-2"),
                    dbc.Tab(label="Risks Transmission", tab_id="tab-3"),
                    dbc.Tab(label="Comparison", tab_id="tab-4"),
                ],
                id="card-tabs",
                card=True,
                active_tab="tab-1",
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
    ], style={"margin-left": "100px", "width": '1200px'}
)


@ app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab == 'tab-1':
        return dbc.Container([
            html.H4("Overview of Trends & Forecasts"),
            timeseries_controls,
            dcc.Graph(id='time-series-plot-output',
                  style={'width': '1000px'}),
            html.H4("Relationship between Variables"),
            scatter_controls,
            dcc.Graph(id='scatter-plot-output',
                  style={'width': '1000px'})
        ])
    elif active_tab == 'tab-2':
        return dbc.Container([html.H4("Insights into FinNUS Risk Scores"),
                                html.P("The company is exposed to various external factors that have contributed to its operational, legal and macro risk. The primary factors that contribute to its xx risk are shown below. The explainability results are result of our proprietory algorithm which is based blockchain-protected data."),
                                html.H4(
                                    "Factors influencing the risk classification (placeholder images)"),
                                dbc.Row([html.Img(src='/assets/shap_plot.png', height="330px"),
                                        html.Img(
                                            src='/assets/shap_plot.png', height="330px"),
                                        html.Img(src='/assets/shap_plot.png', height="330px")])
                                ])
    elif active_tab == 'tab-3':
        return dbc.Container([
            html.H4("Risks Transmission"),
            html.Img(src='/assets/ownership-nike.png', height="330px"),
        ])
    elif active_tab == 'tab-4':
        return dbc.Container([
            html.H4("Comparison with Other Risk Providers"),
            html.Img(src='/assets/benchmark_type_2.png', height="500px")
        ])
    else:
        return "This is tab {}".format(active_tab)


@ app.callback(
    Output("time-series-plot-output", "figure"),
    Input("variable-of-interest", "value")
)
def plot_line_graph(variable_name):
    df_timeseries = entity_df[(entity_df['Entity ID'] == '2608434')]
    fig = px.bar(df_timeseries, x="Year", y=variable_name,color="is_predicted",title=f'Historical {variable_name}')
    return fig


@ app.callback(
    Output("scatter-plot-output", "figure"),
    [Input("x1", "value"),Input("x2", "value")]
    )

def plot_scatter_graph(variable_1,variable_2):
    df_timeseries = entity_df[(entity_df['Entity ID'] == '2608434')]
    fig = px.scatter(df_timeseries, x=variable_1, y=variable_2,title=f'Scatter Matrix between {variable_1} and {variable_2}')
    fig.update(layout_showlegend=False)
    return fig

layout=dbc.Container(
                        [html.H2("FinNUS+", style={"margin-left": "100px"}),
                        dbc.Badge("Entity ID: 2608434", style={
                                  "fontSize": "24px", "margin-left": "9%"}),
                        html.P(),
                        dbc.Badge("Company Name: Nike", style={
                                  "fontSize": "24px", "margin-left": "9%"}),
                        html.P(),
                        card_tabs
                        ], className="mt-4")
