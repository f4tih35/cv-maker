#!/usr/bin/python
# -*- coding: utf-8 -*-

import bcrypt
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user, login_user
from ..extensions import db
from ..forms import RegisterForm, LoginForm
from ..models import User


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'{form.email.data} logged in', 'success')
            return redirect(url_for('welcome'))
        else:
            flash(f'Email or password incorrect', 'danger')
            return redirect(url_for('login'))
    return render_template('login-new.html', title='Login', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        exist = User.query.filter_by(email=form.email.data).first()
        if exist:
            flash(f'This email already exists!', 'danger')
            return redirect(url_for('register'))
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created', 'success')
        logout_user()
        return redirect(url_for('login'))
    return render_template('register-new.html', title='Register', form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
