from turtle import width
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
import os

from app import *

layout = html.Iframe(src="https://app.powerbi.com/view?r=eyJrIjoiOTJlODE4NGYtMjZmMC00OWExLThjMjItZmFlY2IwYjNmZWVmIiwidCI6ImRjYmYyYTFmLTk1MzItNGQ1Ni1hYzQxLTU2MTVlMzhlNTBiNyJ9",
        style={"height": "100vh", "width": "100%"})




    
