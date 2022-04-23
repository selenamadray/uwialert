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
    type = StringField('Type', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    date = StringField('Date of Incident', validators=[InputRequired()])
    details = StringField('Details', validators=[InputRequired()])
    submit = SubmitField('Make Report', render_kw={
                         'class': 'btn waves-effect waves-light white-text'})