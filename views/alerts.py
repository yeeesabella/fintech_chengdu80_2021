# watch list page
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
import pathlib

BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()

company_news = dbc.FormGroup(
    [
        dbc.Label("Company related news"),
        dbc.RadioItems(
            options=[
                {"label": "All", "value": 1},
                {"label": "Negative news only", "value": 2},
            ],
            value=1,
            id="company-news-input",
        ),
    ]
)

country_news = dbc.FormGroup(
    [
        dbc.Label("Country news"),
        dbc.RadioItems(
            options=[
                {"label": "All", "value": 1},
                {"label": "Negative news only", "value": 2},
            ],
            value=1,
            id="country-news-input",
        ),
    ]
)
social_media = dbc.FormGroup(
    [
        dbc.Label("Social media news"),
        dbc.RadioItems(
            options=[
                {"label": "All", "value": 1},
                {"label": "Negative sentiments only", "value": 2},
            ],
            value=1,
            id="social-media-input",
        ),
    ]
)

financial_strength = html.Div([html.Br(),
                               dbc.Row([dbc.Col(dbc.Label("Financial Strength"),style={'textAlign':'left'}), 
                                        dbc.Col(dbc.Label("Notify me when...."),style={'textAlign':'right'}), 
                                        dbc.Col(dbc.Label("Threshold %"),style={'textAlign':'right','right':'120px'})],style={'width':'3'}),
                               dbc.Row(
    [dbc.Col(dbc.Checklist(
        options=[
            {"label": "Risk scores from other providers", "value": 1},
        ],
        value=[1],
        id="financial-strength-input",
    ), style={'textAlign': 'left'}),
        dbc.Col(dcc.Dropdown(
            options=[{"label": "<", "value": 1},
                     {"label": ">", "value": 2},
                {"label": "Any increase", "value": 3},
                {"label": "Any decrease", "value": 4}
            ], value=[]
        ), width=3
    ),
        dbc.Col(html.Div(
            [
                dbc.Input(type="number", min=0, max=100, step=1),
            ],
            id="styled-numeric-input",
        ),
        width=3,
    )
    ],
    style={'textAlign': 'center', 'width': '3', 'margin-right': '10px'}
)])


finnus_factors = html.Div([html.Br(),
                               dbc.Row([dbc.Col(dbc.Label("FinNUS Factors"),style={'textAlign':'left'}), 
                                        dbc.Col(dbc.Label("Notify me when...."),style={'textAlign':'right'}), 
                                        dbc.Col(dbc.Label("Threshold %"),style={'textAlign':'right','right':'120px'})],style={'width':'3'}),
                               dbc.Row(
    [dbc.Col(dbc.Checklist(
        options=[
            {"label": "FinNUS Risk Score", "value": 1},
            {"label": "FinNUS Metrics - Top 5 Importance", "value": 2},
        ],
        value=[1, 2],
        id="finnus-factors-input",
    ), style={'textAlign': 'left'}),
        dbc.Col(dcc.Dropdown(
            options=[{"label": "<", "value": 1},
                     {"label": ">", "value": 2},
                {"label": "Any increase", "value": 3},
                {"label": "Any decrease", "value": 4}
            ], value=[]
        ), width=3
    ),
        dbc.Col(html.Div(
            [
                dbc.Input(type="number", min=0, max=100, step=1),
            ],
            id="styled-numeric-input",
        ),
        width=3,
    )
    ],
    style={'textAlign': 'center', 'width': '3', 'margin-right': '10px'}
)])



alert_button = html.Div(
    [
        dbc.Button(
            "Set alert", id="set-alert-button", color='primary',
            outline=True, className="mr-2", n_clicks=0, style={"margin-right": "15px"}
        ),
        html.Span(id="alert-output")
    ]
)


@ app.callback(
    Output("alert-output", "value"), [Input("set-alert-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"✓ Alert set!"


inputs = html.Div(
    [
        dbc.Form([finnus_factors, financial_strength,html.Br(),
                 social_media, company_news, country_news]),
        html.P(),
        alert_button
    ]
)


def make_item(entity_id,risk_level,colour):
    # one_entity = watchlist_df[watchlist_df['Entity']==entity_id]
    # one_entity = one_entity.transpose().reset_index().rename(columns={'index':'Key Metrics'}).iloc[1:]
    # new_header = one_entity.iloc[0]
    # one_entity = one_entity[1:]
    # one_entity.columns = new_header
    # one_entity = one_entity[one_entity['Year']!='entid']
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    [
                    
                    dbc.Button(
                        f"Entity ID #{entity_id}",
                        color="link",style={'fontSize':'20px','margin-top':'0%'},
                        id=f"group-{entity_id}-toggle",
                        n_clicks=0,
                    ),dbc.Row([html.P("Overall Risk Level",style={'margin-left':'25px','font-size':'15px','margin-right':'10px'}),
                    dbc.Badge(risk_level, color=colour,pill=False,style={'height':'20px','font-size':'15px'})]),
                    ]
                )
            ),
            dbc.Collapse(
                dbc.CardBody(inputs
                             #         dbc.Table.from_dataframe(one_entity[:-2], striped=True, bordered=True, hover=True,style={
                             # 'textAlign': 'center', 'margin-left': '0%', 'width': '100%'})
                             ),
                id=f"collapse-{entity_id}",
                is_open=False,
            ),
        ], style={'margin-left': '10%', 'width': '80%'}
    )


accordion = html.Div(
    [make_item(722691858,'High','danger'), make_item(36393553,'Low','success'), make_item(43814551,'Medium','warning')], className="accordion"
)


@ app.callback(
    [Output(f"collapse-{entity_id}", "is_open")
     for entity_id in [722691858, 36393553, 43814551]],
    [Input(f"group-{entity_id}-toggle", "n_clicks")
     for entity_id in [722691858, 36393553, 43814551]],
    [State(f"collapse-{entity_id}", "is_open")
     for entity_id in [722691858, 36393553, 43814551]],
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-722691858-toggle" and n1:
        return not is_open1, False, False
    elif button_id == "group-36393553-toggle" and n2:
        return False, not is_open2, False
    elif button_id == "group-43814551-toggle" and n3:
        return False, False, not is_open3
    return False, False, False


###############################################################################
########### Features ###########
###############################################################################
layout = dbc.Container([html.H1(
    "My Alerts", style={'textAlign': 'right'}
),
    html.Hr(), accordion
], style={'margin-left': '20%'})
