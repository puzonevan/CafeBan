from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__, static_url_path='/static')
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home(): 
    return render_template("home.html")

@app.route('/gallery')
def gallery(): 
    return render_template("gallery.html")

@app.route('/menu')
def menu(): 
    return render_template("menus.html")

@app.route('/menu/<int:menu_id>')
def singlemenu(menu_id): 
    return render_template("menu.html")

@app.route('/locations')
def location(): 
    return render_template("locations.html")

