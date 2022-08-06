from flask import Flask
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class JobDescriptionAndResumeForm(FlaskForm):
    responsibilities = TextAreaField('Role Responsibilities')
    requirements = TextAreaField('Requirements/Qualifications')
    experience = TextAreaField('Work Experience')
    education = TextAreaField('Education')
    skills = TextAreaField('Technical Skills')
    submit = SubmitField('Analyze')