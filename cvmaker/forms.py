from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
    email  = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign In')

class WelcomeForm(FlaskForm):
    address = StringField('Address')
    work = StringField('Job')
    school = StringField('School')
    hobbies = StringField('Hobbies')
    submit = SubmitField('Continue')

class EditForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
    email  = StringField('Email',validators=[DataRequired(), Email()])
    address = StringField('Address')
    work = StringField('Job')
    school = StringField('School')
    hobbies = StringField('Hobbies')
    submit = SubmitField('Continue')
    