from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, FileField, TextAreaField
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
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    phone = StringField('Phone')
    introducing = TextAreaField('Introducing')
    job = StringField('Job')
    address = StringField('Address')
    work = StringField('Work History')
    school = StringField('School')
    hobbies = StringField('Hobbies')
    submit = SubmitField('Continue')

class EditForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
    email  = StringField('Email',validators=[DataRequired(), Email()])
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    phone = StringField('Phone')
    introducing = TextAreaField('Introducing')
    job = StringField('Job')
    address = StringField('Address')
    dateofbirth = DateTimeField('DateOfBirth')
    work = StringField('Job')
    school = StringField('School')
    hobbies = StringField('Hobbies')
    imgfilename = FileField('image')
    submit = SubmitField('Edit')
    
class MyForm(FlaskForm):
    image = FileField('image')