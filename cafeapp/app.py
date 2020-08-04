from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

@app.route('/home')
def home(): 
    return "Hello World!"

@app.route('/gallery')
def gallery(): 
    return "Hello Gallery!"

@app.route('/menu')
def menu(): 
    return "Hello Menus!"

@app.route('/menu/<int:menu_id>')
def singlemenu(menu_id): 
    return "Hello Menu!"

@app.route('/location')
def location(): 
    return "Hello Location!"

