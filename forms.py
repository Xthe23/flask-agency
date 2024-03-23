from wtforms.validators import DataRequired, Email
from wtforms import StringField, BooleanField, TimeField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, FileField
from wtforms.validators import InputRequired, Length, EqualTo, Optional


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     InputRequired(), EqualTo('password')])
    role = SelectField(
        'Role', choices=[('client', 'Client'), ('worker', 'Worker')])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    resume = FileField('Resume', validators=[Optional()])
    # Optional fields
    address = StringField('Address', validators=[Optional(), Length(max=100)])
    city = StringField('City', validators=[Optional(), Length(max=100)])
    state = StringField('State', validators=[Optional(), Length(max=100)])
    zip_code = StringField('Zip Code', validators=[Optional(), Length(max=100)])
    phone = StringField('Phone', validators=[Optional(), Length(max=100)])
    schedule_monday = BooleanField('Monday')
    schedule_tuesday = BooleanField('Tuesday')
    schedule_wednesday = BooleanField('Wednesday')
    schedule_thursday = BooleanField('Thursday')
    schedule_friday = BooleanField('Friday')
    schedule_saturday = BooleanField('Saturday')
    schedule_sunday = BooleanField('Sunday')
    start_date = TimeField('Start Time', format='%H:%M', validators=[Optional()])
    end_date = TimeField('End Time', format='%H:%M', validators=[Optional()])
