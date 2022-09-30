from enum import unique
import dash
import dash_bootstrap_components as dbc
import os

from sqlalchemy import Table, create_engine
from sqlalchemy.pool import NullPool

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.ZEPHYR]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
# FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

db_url = "postgresql://postgres:20091994@localhost:5432/mapweb"
engine = create_engine(db_url, poolclass = NullPool)
conn = engine.connect()
db = SQLAlchemy()

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True,nullable=False)
    password = db.Column(db.String(80), unique=True,nullable=False)

Users_tbl = Table('usuarios', Usuarios.metadata)


app = dash.Dash(__name__, external_stylesheets = estilos + [dbc_css])

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server



server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI= db_url,
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(server)

class Usuarios(UserMixin, Usuarios):
    pass
