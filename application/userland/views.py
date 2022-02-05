#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from flask_weasyprint import render_pdf
from weasyprint import images, HTML
from ..forms import MyForm, EditForm, WelcomeForm


userland = Blueprint('userland', __name__, url_prefix='/userland')


@userland.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: {filename}'
    return render_template('upload.html', form=form)


@userland.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.imgfilename:
        img_url = images.url(current_user.imgfilename)
    else:
        img_url = None
    return render_template('index-new.html', img_url=img_url)


@userland.route('/edit', methods=['GET', 'POST'])
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


@userland.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    if not current_user.welcome:
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


@userland.route('/getpdf')
@login_required
def getpdf():
    if current_user.imgfilename:
        img_url = images.url(current_user.imgfilename)
    else:
        img_url = None
    html = render_template('resume-new.html', img_url=img_url)
    # return render_template('resume.html', title='Register')
    return render_pdf(HTML(string=html))


@userland.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'), 404


@userland.route('/')
def intro():
    return render_template('intro-new.html')
