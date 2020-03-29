from flask_wtf import FlaskForm

from wtforms import StringField, TextField, SubmitField


class MainForm(FlaskForm):
    """Index page form"""
    recording_url = StringField('Recording:')
    submit = SubmitField('Submit')
