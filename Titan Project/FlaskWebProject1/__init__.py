"""
The flask application package.
"""

from flask import Flask
import pyodbc
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['Cougagram'] = 'DESKTOP-CR51903\SQLEXPRESS'
db = SQLAlchemy(app)
import FlaskWebProject1.views
