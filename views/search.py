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
entity_df = pd.read_csv(DATA_PATH.joinpath("tax_year.csv"))
watchlist_df = pd.read_csv(DATA_PATH.joinpath("my_watchlist.csv"))


controls = dbc.Container(dbc.Row(
    [
        dbc.Label("Entity ID", style={"margin-right": "20px"}),
        dcc.Dropdown(
            id="x-variable",
            options=[
                {"label": col, "value": col} for col in entity_df['entid'].unique()
            ],
            value="Company ID", style={"width": "20rem", "margin-right": "20px"}
        ),
        html.Div(
            [
                dbc.Button(
                    "✚ Add to watch list", id="add-to-watchlist-button",
                    outline=True, className="mr-2", n_clicks=0, style={"margin-right": "15px"}
                ),
                html.Span(id="example-output",
                          style={"verticalAlign": "middle"})
            ]
        )
    ],
    align="left"
))

show_entity = dbc.Row([html.H4("Entity ID",style={'margin-right':'30px'}),
                       html.H4(id="entity-output")])

show_description = html.Div(dbc.Row([dbc.Row([dbc.Col([html.H4("Brief Description"),
                                            html.P("Didi Chuxing is a mobile transportation company headquartered in Beijing. Known simply as Didi, it is now one of the world's largest ride-hailing companies, serving more than 550 million users across Asia, Australia, and Latin America. Didi was founded in 2012.")]),
                                      html.Img(
                                          src='/assets/socialmedia_mockup.png', style={'width': '15%'})
                                      ])],justify="end"))

all_risks = dbc.Col(
    [
        html.H5(["Legal risks", dbc.Badge(
            "High", color="danger", className="ml-1")]),
        html.H5(["Operation risks", dbc.Badge(
            "Medium",  color="warning", className="ml-1")]),
        html.H5(["Loan risks", dbc.Badge(
            "Low",  color="success", className="ml-1")]),
        html.H5(["Other risks", dbc.Badge("Low",  color="success", className="ml-1")])],
    width=12,style={'textAlign':'right','height':'200px'}
)

key_metrics = dbc.CardGroup(
    [
        dbc.Col([dbc.Card(
            dbc.CardBody([
                html.H4("Total Revenue", className="card-title"),
                html.Div(id="revenue-output",
                         style={'textAlign': 'center'})
            ])
        ),html.P(),dbc.Card(
            dbc.CardBody([
                html.H4("Total blabla", className="card-title"),
                html.Div(id="revenue-output",
                         style={'textAlign': 'center'})
            ])
        )], width=3),dbc.Col([dbc.Card(
            dbc.CardBody([
                html.H4("Total Revenue", className="card-title"),
                html.Div(id="revenue-output",
                         style={'textAlign': 'center'})
            ])
        ),html.P(),dbc.Card(
            dbc.CardBody([
                html.H4("Total Revenue", className="card-title"),
                html.Div(id="revenue-output",
                         style={'textAlign': 'center'})
            ])
        )], width=3),dbc.Col([dbc.Card(
            dbc.CardBody([
                html.H4("Total Assets", className="card-title"),
                html.Div(id="assets-output",
                         style={'textAlign': 'center'})
            ])
        ),html.P(),dbc.Card(
            dbc.CardBody([
                html.H4("Total Profit/Loss", className="card-title"),
                html.Div(id="profitloss-output",
                         style={'textAlign': 'center'})
            ])
        )], width=3),
        dbc.Col(dbc.Card(all_risks),style={'height':'100%'})
    ],
)

download_historical = html.Div([
            dbc.Button("Download Historical CSV", id="btn_csv", className="mr-2",
                       color='primary', n_clicks=0),
            dcc.Download(id="download-dataframe-csv")], style={'textAlign': 'left'})

table = html.Div(id='table-stats', style={'textAlign': 'left', 'margin-left': '20%', 'width': '50px'})
access_premium = html.Div(
            [
                dbc.Button(
                    "🔐 Access premium content", id="access-premium-button",href='/premium_content',
                    outline=False, color='secondary',className="mr-2",
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '400px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'}
                )
            ]
        )

layout = dbc.Container(
    [
        html.H1("Entity Search", style={"textAlign": "right"}),
        html.Hr(style={
        }),
        dbc.Col(controls,
                align="left",
                # justify="center",
                style={'margin-left': '10%'}
                ),
        html.P(),
        show_entity, show_description,
        key_metrics,
        html.P(),
        dbc.Row([html.H4("Data last updated on ",style={'margin-right':'30px'}),
                       html.H4(id="year-output")]),
        download_historical,
        html.P(),
        table,
        dcc.Graph(id='line-plot-output',
                  style={'width': '1000px'}),
                  access_premium,
                  
        html.P()
    ],style={'margin-left':'20%'}
)


@ app.callback(
    [Output("entity-output", "children"),
     Output("revenue-output", "children"),
     Output("year-output", "children"),
     Output("assets-output", "children"),
     Output("profitloss-output", "children")],
    Input("x-variable", "value")
)
def make_table(entity_id):
    df = entity_df[(entity_df['entid'] == entity_id)
                   & (entity_df['islatest'] == 1)]
    df = round(df,2)
    return [df['entid'], df['revenue'], df['year'], df['assets'],df['profit_loss']]


@ app.callback(
    Output("line-plot-output", "figure"),
    Input("x-variable", "value")
)
def plot_line_graph(entity_id):
    df_timeseries = entity_df[(entity_df['entid'] == entity_id)]
    fig = px.line(df_timeseries, x="year", y="revenue", title='Revenue')
    return fig


@app.callback(
    Output("example-output", "children"), [
        Input("add-to-watchlist-button", "n_clicks"), Input("x-variable", "value")]
)
def on_button_click(n, entity_id):
    if n is None:
        return "Not clicked."
    else:
        add_to_watch_list = entity_df[(entity_df['entid'] == entity_id) & (
            entity_df['islatest'] == 1)][['entid', 'profit_loss', 'revenue']]
        watchlist_df.append(add_to_watch_list).to_csv(
            DATA_PATH.joinpath("my_watchlist.csv"), index=False)
        return f"✓ Added {n} entity to watch list."


@app.callback(
    Output("download-dataframe-csv", "data"),
    [Input("btn_csv", "n_clicks"), Input("x-variable", "value")],
    prevent_initial_call=True,
)
def func(n_clicks, entity_id):
    if n_clicks > 0:
        df_timeseries = entity_df[(entity_df['entid'] == entity_id)]
        return dcc.send_data_frame(df_timeseries.to_csv, str(entity_id)+".csv")

@ app.callback(
    Output("table-stats", "children"),
    Input("x-variable", "value")
)
def make_all_table(entity_id):
    if entity_id is None:
        raise PreventUpdate
    else:
        df_timeseries = entity_df[(entity_df['entid'] == entity_id)]
        df_show = pd.pivot_table(columns='year',values=['revenue','assets'],data=df_timeseries).reset_index().rename(columns={'index':'Metrics'})
        return dbc.Table.from_dataframe(round(df_show,2))