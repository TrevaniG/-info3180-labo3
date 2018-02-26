from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='secrethash'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='82ecd6869a4301'
app.config['MAIL_PASSWORD']='56dee6ea4918fb'

mail=Mail(app)
from app import views