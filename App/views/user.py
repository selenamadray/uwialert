from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.models import User
from flask import Flask, render_template, redirect, url_for, request
from .forms import SignUpForm, LogInForm
from App.database import *

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    get_all_reports,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@user_views.route('/signup', methods=['GET'])
def signup():
    form = SignUpForm()  # create form object
    return render_template('signup.html', form=form)


@user_views.route('/signup', methods=['POST'])
def signupAction():
    form = SignUpForm()  # create form object
    if not form.validate_on_submit():
        flash('Error invalid input!')
        return redirect(url_for('signup'))

    data = request.form  # get data from form submission
    existingUser = User.query.filter_by(username=data['username']).first()

    if existingUser is not None:
        flash("The email address " +
              data['username']+" is already in use. Please try again with a new email.")
        return redirect(url_for('signup'))

    newuser = User(username=data['username'],
                    email=data['email'])  # create user object
    newuser.set_password(data['password'])  # set password
    db.session.add(newuser)  # save new user
    db.session.commit()
    flash('Account Created!')  # send message
    return redirect(url_for('index'))  # redirect to login page


@user_views.route('/', methods=['GET'])
def index():
    form = LogInForm()
    return render_template('login.html', form=form)


@user_views.route('/login', methods=['GET', 'POST']) 
def login():
    error = None
    if request.method == 'POST':
        userToLogIn = User.query.filter_by(username=request.form['username']).first()
        if userToLogIn is None or request.form['password'] != userToLogIn['password']:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', form=User(username="", password=""), error=error)


@user_views.route('/notifs', methods=['GET'])
def get_reports_page():
    reports = get_all_reports()
    return render_template('notifs.html', report=reports)


@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)


@user_views.route('/api/lol')
def lol():
    return 'lol'


@user_views.route('/static/users')
def static_user_page():
    return send_from_directory('static', 'static-user.html')
