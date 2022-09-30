from dash import html, dcc
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output
from app import *
from flask_login import current_user
from components import sidebar, dashboard, webmap



def render_layout(username):
    content = html.Div(id='page-content-myindex', style={'height' : '100vh'})
    layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col([
                    dcc.Location(id='url', refresh=False),
                    sidebar.render_sidebar("Cerro cora", "img_hom.png")
                ], md=2, sm= 2, style={'background-color' : 'white', }),
                dbc.Col([
                    content
                ], md=10, sm= 10, style={'background-color' : 'transparent' })
            ])
        ], fluid=True
    )
    return layout

@app.callback(
    Output('page-content-myindex', 'children'),
    [Input('url', 'pathname')]
)
def render_page(pathname):
    if pathname =='/webmap':
        if current_user.is_authenticated:
            return webmap.render_web_map("cerrocora")

    if pathname == '/dashboard':
        if current_user.is_authenticated:
            return dashboard.layout
