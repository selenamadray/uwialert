from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email
from App.models import User, Report


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('New Password', validators=[
                             InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up', render_kw={
                         'class': 'btn waves-effect waves-light white-text'})


class LogInForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={
                         'class': 'btn waves-effect waves-light white-text'})

class ReportForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    type = StringField('What type of incident are you reporting?', validators=[InputRequired()])
    location = StringField('Where did this incident occur?', validators=[InputRequired()])
    date = StringField('Please give the date of the incident.', validators=[InputRequired()])
    details = StringField('Please give a brief description of any important details.', validators=[InputRequired()])
    submit = SubmitField('Make Report', render_kw={
                         'class': 'btn waves-effect waves-light white-text'})