import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app
from flask_login import current_user
from users_mgt import update_password
from werkzeug.security import check_password_hash


group_input = dbc.Col(
    [
        dbc.Row(
            dbc.FormGroup(
                [
                    dbc.Label("Old Password: ",
                              html_for="oldPassword", width=6),
                    dbc.Col(
                        dbc.Input(
                            type="password", id="oldPassword",
                            className='form-control',
                            n_submit=0, placeholder="Enter old password"
                        ),
                        width=6,
                    ),
                ], row=True
            )
        ),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("New Password: ",
                              html_for="newPassword1", width=6),
                    dbc.Col(
                        dbc.Input(
                            type="password",
                            id="newPassword1",
                            className='form-control',
                            n_submit=0,
                            placeholder="Enter new password",
                        ),
                        width=6,
                    ),
                ], row=True)
        ),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Retype New Password: ",
                              html_for="newPassword2", width=6),
                    dbc.Col(
                        dbc.Input(
                            type="password",
                            id="newPassword2",
                            className='form-control',
                            n_submit=0,
                            placeholder="Retype new password",
                        ),
                        width=6,
                    ),
                ], row=True
            ))
    ]
)

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlProfile', refresh=True),
        html.H3('Profile Management'),
        html.Hr(),
        dbc.Row([

            dbc.Col([
                dbc.Label('Username:'),
                html.Br(),
                html.Br(),
                dbc.Label('Email:'),
            ], md=2),

            dbc.Col([
                dbc.Label(id='username', className='text-success'),
                html.Br(),
                html.Br(),
                dbc.Label(id='email', className='text-success'),
            ], md=2),
            dbc.Form([group_input]),
            dbc.Col([
                html.Button(
                    children='Update Password',
                    n_clicks=0,
                    type='submit',
                    id='updatePasswordButton',
                    className='btn btn-primary btn-lg',
                    style={'textAlign': 'center', 'margin-left': '40%', 'width': '200px', 'height': '45px', 'padding': '10px', 'margin-top': '10px',
                           'font-size': '16px'
                           }
                ),
                html.Br(),
                html.Div(id='updateSuccess')], md=8),
        ])
    ]  # , className='jumbotron'
    )
], style={
    'textAlign': 'center', 'margin-left': '20%'
}
)


@app.callback(
    Output('username', 'children'),
    [Input('pageContent', 'children')])
def currentUserName(pageContent):
    try:
        username = current_user.username
        return username
    except AttributeError:
        return ''


@app.callback(
    Output('email', 'children'),
    [Input('pageContent', 'children')])
def currentUserEmail(pageContent):
    try:
        email = current_user.email
        return email
    except AttributeError:
        return ''

################################################################################
# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF OLD PWD IS NOT CURR PWD
################################################################################


@app.callback(Output('oldPassword', 'className'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('pageContent', 'children'),
              State('oldPassword', 'value'),
              State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def validateOldPassword(n_clicks, newPassword1Submit, newPassword2Submit, pageContent,
                        oldPassword, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if check_password_hash(current_user.password, oldPassword):
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


# ###############################################################################
# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF NEW PASSWORDS ARE NOT THE SAME
# ###############################################################################
@app.callback(Output('newPassword1', 'className'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def validatePassword1(n_clicks, newPassword1Submit, newPassword2Submit, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if newPassword1 == newPassword2:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


# ###############################################################################
# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF NEW PASSWORDS ARE NOT THE SAME
# ###############################################################################
@app.callback(Output('newPassword2', 'className'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def validatePassword2(n_clicks, newPassword1Submit, newPassword2Submit, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if newPassword1 == newPassword2:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


################################################################################
# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - UPDATE DATABASE WITH NEW PASSWORD
################################################################################
@app.callback(Output('updateSuccess', 'children'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('pageContent', 'children'),
              State('oldPassword', 'value'),
              State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def changePassword(n_clicks, newPassword1Submit, newPassword2Submit, pageContent,
                   oldPassword, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if check_password_hash(current_user.password, oldPassword) and newPassword1 == newPassword2:
            try:
                update_password(current_user.username, newPassword1)
                return html.Div(children=['Update Successful'], className='text-success')
            except Exception as e:
                return html.Div(children=['Update Not Successful: {e}'.format(e=e)], className='text-danger')
        else:
            return html.Div(children=['Old Password Invalid'], className='text-danger')
