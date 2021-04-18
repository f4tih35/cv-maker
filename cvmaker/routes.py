from cvmaker import app, db, login_manager
from flask import render_template, flash, redirect, url_for, session, jsonify, make_response, request
from cvmaker.forms import RegisterForm, LoginForm, WelcomeForm, EditForm, MyForm
from cvmaker.models import User
from flask_login import login_required, login_user, logout_user, current_user
import json
import pdfkit
from flask_weasyprint import render_pdf
from . import bcrypt, images, app
from werkzeug.utils import secure_filename
from flask_uploads import configure_uploads, IMAGES, UploadSet

@app.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: { filename }'
    return render_template('upload.html', form=form)


@app.route('/home',methods=['GET','POST'])
@login_required
def index():
    if current_user.imgfilename:
        img_url = images.url(current_user.imgfilename)
    else:
        img_url = None
    return render_template('index-new.html',img_url=img_url)

@app.route('/edit',methods=['GET','POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data

        current_user.job = form.job.data
        current_user.introducing = form.introducing.data

        try:
            current_user.phone = int(form.phone.data)
        except:
            flash(f'Incorrect Phone', 'danger')

        current_user.address = form.address.data
        current_user.work = form.work.data
        current_user.school = form.school.data
        current_user.hobbies = form.hobbies.data

        if not current_user.imgfilename == form.imgfilename.data:
            try:
                current_user.imgfilename = images.save(form.imgfilename.data)
                img_url = images.url(current_user.imgfilename)
            except:
                flash(f'Incorrect File', 'danger')
                print('incorrect file')

        db.session.add(current_user)
        db.session.commit()
        flash(f'Edited', 'success')
        return redirect(url_for('index'))
    return render_template('edit-new.html', title='Home', form=form)

@app.route('/login',methods=['GET','POST'])
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

@app.route('/welcome',methods=['GET','POST'])
@login_required
def welcome():
    if current_user.welcome == False:
        form = WelcomeForm()
        if form.validate_on_submit():
            current_user.firstname = form.firstname.data
            current_user.lastname = form.lastname.data
            current_user.address = form.address.data

            current_user.job = form.job.data
            current_user.introducing = form.introducing.data

            try:
                current_user.phone = int(form.phone.data)
            except:
                flash(f'Incorrect Phone', 'danger')

            current_user.hobbies = form.hobbies.data
            current_user.work = form.work.data
            current_user.school = form.school.data
            current_user.welcome = True
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index')) 
    return render_template('welcome-new.html', title='Welcome', form=form)

@app.route('/register',methods=['GET','POST'])
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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

from weasyprint import HTML

@app.route('/getpdf')
@login_required
def getpdf():
    if current_user.imgfilename:
        img_url = images.url(current_user.imgfilename)
    else:
        img_url = None
    html = render_template('resume-new.html',img_url=img_url)
    #return render_template('resume.html', title='Register')
    return render_pdf(HTML(string=html))


@app.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def intro():
    return render_template('intro-new.html')

