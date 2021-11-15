from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit_button = SubmitField()

class UserSignupForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit_button = SubmitField()

class CharacterForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    alias = StringField('Alias:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
    comics_appeared_in = IntegerField('Appearance(s):', validators=[DataRequired()])
    super_power = StringField('Super Power(s):', validators=[DataRequired()])
    submit_button = SubmitField()
