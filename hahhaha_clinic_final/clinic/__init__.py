import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()  # Tải các biến môi trường từ file .env

app = Flask(__name__)
app.secret_key = "KJGHJG^&*%&*^T&*(IGFG%ERFTGHCFHGF^&**&TYIU"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/haha?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_USERNAME'] = "phongkhamsaigoncare@gmail.com"
app.config['MAIL_PASSWORD'] = "secret_password"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_PORT'] = 587
app.config['SUM'] = 100000

app.config['PAGE_SIZE'] = 5

mail = Mail(app)

db = SQLAlchemy(app=app)

cloudinary.config(
       cloud_name = 'dmz9kuzue',
       api_key = '961193598266337',
       api_secret = 'secrect'
)

login = LoginManager(app=app)

MAX_PATIENT = 3
