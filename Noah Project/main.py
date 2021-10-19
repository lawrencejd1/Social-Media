from flask import Flask, Blueprint, render_template, abort, jsonify, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from datetime import datetime
from FlaskWebProject1 import app
import pyodbc
from flask_sqlalchemy import SQLAlchemy

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

def create_new_user():
    if request.method == "POST":
        full_connection_string = connect_to_server()
        user_data = collect_user_data()
        execution_statement = create_exec_statement(user_data)
        try:
            run_procedure(full_connection_string, execution_statement)
            return redirect( url_for('contact') )
        except:
            return render_template('about.html')
    else:
        return render_template('about.html')


def connect_to_server():
    full_connection_string = make_connection_string('DESKTOP-CR51903\SQLEXPRESS', 'Cougagram')
    return full_connection_string

def make_connection_string(server, database):
    connection_string = 'DRIVER={SQL SERVER}; SERVER=' + server + '; Database=' + database + '; TRUSTCONNECTION=yes'
    #connection_string += 'User Id=cSam;Password=P@ssw0rd;'
    return connection_string

def query_data(connection_string, query):
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    return data

def run_procedure(connection_string, command):
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        cursor.execute(command)

def create_exec_statement(form_data):
    execution_statement = "EXEC Create_User '"
    count = 0
    while count < len(form_data):
        if count == 0:
            execution_statement += form_data[count] + "'"
        else:
            execution_statement += ", '" + form_data[count] + "'"
        count += 1
    execution_statement += ";"
    return execution_statement

def collect_user_data():
    user_data = [request.form['username'], request.form['first_name'], request.form['last_name'],
                 request.form['email'], request.form['password']]
    return user_data
def collect_group_data():
    group_data = [request.form['category_name'],request.form['group_name'], request.form['group_description']]
    return group_data
def join_group():
    group_data = [request.form['category_name'],request.form['group_name'], request.form['group_description']]
    return group_data