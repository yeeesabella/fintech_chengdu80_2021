import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

from app import app

table_header = [html.Br(),
    html.Thead(html.Tr([html.Th("Smart Contract Field"), html.Th("Content")]))
]

row1 = html.Tr([html.Td("Hash (SHA256)"), html.Td("FC78B890F9 1DD8E92C40 2A45FA57E8 9DF7E2677011 78542DCC570 B90FFA0FBE5")])
row2 = html.Tr([html.Td("Smart Contract Date"), html.Td("20-July-2021")])
row3 = html.Tr([html.Td("Contract Details"), html.Td("The payment to be made on authentication of data")])
row4 = html.Tr([html.Td("Company for which data is provided"), html.Td("Chengdu Inc.")])
row5 = html.Tr([html.Td("Data Provider"), html.Td("DataCat Inc.")])
row6 = html.Tr([html.Td("Contract Cost"), html.Td("ETH 2000")])


table_body = [html.Tbody([row1, row2, row3, row4, row5, row6])]

export_contract = html.Div(
            [
                dbc.Button(
                    "Deploy to Ethereum", id="sync-ethereum",color="primary", className="mr-2", n_clicks=0
                ),
                html.Span(id="sync-output",
                          style={"verticalAlign": "middle"})
            ],style={'textAlign': 'left','margin-left':'20%'}
        )


# df = pd.DataFrame(
#     [
#         ["Hash (SHA256)", 'FC78B890F9 1DD8E92C40 2A45FA57E8 9DF7E2677011 78542DCC570 B90FFA0FBE5'],
#         ["Smart Contract Date", '20-July-2021'],
#         ["Contract Details", 'The payment to be made on authentication of data'],
#         ["Company for which data is provided", 'Chengdu Inc.'],
#         ["Data Provider", 'Data Inc.'],
#         ["Contract Cost", 'ETH 2000']
#     ],
#     columns=["Smart Contract Field", "Content"],
# )


layout = html.Div([html.P(),
    dbc.Table(table_header+table_body, bordered=True,size='md',
                        style={'margin-left':'20%','margin-top':'20px','width':'800px'}),
                export_contract,
                html.P(),
                dbc.Button("View your business risk scores", id="view_risk_scores", href='/myriskscore',
                   outline=True, color='primary', className="mr-2",
                   style={'textAlign': 'center', 'width': '800px', 'margin-left':'20%','margin-top': '10px', 'font-size': '16px'}),
                ]
                )

# @app.callback(
#     Output("export-button", "data"),
#     [Input("export-csv", "n_clicks")],
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     if n_clicks > 0:
#         return dcc.send_data_frame(df.to_csv, "smart-contract.csv")


@app.callback(
    Output("sync-output", "children"), [
        Input("sync-ethereum", "n_clicks")]
)
def on_button_click(n):
    if n==0:
        return " "
    else:
        return f"✓ Deployed!"