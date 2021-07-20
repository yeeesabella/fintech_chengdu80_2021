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
entity_df = pd.read_csv(DATA_PATH.joinpath("search_result.csv"))
watchlist_df = pd.read_csv(DATA_PATH.joinpath("my_watchlist.csv"))
df_metrics = pd.read_csv(DATA_PATH.joinpath("key_metrics.csv"))


view_risk_analysis = html.Div(
            [
                dbc.Button(
                    "View Risk Analysis", id="access-risk_analysis",href='/premium_content',
                    outline=False, color='secondary',className="mr-2",
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '200px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'}
                )
            ], style={'margin-right': '20'}
        )

risk_scores = dbc.Card(
    dbc.CardBody(
        [
        html.H5(["Legal risks", dbc.Badge(
            "High", color="danger", className="ml-1")]),
        html.H5(["Operation risks", dbc.Badge(
            "Medium",  color="warning", className="ml-1")]),
        html.H5(["Loan risks", dbc.Badge(
            "Low",  color="success", className="ml-1")]),
        html.H5(["Other risks", dbc.Badge("Low",  color="success", className="ml-1")]),
        html.H5(view_risk_analysis)],
        style={'textAlign':'right','height':'150px', 'width':'250px'}
    )
)


show_description = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Nike: Company Description", className="card-title"),
            html.P(
                "Micron Technology, Inc., through its subsidiaries, manufactures and markets dynamic random access memory chips (DRAMs), static random access memory chips (SRAMs), flash memory, semiconductor components, and memory modules.",
                className="card-text",
            )
            ,
        ]
    ),
    style={"width": "40rem"},
)

social_media_card = dbc.Card(
    dbc.CardBody(
        [
                    html.Img(
                        src='/assets/socialmedia_mockup.png',
                        className="logo"
                        , style={'height':'30%', 'width':'30%'}
                    ),
        ],
        style={"width": "20"}
    ))

company_news_card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Recent News", className="card-title"),
            # html.H4(dbc.NavLink("Is Nike really facing a sneaker shortage?.", active=True, href="https://qz.com/2035396/is-nike-really-facing-a-sneaker-shortage/"))
            # ,
            # html.P(
            #     "Nike could run out of sneakers made in Vietnam as Covid crisis worsens, S&P Global warns.",
            #     className="card-text", href='https://www.cnbc.com/2021/07/19/nike-could-run-out-of-shoes-from-vietnam-as-covid-worsens-sp-global.html'
            # ),
            # dbc.NavLink("Nike could run out of sneakers made in Vietnam as Covid crisis worsens, S&P Global warns.", active=True, href="https://www.cnbc.com/2021/07/19/nike-could-run-out-of-shoes-from-vietnam-as-covid-worsens-sp-global.html")
            # ,
            # dbc.NavLink("Nike's 'Star Wars' Sneakers Look Fantastic.", active=True, href="https://kotaku.com/nikes-star-wars-sneakers-look-fantastic-1847316695")
            # ,
            # # html.P(
            # #     "Nike's 'Star Wars' Sneakers Look Fantastic.",
            # #     className="card-text", href='https://kotaku.com/nikes-star-wars-sneakers-look-fantastic-1847316695'
            # # )
            # ,

            dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Is Nike really facing a sneaker shortage?", active=True, href="https://qz.com/2035396/is-nike-really-facing-a-sneaker-shortage/")),
        dbc.NavItem(dbc.NavLink("Nike could run out of sneakers made in Vietnam as Covid crisis worsens, S&P Global warns.", href="https://www.cnbc.com/2021/07/19/nike-could-run-out-of-shoes-from-vietnam-as-covid-worsens-sp-global.html")),
        dbc.NavItem(dbc.NavLink("Nike's 'Star Wars' Sneakers Look Fantastic.", href="https://kotaku.com/nikes-star-wars-sneakers-look-fantastic-1847316695")),
    ],
    vertical="md",
)
        ]
    ),
    style={"width": "40rem"},
)


sentiment_data = dbc.Row(children=
    [
        dbc.Col(company_news_card, width=4,style={'margin-left': '100'}),
        dbc.Col(social_media_card, width=4, style={'margin-left': '400'}),
        # dbc.Col(social_media_card),
    ]
)


size_grid_cards = dbc.Row(children=
    [
        dbc.Col(show_description, width=4,style={'margin-left': '100'}),
        dbc.Col(risk_scores, width=4, style={'margin-right': '100'}),
        # dbc.Col(social_media_card),
    ]
)


view_forecast = html.Div(
            [
                dbc.Button(
                    "Checkout our forecast figures for key metric", id="view_forecast",href='/premium_content',
                    outline=False, color='secondary',className="mr-2",
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '400px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'}
                )
            ]
        )


table_header = [html.Br(),
    html.Thead(html.Tr([html.Th("Metric"), html.Th("Value")]))
]

row1 = html.Tr([html.Td("Total Assets"), html.Td("$86.90")])
row2 = html.Tr([html.Td("Total Liabilites"), html.Td("$21.30")])
row3 = html.Tr([html.Td("Total Equity"), html.Td("$65.60")])
row4 = html.Tr([html.Td("Debt to Equity (DE) Ratio"), html.Td("0.1")])
row5 = html.Tr([html.Td("Debt Ratio"), html.Td("0.1")])
row6 = html.Tr([html.Td("Return on Assets (ROA)"), html.Td("12%")])
row7 = html.Tr([html.Td("Return on Equity (ROE)"), html.Td("14%")])
row8 = html.Tr([html.Td("Net Income"), html.Td("$8.10")])
row9 = html.Tr([html.Td("Profit Margin"), html.Td("3.2%")])
row10 = html.Tr([html.Td("Total Number Of Employees"), html.Td("$31.00")])
row11 = html.Tr([html.Td("Registered capital"), html.Td("300")])
row12 = html.Tr([html.Td("Paid Up Capital"), html.Td("3")])


table_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12])]



layout = dbc.Container(
    [
        dbc.Col([size_grid_cards],
                        align="left",

                style={'margin-left': '1'}
        ),

        # dbc.Col([view_risk_analysis]),
        html.P(),

        html.P(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Col([dbc.Table(table_header+table_body, bordered=True,size='md',
                        # style={'margin-left':'20%','margin-top':'20px'}
                        )
                        ], align='left', style={'margin-left': '1'}),
        view_forecast,          
        html.P(),
        sentiment_data
    ],style={'margin-left':'20%'}
)