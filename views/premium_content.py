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

# YEAR=[2010, 2019]
ACCOUNT="A0001"

BASE_PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = BASE_PATH.joinpath("data").resolve()

##############################################################################################################################################################
def network_graph(AccountToSearch):

    edge1 = pd.read_csv(DATA_PATH.joinpath("edge1.csv"))
    node1 = pd.read_csv(DATA_PATH.joinpath("node1.csv"))

    # filter the record by datetime, to enable interactive control through the input box
    # edge1['Datetime'] = "" # add empty Datetime column to edge1 dataframe
    accountSet=set() # contain unique account
    for index in range(0,len(edge1)):
        # edge1['Datetime'][index] = datetime.strptime(edge1['Date'][index], '%d/%m/%Y')
        # if edge1['Datetime'][index].year<yearRange[0] or edge1['Datetime'][index].year>yearRange[1]:
        #     edge1.drop(axis=0, index=index, inplace=True)
        #     continue
        accountSet.add(edge1['Source'][index])
        accountSet.add(edge1['Target'][index])

    # to define the centric point of the networkx layout
    shells=[]
    shell1=[]
    shell1.append(AccountToSearch)
    shells.append(shell1)
    shell2=[]
    for ele in accountSet:
        if ele!=AccountToSearch:
            shell2.append(ele)
    shells.append(shell2)


    G = nx.from_pandas_edgelist(edge1, 'Source', 'Target', ['Source', 'Target', 'TransactionAmt'], create_using=nx.MultiDiGraph())
    nx.set_node_attributes(G, node1.set_index('Account')['CustomerName'].to_dict(), 'CustomerName')
    nx.set_node_attributes(G, node1.set_index('Account')['Type'].to_dict(), 'Type')
    # pos = nx.layout.spring_layout(G)
    # pos = nx.layout.circular_layout(G)
    # nx.layout.shell_layout only works for more than 3 nodes
    if len(shell2)>1:
        pos = nx.drawing.layout.shell_layout(G, shells)
    else:
        pos = nx.drawing.layout.spring_layout(G)
    for node in G.nodes:
        G.nodes[node]['pos'] = list(pos[node])


    if len(shell2)==0:
        traceRecode = []  # contains edge_trace, node_trace, middle_node_trace

        node_trace = go.Scatter(x=tuple([1]), y=tuple([1]), text=tuple([str(AccountToSearch)]), textposition="bottom center",
                                mode='markers+text',
                                marker={'size': 50, 'color': 'LightSkyBlue'})
        traceRecode.append(node_trace)

        node_trace1 = go.Scatter(x=tuple([1]), y=tuple([1]),
                                mode='markers',
                                marker={'size': 50, 'color': 'LightSkyBlue'},
                                opacity=0)
        traceRecode.append(node_trace1)

        figure = {
            "data": traceRecode,
            "layout": go.Layout(title='Interactive Transaction Visualization', showlegend=False,
                                margin={'b': 40, 'l': 40, 'r': 40, 't': 40},
                                xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                height=600
                                )}
        return figure


    traceRecode = []  # contains edge_trace, node_trace, middle_node_trace
    ############################################################################################################################################################
    colors = list(Color('lightcoral').range_to(Color('darkred'), len(G.edges())))
    colors = ['rgb' + str(x.rgb) for x in colors]

    index = 0
    for edge in G.edges:
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        weight = float(G.edges[edge]['TransactionAmt']) / max(edge1['TransactionAmt']) * 10
        trace = go.Scatter(x=tuple([x0, x1, None]), y=tuple([y0, y1, None]),
                           mode='lines',
                           line={'width': weight},
                           marker=dict(color=colors[index]),
                           line_shape='spline',
                           opacity=1)
        traceRecode.append(trace)
        index = index + 1
    ###############################################################################################################################################################
    node_trace = go.Scatter(x=[], y=[], hovertext=[], text=[], mode='markers+text', textposition="bottom center",
                            hoverinfo="text", marker={'size': 50, 'color': 'LightSkyBlue'})

    index = 0
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        hovertext = "CustomerName: " + str(G.nodes[node]['CustomerName']) + "<br>" + "AccountType: " + str(
            G.nodes[node]['Type'])
        text = node1['Account'][index]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['hovertext'] += tuple([hovertext])
        node_trace['text'] += tuple([text])
        index = index + 1

    traceRecode.append(node_trace)
    ################################################################################################################################################################
    middle_hover_trace = go.Scatter(x=[], y=[], hovertext=[], mode='markers', hoverinfo="text",
                                    marker={'size': 20, 'color': 'LightSkyBlue'},
                                    opacity=0)

    index = 0
    for edge in G.edges:
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        hovertext = "From: " + str(G.edges[edge]['Source']) + "<br>" + "To: " + str(
            G.edges[edge]['Target']) + "<br>" + "TransactionAmt: " + str(
            G.edges[edge]['TransactionAmt'])
 
        middle_hover_trace['x'] += tuple([(x0 + x1) / 2])
        middle_hover_trace['y'] += tuple([(y0 + y1) / 2])
        middle_hover_trace['hovertext'] += tuple([hovertext])
        index = index + 1

    traceRecode.append(middle_hover_trace)
    #################################################################################################################################################################
    figure = {
        "data": traceRecode,
        "layout": go.Layout(title='Risk Transmission Network', showlegend=False, hovermode='closest',
                            margin={'b': 40, 'l': 40, 'r': 40, 't': 40},
                            xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                            yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                            height=600,
                            clickmode='event+select',
                            annotations=[
                                dict(
                                    ax=(G.nodes[edge[0]]['pos'][0] + G.nodes[edge[1]]['pos'][0]) / 2,
                                    ay=(G.nodes[edge[0]]['pos'][1] + G.nodes[edge[1]]['pos'][1]) / 2, axref='x', ayref='y',
                                    x=(G.nodes[edge[1]]['pos'][0] * 3 + G.nodes[edge[0]]['pos'][0]) / 4,
                                    y=(G.nodes[edge[1]]['pos'][1] * 3 + G.nodes[edge[0]]['pos'][1]) / 4, xref='x', yref='y',
                                    showarrow=True,
                                    arrowhead=3,
                                    arrowsize=4,
                                    arrowwidth=1,
                                    opacity=1
                                ) for edge in G.edges]
                            )}
    return figure



