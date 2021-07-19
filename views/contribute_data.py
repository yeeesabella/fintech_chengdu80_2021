from app import app, User
import numpy
import pandas as pd

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State
import pathlib
import base64
import datetime
import io
import dash_table


layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            "display": "block",
            "margin-left": "auto",
            "margin-right": "auto"
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-datatable'),
                   dbc.Button(children=['Upload'],
                    type='submit',
                    color='secondary',
                    href='/blockchain',
                    style={'textAlign': 'center', 
                    'margin-left': '70%', 
                    'margin-top': '10px','right': '20px',
                           'font-size': '16px'
                           }
                )
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([


        # dash_table.DataTable(
        #     data=df.to_dict('records'),
        #     columns=[{'name': i, 'id': i} for i in df.columns],
        #     page_size=15
        # ),
        # dcc.Store(id='stored-data', data=df.to_dict('records')),
        # html.Button(
        #             children='Login',
        #             n_clicks=0,
        #             type='submit',
        #             className='btn btn-primary btn-lg',
        #             style={'textAlign': 'center', 'margin-left': '40%', 'width': '200px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
        #                    'font-size': '16px'
        #                    }),

        html.Hr(),  # horizontal line
    ])


# @app.callback(Output('output-datatable', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children
