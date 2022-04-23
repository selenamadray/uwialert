from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.models import User, Report
from flask import Flask, render_template, redirect, url_for, request
from .forms import SignUpForm, LogInForm, ReportForm
from App.database import *
from flask import flash

from App.controllers import (
    authenticate,
    logout_user,
    login_user,
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

@user_views.route('/logout', methods=['GET'])
def logout():
    form = LogInForm()
    logout_user()
    return render_template('login.html', form=form)


@user_views.route('/signup', methods=['POST'])
def signupAction():
    form = SignUpForm()  # create form object
    if not form.validate_on_submit():
        flash('Error invalid input!')
        return render_template('signup.html', form=form)

    data = request.form  # get data from form submission
    existingUser = User.query.filter_by(username=data['username']).first()

    if existingUser is not None:
        flash("The email address " +
              data['username']+" is already in use. Please try again with a new email.")
        return render_template('signup.html', form=form)

    newuser = User(username=data['username'],
                    email=data['email'])  # create user object
    newuser.set_password(data['password'])  # set password
    db.session.add(newuser)  # save new user
    db.session.commit()
    flash('Account Created!')  # send message
    return render_template('index.html')  # redirect to login page


@user_views.route('/', methods=['GET'])
def index():
    form = LogInForm()
    return render_template('login.html', form=form)


@user_views.route('/login', methods=['GET', 'POST']) 
def login():
    error = None
    if request.method == 'POST':
        userToLogIn= authenticate(request.form['username'],request.form['password'])
        if userToLogIn:
             login_user(userToLogIn,True)
             return render_template('index.html')
        # .username is None or request.form['password'] != userToLogIn.password:
        #     error = 'Invalid Credentials. Please try again.'
        #     return error
        else:
            return 'Invalid Credentials. Please try again.'
           
            
    

@user_views.route('/notifs', methods=['GET'])
def get_reports_page():
    reports = get_all_reports()
    return render_template('notifs.html', reports=reports)

#@user_views.route('/map', methods=['GET'])
#def get_all_map():
  #  location = getMap()
   # return render_template('map.html', location=location)


@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)


@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/map')
def map_page():
    return render_template('map.html')

@user_views.route('/static/users')
def static_user_page():
    return send_from_directory('static', 'static-user.html')

@user_views.route('/report', methods=['GET'])
def makereport():
    form = ReportForm()  # create form object
    return render_template('report.html', form=form)

@user_views.route('/report', methods=['POST'])
def reportAction():
    form = ReportForm() # create form object
    if not form.validate_on_submit():
        flash('Error invalid input!')
        return render_template('report.html', form=form)

    data = request.form  # get data from form submission
    newreport = Report(name=data['name'],
                    type=data['type'], location=data['location'], date=data['date'], details=data['details'])  # create user object
    db.session.add(newreport)  # save new user
    db.session.commit()
    flash('Thank you for making a report.')  # send message
    return render_template('index.html')  # redirect to login page 