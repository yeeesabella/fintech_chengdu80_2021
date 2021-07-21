# index page
import dash_bootstrap_components
from dash_bootstrap_components._components.Navbar import Navbar
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.dependencies import ClientsideFunction
import dash

from app import app, server
from flask_login import logout_user, current_user
from views import login, error, search, blockchain, profile, user_admin, aboutus, pricing, alerts, contribute_data, signup, premium_content, payment,fullsearch,myriskscore

###############################################################################
########### LANDING PAGE LAYOUT ###########
###############################################################################

sideBar = dbc.Nav(id='sideBar',
                 children=[],
                #  style=SIDEBAR_STYLE,
                 pills=True
                 )

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(src='/assets/finnus_logo_horizontal_transparent.png', height="50px",style={"margin-left":"50px"})),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
        dbc.NavLink("About Us", href="/aboutus", active="exact",style={"color":"#162e44"}),
        dbc.NavLink("Pricing", href="/pricing", active="exact",style={"color":"#162e44"}),
    ],
    # color="secondary",
    dark=True, className = 'row sticky-top', style={'background-color': '#C6D9F1',"sticky":"fixed"}
)

content = html.Div(id="pageContent")



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([sideBar,navbar,content
    ])
], id='table-wrapper')

# ################################################################################
# # HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
# ################################################################################
@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/':
        if current_user.is_authenticated:
            if current_user.admin == 2: # individual
                return fullsearch.layout
            if current_user.admin == 1: # corporate
                return fullsearch.layout    
            elif current_user.admin == 0: # real admin
                return user_admin.layout
        else:
            return login.layout

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return login.layout
        else:
            return login.layout

    if pathname == '/search':
        return search.layout

    if pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout

    if pathname == '/admin':
        if current_user.is_authenticated:
            if current_user.admin == 1:
                return user_admin.layout
            else:
                return error.layout
        else:
            return login.layout

    if pathname == '/aboutus':
        return aboutus.layout

    if pathname == '/pricing':
        return pricing.layout

    if pathname == '/alerts':
        return alerts.layout

    if pathname == '/signup':
        return signup.layout

    if pathname == '/data_provider':
        return data_provider.layout

    if pathname == '/contribute_data':
        return contribute_data.layout

    if pathname == '/premium_content':
        return premium_content.layout
    
    if pathname == '/payment':
        return payment.layout

    if pathname == '/blockchain':
        if current_user.is_authenticated:
            return blockchain.layout
        else:
            return login.layout

    if pathname == '/fullsearch':
        return fullsearch.layout

    if pathname == '/login':
        return login.layout

    if pathname == '/myriskscore':
        return myriskscore.layout
    else:
        return error.layout

# ################################################################################
# # ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
# 0 = data provider, 1 = admin, 2 = normal user
# ################################################################################
@app.callback(
    Output('sideBar', 'children'),
    [Input('pageContent', 'children')])
def sideBar(input1):
    if current_user.is_authenticated:
        if current_user.admin == 0: # real admin
            SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 70,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    'background-color':'#DCE6F2'
}
            navBarContents = html.Div(
                [   
                    html.P(
                        "Welcome back, Admin! 👋🏽", className="lead", style={'textAlign': 'center'}
                    ),
                    dbc.Nav(
                        [
                            dbc.NavLink("My Alerts", href="/alerts", active="exact"),
                            dbc.NavLink("Entity Search", href="/fullsearch",
                                        active="exact"),
                            dbc.NavLink("🔓 FinNUS+", href="/premium_content",
                                        active="exact"),
                            dbc.NavLink("Assess my business", href="/contribute_data", active="exact"),
                            dbc.DropdownMenu(
                                nav=True,
                                in_navbar=True,
                                label=current_user.username,
                                children=[
                                    dbc.DropdownMenuItem(
                                        'Profile', href='/profile'),
                                    dbc.DropdownMenuItem(
                                        'Admin', href='/admin'),
                                    dbc.DropdownMenuItem(divider=True),
                                    dbc.DropdownMenuItem(
                                        'Logout', href='/logout'),
                                ],
                            )
                        ],
                        vertical=True,
                        pills=True
                    ),
                ],
                style=SIDEBAR_STYLE,
            )
            return navBarContents

        elif current_user.admin == 1: # corporate
            SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 70,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    'background-color':'#DCE6F2'
}
            navBarContents = html.Div(
                [   
                    html.P(
                        "Welcome back! 👋🏽", className="lead", style={'textAlign': 'center'}
                    ),
                    dbc.Nav(
                        [
                            dbc.NavLink("My Alerts", href="/alerts", active="exact"),
                            dbc.NavLink("Entity Search", href="/fullsearch",active="exact"),
                            dbc.NavLink("🔓 FinNUS+", href="/premium_content",active="exact"),
                            dbc.NavLink("Assess my business", href="/contribute_data", active="exact"),
                            dbc.DropdownMenu(
                                nav=True,
                                in_navbar=True,
                                label=current_user.username,
                                children=[
                                    dbc.DropdownMenuItem(
                                        'Profile', href='/profile'),
                                    dbc.DropdownMenuItem(divider=True),
                                    dbc.DropdownMenuItem(
                                        'Logout', href='/logout'),
                                ],
                            )
                        ],
                        vertical=True,
                        pills=True
                    ),
                ],
                style=SIDEBAR_STYLE,
            )
            return navBarContents

        elif current_user.admin == 2: # individual
            SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 70,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    'background-color':'#DCE6F2'
}
            
            navBarContents = html.Div(
                [   
                    html.P(
                        "Welcome back! 👋🏽", className="lead", style={'textAlign': 'center'}
                    ),
                    dbc.Nav(
                        [
                            dbc.NavLink("My Alerts", href="/alerts", active="exact"),
                            dbc.NavLink("Entity Search", href="/fullsearch",
                                        active="exact"),
                            dbc.NavLink("🔓 FinNUS+", href="/premium_content",
                                        active="exact"),
                            dbc.DropdownMenu(
                                nav=True,
                                in_navbar=True,
                                label=current_user.username,
                                children=[
                                    dbc.DropdownMenuItem(
                                        'Profile', href='/profile'),
                                    dbc.DropdownMenuItem(divider=True),
                                    dbc.DropdownMenuItem(
                                        'Logout', href='/logout'),
                                ],
                            )
                        ],
                        vertical=True,
                        pills=True
                    ),
                ],
                style=SIDEBAR_STYLE,
            )
            return navBarContents
        else:
            return ''

    else:
        return ''

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port='8888')
