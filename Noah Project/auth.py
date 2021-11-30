from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask.wrappers import Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return render_template('signup.html', userExists=None, isStudent=None)

@auth.route('/signup', methods=['POST'])
def signup_post():

    isStudent = True
    userExists = False

    email = request.form.get('email')
    username = request.form.get('username')
    firstname = request.form.get('firstName')
    lastname = request.form.get('lastName')
    password = request.form.get('password')
    major = request.form.get('major')
    grad_year = request.form.get('grad_year')
    birthday = request.form.get('birthday')

    if('@students.ccu.edu' in email):
        isStudent = True
    else:
        isStudent = False
        return render_template('signup.html', userExists=userExists, isStudent=isStudent)

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        userExists = True
        return render_template('signup.html', userExists=userExists, isStudent=isStudent)

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, firstname=firstname, lastname=lastname, username=username, password=generate_password_hash(password, method='sha256'), 
                    major=major, grad_year=grad_year, birthday=birthday)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html', invalid_login=None)

@auth.route('/login', methods=['POST'])
def login_post():

    invalid_login = False

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        invalid_login = True
        return render_template('login.html', invalid_login=invalid_login) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    
    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))