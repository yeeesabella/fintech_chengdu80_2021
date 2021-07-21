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
# import dash_cytoscape as cyto


BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()
entity_df = pd.read_csv(DATA_PATH.joinpath("huawei_data.csv"))

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
entity_df['Entity ID'] = entity_df['Entity ID'].astype(int).astype(str)


timeseries_controls = dbc.Container(dbc.Row(
    [
        dbc.Label("Variable of interest", style={"margin-right": "20px","verticalAlign":'middle'}),
        dcc.Dropdown(
            id="variable-of-interest",
            options=[{"label": col, "value": col} for col in variables],
            value='Total Assets', style={"width": "20rem", "margin-right": "20px"}
        )]))

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
            html.H4("Revenue - by Business Unit"),
            html.Img(src='/assets/biz prop.png', height="300px"),
            html.Br(),
            html.Br(),
            dbc.Row([dbc.Col([html.H4("Revenue - by Geography"),
            html.Img(src='/assets/region prop.png', height="300px")]),
            dbc.Col([html.H4("Risk Scores - by Geography"),
            html.Img(src='/assets/risk-rating.png', height="300px")])]),
        ])
    elif active_tab == 'tab-2':
        return dbc.Container([html.H3("Insights into FinNUS Risk Scores"),
                                html.P("The company is exposed to various external factors that have contributed to its operational, legal and macro risk. The primary factors that contribute to its loan risk are shown below. The explainability results are result of our proprietory algorithm which is based blockchain-protected data."),
                                html.H3(
                                    "Factors influencing the risk classification"),
                                html.P(),
                                html.H4("Local SHAP Plot"),
                                html.P("The output value (f(x)) is the classification class for the observation."),
                                html.P("Red/blue: Features that push the prediction higher (to the right) are shown in red, and those pushing the prediction lower are in blue."),
                                dbc.Badge("FinNUS Insights",style={'fontSize':'16px'}),
                                html.P("From the above SHAP plots, the company’s high credit risk is primarily due to operating cost and tax policies."),
                                html.Img(src='/assets/SHAP.png', height="500px"),
                                html.P(),
                                html.H4("LIME Plot"),
                                html.P("The LIME plots show the different factors affecting the credit and operational risk of the company."),
                                dbc.Badge("FinNUS Insights",style={'fontSize':'16px'}),
                                html.P("The company has high probability for credit risk due to non-compliance with tax policies."),
                                html.Img(src='/assets/LIME.png', height="330px"),
                                html.P(),
                                ])
    elif active_tab == 'tab-3':
        return dbc.Container([
            html.H4("Ownership Structure"),
            html.Img(src='/assets/ownership_huawei.png', height="330px"),
            html.P(),
            html.H4("Risks Network"),
            html.Img(src='/assets/huawei_network.png', height="500px"),
        ])
    elif active_tab == 'tab-4':
        return dbc.Container([
            html.H4("Comparison with Other Risk Providers"),
            html.Img(src='/assets/benchmark_type_1.png', height="500px")
        ])
    else:
        return "This is tab {}".format(active_tab)

@ app.callback(
    Output("time-series-plot-output", "figure"),
    Input("variable-of-interest", "value")
)
def plot_line_graph(variable_name):
    df_timeseries = entity_df[(entity_df['Entity ID'] == '722691858')]
    fig = px.bar(df_timeseries, x="Year", y=variable_name,color="is_predicted",title=f'Historical {variable_name}')
    return fig


layout=dbc.Container(
                        [html.H2("FinNUS+", style={"margin-left": "100%"}),
                        html.Hr(style={'width':'1200px','margin-left':'10%'}),
                        dbc.Row([html.H4("Entity ID",style={'margin-left':'10%'}),
                                dbc.Badge("722691858", pill=True,style={"fontSize": "20px", "margin-left": "6%"})]),
                                html.P(),
                        dbc.Row([html.H4("Company Name",style={'margin-left':'10%'}),
                                dbc.Badge("Huawei", pill=True,style={"fontSize": "20px", "margin-left": "3%",'margin-right':'3%'}), 
        html.Div(
            [
                dbc.Button(
                    "✚ Add to alerts", id="add-to-watchlist-button",
                    outline=True,color="primary", className="mr-2", n_clicks=0, style={"margin-right": "15px"}
                ),
                html.Span(id="example-output",
                          style={"verticalAlign": "middle"})
            ]
        )]),
                        html.P(),
                        card_tabs
                        ], className="mt-4")


@app.callback(
    Output("example-output", "children"), [
        Input("add-to-watchlist-button", "n_clicks")]
)
def on_button_click(n):
    if n==0:
        return " "
    else:
        return f"✓ Added to alerts!"