# styles: for right side hover/click component
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


graph_layout = dbc.Container([
    #########################Title
    html.Div([html.H2("Analyzing Risk Transmission")],
             className="row",
             style={'textAlign': "center", "margin-left":"100px"}),
            #  html.Div([html.H1("Transaction Network Graph")],
    #############################################################################################define the row
    html.Div(
        className="row",
        children=[
            ##############################################left side two input components
            html.Div(
                className="two columns",
                children=[

                    html.Div(
                        className="twelve columns",
                        children=[
                            dcc.Markdown(("""
                            **Account To Search**
                            (Input the account to visualize)
                            """)),
                            dcc.Input(id="input1", type="text", placeholder="Account"),
                            html.Div(id="output")
                        ],
                        style={'height': '100px', "margin-left":"120px"}
                    )
                ]
            ),

            ############################################middle graph component
            html.Div(
                className="eight columns",
                children=[dcc.Graph(id="my-graph",
                                    figure=network_graph(ACCOUNT))],
                                    style={'height': '300px', "margin-left":"200px"}
            ),
        ]
    )
])


layout = dbc.Container([html.H2(
                        "Risk Analysis", style={"margin-left":"100px"}
                    ),
                    html.P("The company is exposed to various external factors that have contributed to its operational, legal and macro risk. The primary factors that contribute to its xx risk are shown below. The explainability results are result of our proprietory algorithm which is based blockchain-protected data.", style={"margin-left":"100px"}),

                    html.H4(
                        "Factors influencing the risk classification", style={"margin-left":"350px"}
                    ),
                    html.Img(src='/assets/shap_plot.png', height="500px",style={"margin-left":"200px"}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                                html.Div(graph_layout,),
                                html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2(
                        "Benchmark Risk Scores", style={"margin-left":"100px"}
                    ),
                    html.Img(src='/assets/benchmark_type_2.png', height="500px",style={"margin-left":"300px"}),
], className="mt-4")


###################################callback for left side components
@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('input1', 'value')])
def update_output(input1):
    # YEAR = value
    ACCOUNT = input1
    return network_graph(input1)
    # to update the global variable of YEAR and ACCOUNT
################################callback for right side components
@app.callback(
    dash.dependencies.Output('hover-data', 'children'),
    [dash.dependencies.Input('my-graph', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    dash.dependencies.Output('click-data', 'children'),
    [dash.dependencies.Input('my-graph', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)