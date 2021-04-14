from cvmaker import app, db, login_manager
from flask import render_template, flash, redirect, url_for
from cvmaker.forms import RegisterForm, LoginForm
from cvmaker.models import User
from flask_login import login_required, login_user, logout_user, current_user
@app.route('/')
@app.route('/home')

@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()  
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'{form.email.data} logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'{form.email.data} login failed', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data} account created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))