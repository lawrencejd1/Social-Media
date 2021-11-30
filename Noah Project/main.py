import os
from flask import Blueprint, current_app, render_template, request
from flask.helpers import url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect, secure_filename

from .models import Post, User
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    for post in posts:
        print(post.image)
    return render_template('index.html', posts=posts)

@main.route('/profile')
@login_required
def profile():

    user = current_user._get_current_object()
    

    return render_template('profile.html', user=user)

@main.route('/addpost')
@login_required
def addPost():
    return render_template('add_post.html')

@main.route('/addpost', methods=['POST'])
@login_required
def addPost_post():
    basedir = os.path.abspath(os.path.dirname(__file__))

    user = current_user._get_current_object()

    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join(basedir, current_app.config['UPLOAD_FOLDER'], filename))
    caption = request.form.get('caption')

    post = Post(username=user.username, image=filename, caption=caption)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('main.index'))
