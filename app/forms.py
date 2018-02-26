from flask_wtf import FlaskForm

from wtforms import TextField, Form, TextAreaField,  StringField, SubmitField

from wtforms import validators, ValidationError

class LoginForm(FlaskForm):
    name=StringField('name',[validators.Required("Please enter your name.")])
    email=StringField('email',[validators.Required('Please enter an email address.'),
    validators.Email('Please enter your email address.')])
    
    subject= StringField('subject',[validators.Required('Please enter an email address.')])
    message=TextAreaField('message',[validators.Required('Message field cannot be empty.')])
    submit=SubmitField('Send')
    
    