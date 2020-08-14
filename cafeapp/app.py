# Flask Imports 
from flask import Flask
# Form Imports 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired 
# SQL Imports 
from flask_sqlalchemy import SQLAlchemy 


""" Initialize / configure app """
app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'MY_SECRET_KEY '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' 

""" Bind app to SQL """
db = SQLAlchemy(app)


""" Form Classes """ 
class ContactForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ReviewForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    review = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Add Review")

class ApplicationForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    number = StringField("Number", validators=[DataRequired()])
    submit = SubmitField("Submit")

""" Database Models """ 
class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, index = True)
    email = db.Column(db.String(100), unique = True, index = True)
    subject = db.Column(db.String(50), unique = False, index = False)
    message = db.Column(db.String(300), unique = False, index = False)

class Review(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, index = True)
    review = db.Column(db.String(1000), unique = True, index = False)

class Application(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, index = True)
    number = db.Column(db.String(15), unique = True, index = False)
    description = db.Column(db.String(1000), unique = True, index = False)




import routes 