from app import application, classes, db
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

import os


class UploadFileForm(FlaskForm):
    """Class for uploading file when submitted"""
    file_selector = FileField('File', validators=[FileRequired()])
    submit = SubmitField('Submit')


# @application.route('/index')
# def index():
#     """Index Page : Renders index.html with author name."""
#     return ("<h1> File uploaded. Thanks for using Deep Depeception! </h1>")
#     # return (render_template('index.html', author='Deep Deception'))


@application.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    """
    upload and process a csv file to check for deception.
    Note: This is still a WIP
    """
    file = UploadFileForm()  # file : UploadFileForm class instance
    if file.validate_on_submit():  # Check if it is a POST request and if it is valid.
        f = file.file_selector.data  # f : Data of FileField
        filename = f.filename
        # filename : filename of FileField

        file_dir_path = os.path.join(application.instance_path, 'files')
        file_path = os.path.join(file_dir_path, filename)
        # f.save(file_path)  # Save file to file_path (instance/ + 'files’ + filename)

        return redirect(url_for('upload'))  # Redirect to / (/index) page.
    return render_template('upload.html', form=file)


@application.route('/register',  methods=('GET', 'POST'))
def register():
    registration_form = classes.RegistrationForm()
    if registration_form.validate_on_submit():
        username = registration_form.username.data
        password = registration_form.password.data
        email = registration_form.email.data

        user_count = classes.User.query.filter_by(username=username).count() \
                     + classes.User.query.filter_by(email=email).count()
        if user_count > 0:
            return '<h1>Error - Existing user : ' + username \
                   + ' OR ' + email + '</h1>'
        else:
            user = classes.User(username, email, password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', form=registration_form)


@application.route('/login', methods=['GET', 'POST'])
@application.route('/', methods=['GET', 'POST'])
def login():
    login_form = classes.LogInForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        # Look for it in the database.
        user = classes.User.query.filter_by(username=username).first()

        # Login and validate the user.
        if user is not None and user.check_password(password):
            login_user(user)
            return redirect(url_for('upload'))

    return render_template('login.html', form=login_form)


@application.route('/logout')
@login_required
def logout():
    before_logout = '<h1> Before logout - is_autheticated : ' \
                    + str(current_user.is_authenticated) + '</h1>'

    logout_user()

    after_logout = '<h1> After logout - is_autheticated : ' \
                   + str(current_user.is_authenticated) + '</h1>'
    return before_logout + after_logout


@application.route('/team')
def team():
    """Index Page : Renders index.html with author name."""
    return (render_template('our-team.html', author='Deception Perception'))
