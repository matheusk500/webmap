from dash import html, dcc
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
import os
from dash_iconify import DashIconify

from app import *

def render_sidebar(cidade,logo_cidade):
    layout = dbc.Col([
        html.H1(cidade, className='text-primary', style={'font-size' : '30px', 'text-align' : 'center'}),
        html.P('By BrEngenharia', className='text-info'),

        html.Div(
            html.Img(src='/assets/images/'+logo_cidade, id='avatar_change', alt='avatar', className='perfil_avatar'), className='div_perfil_avatar'
        ),

        html.Hr(),
            
        dbc.Nav(
            [
            dbc.NavLink('Web Mapa', href='/webmap', active='exact'),
            dbc.NavLink('Web Mapa - Legendas', active='exact'),
            dbc.NavLink('Dashboard', href='/dashboard', active='exact'),
            dbc.NavLink('Sair', href='/', active='exact')
            ], 
            vertical=True, pills=True, id='nav_buttons', style={'margin-bottom' : '50px'}
        ),
        
    ], id='sidebar_completa')

    return layout

