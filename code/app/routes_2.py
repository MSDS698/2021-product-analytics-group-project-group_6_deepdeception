from app import application
from flask import render_template, redirect, url_for
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
@application.route('/', methods=['GET', 'POST'])
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


@application.route('/team')
def team():
    """Index Page : Renders index.html with author name."""
    return (render_template('our-team.html', author='Deception Perception'))
