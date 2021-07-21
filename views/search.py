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

show_description = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Company Description", className="card-title"),
            html.P(
                "Huawei Technologies Co., Ltd. is a Chinese multinational technology company headquartered in Shenzhen, Guangdong. It designs, develops, and sells telecommunications equipment and consumer electronics. The company was founded in 1987 by Ren Zhengfei, a former Deputy Regimental Chief in the People's Liberation Army.",
                className="card-text",
            )
        ]
    ), style={'width': '800px', 'margin-left': '15px'}
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
            html.H5(["Other risks", dbc.Badge(
                "Low",  color="success", className="ml-1")]),
            dbc.Badge("✓ Verified data secured on distributed ledger", color='light')],
        style={'textAlign': 'right'}
    )
)

company_news_card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Recent News", className="card-title"),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Huawei’s P50 flagship will launch on July 29th", active=True,
                                            href="https://www.theverge.com/2021/7/19/22583225/huawei-p50-launch-july-29th-release-date")),
                    dbc.NavItem(dbc.NavLink("Huawei confirms July 29 launch for P50 series",
                                            href="https://www.gsmarena.com/huawei_confirms_july_29_date_for_p50_launch-news-50104.php")),
                    dbc.NavItem(dbc.NavLink("Ericsson warns of China retaliation following Sweden's ...",
                                            href="https://www.ft.com/content/2a596954-1206-4ce2-9dca-9c128d326768")),
                ],
                className="card-text",
            )
        ]
    ), style={'height':'340px','width': '300px', 'margin-left': '10px'}
)

show_social = dbc.Card(
    dbc.CardBody(
        [html.H4("Social", className="card-title"), 
        html.A([
            html.Img(
                src='/assets/twitter.jpeg',
                style={
                    'height': '35%',
                    'width': '35%',
                })
    ], href='https://twitter.com/search?q=huawei&src=typed_query'), 
    html.A([
            html.Img(
                src='/assets/weibologo.png',
                style={
                    'height': '25%',
                    'width': '25%',
                })
    ], href="https://s.weibo.com/weibo/%25E5%258D%258E%25E4%25B8%25BA?topnav=1&wvr=6&b=1"),
    html.A([
            html.Img(
                src='/assets/zhihulogo.png',
                style={
                    'height': '30%',
                    'width': '30%', 'margin-left':'20px'
                })
    ], href="https://www.zhihu.com/search?type=content&q=huawei")
    ],
        style={'textAlign': 'left'}
    ),style={'width':'300px','margin-left': '10px'}
)

view_forecast = html.Div(
    [
        dbc.Button(
            "Checkout our forecast figures for key metric", id="view_forecast", href='/payment',
            outline=False, color='secondary', className="mr-2",
            style={'textAlign': 'center', 'margin-left': '40%', 'width': '400px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                   'font-size': '16px'}
        )
    ]
)


table_header = [html.Br(),
    html.Thead(html.Tr([html.Th("Topline Metrics"), html.Th("")]))
]

row1 = html.Tr([html.Td("Total Assets ($ M)"), html.Td("86.9")])
row2 = html.Tr([html.Td("Total Liabilities ($ M)"), html.Td("21.3")])
row3 = html.Tr([html.Td("Total Equity ($ M)"), html.Td("65.6")])
row4 = html.Tr([html.Td("Debt to Equity (DE) Ratio"), html.Td("0.1")])
row5 = html.Tr([html.Td("Debt Ratio"), html.Td("0.1")])
row6 = html.Tr([html.Td("Return on Assets (ROA)"), html.Td("12%")])
row7 = html.Tr([html.Td("Return on Equity (ROE)"), html.Td("14%")])
row8 = html.Tr([html.Td("Net Income ($ M)"), html.Td("$8.10")])
row9 = html.Tr([html.Td("Profit Margin"), html.Td("3.2%")])
row10 = html.Tr([html.Td("Total Number Of Employees ('000)"), html.Td("31")])
row11 = html.Tr([html.Td("Registered capital ($ M)"), html.Td("300")])
row12 = html.Tr([html.Td("Paid Up Capital ($ M)"), html.Td("3")])


table_body = [html.Tbody(
    [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12])]


layout = dbc.Container(
    [html.H2("Company Details", style={'textAlign': 'right'}),
    html.Hr(style={'width': '1100px'}),
        html.Br(),
        dbc.Row([html.H4("Entity ID", style={'margin-left': '1%'}),
                dbc.Badge("722691858", pill=True, style={"fontSize": "20px", "margin-left": "6%"})]),
        html.P(),
        dbc.Row([html.H4("Company Name", style={'margin-left': '1%'}),
                dbc.Badge("Huawei", pill=True, style={"fontSize": "20px", "margin-left": "3%", 'margin-right': '3%'})]),
     html.P(),
     dbc.Row([show_description, risk_scores], justify='between'),
     dbc.Button(
        "View Risk Analysis", id="access-risk_analysis", href='/payment',
        outline=True, color='primary', className="mr-2",
        style={'textAlign': 'center', 'margin-left': '73%', 'width': '310px', 'margin-top': '10px',
               'font-size': '16px'}
    ),
        html.P(),
        dbc.Row([dbc.Table(table_header+table_body, bordered=True, size='md',style={'width': '800px'}),
        dbc.Col([company_news_card,html.P(),show_social])],justify='between'),
        # dbc.Col([dbc.Table(table_header+table_body, bordered=True, size='md')
        #                 ], align='left', style={'width': '800px'}),
        dbc.Button("View trends & forecasts", id="view_forecast", href='/payment',
                   outline=True, color='primary', className="mr-2",
                   style={'textAlign': 'center', 'width': '790px', 'margin-top': '10px', 'font-size': '16px'}),
        html.P(),
        html.P()
    ], style={'margin-left': '20%'}
)


# dbc.Row([html.P([html.Span("Last Updated Year:  ", id='tooltip-target',style={'textDecoration': 'underline', 'textAlign': 'left'}),
#                          dbc.Tooltip("Noun: rare, ", target="tooltip-target")]),
#                  html.P("2018",style={'textAlign':'right'})],justify='end'),
#         dbc.Row([html.P("Total Assets:  ", style={'textAlign': 'left'}),
#                  html.P("$ 83M", style={'margin-left': '23%'})]),
#         dbc.Row([html.P("Total Liabilities:  ", style={'textAlign': 'left'}),
#                  html.P("$ 10.6M", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Total Equity:  ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 73.1M", style={'margin-left': '22%'})]),
#         dbc.Row([html.P("Debt to Equity (DE) Ratio", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 0.1M", style={'margin-left': '15%'})]),
#         dbc.Row([html.P("Debt Ratio:  ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 0.1M", style={'margin-left': '24%'})]),
#         dbc.Row([html.P("Return on Assets (ROA):  ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 0.12M", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Return on Equity (ROE): ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 0.14M", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Net Income: ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 10.2M", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Profit Margin: ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("$ 0.05M", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Total Number Of Employees ('000): ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("37", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Registered capital: ", style={'textAlign': 'left'}),
#                  # html.Div(id="revenue-output")]),
#                  html.P("300", style={'margin-left': '20%'})]),
#         dbc.Row([html.P("Paid Up Capital: ", style={'textAlign': 'left'}),
#                  html.P("3", style={'margin-left': '20%'})]),
