from dash import html, dcc
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
import os

from app import app

def render_web_map(cidade):

        layout = html.Iframe(src="/assets/maps/"+cidade+".html",
                style={"height": "100vh", "width": "100%"})

        return layout
