from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy 
from wtforms.validators import DataRequired 
import os, sorts


app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'MY_SECRET_KEY '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' 

db = SQLAlchemy(app)

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home(): 
    return render_template("home.html")

@app.route('/gallery')
def gallery(): 

    cafeimages = sorts.mergeSort(os.listdir('./static/CafeImgs'))
    coffeeimages = sorts.mergeSort(os.listdir('./static/CoffImgs'))
    cakeimages = sorts.mergeSort(os.listdir('./static/CakeImgs'))

    return render_template("gallery.html", 
        cafeimages=cafeimages, 
        cakeimages=cakeimages, 
        coffeeimages=coffeeimages, 
    )

@app.route('/menu')
def menu(): 
    return render_template("menus.html")

@app.route('/menu/<int:menu_id>')
def singlemenu(menu_id): 
    return render_template("menu.html")

@app.route('/locations')
def location(): 
    
    locations = [
        {
            'city': 'San Francisco',
            'address': '201 Fell St, CA 94102', 
            'number': '+14154372734',
        }, 
        {
            'city': 'Seoul',
            'address': '10 Hongik-ro, Seogyo-dong, Mapo-gu, Seoul', 
            'number': '+82 2-332-7470',
        }, 
        {
            'city': 'Tokyo',
            'address': '〒 103-0027 Tokyo, Chuo City, Nihonbashi, 2 Chome−11−2 日', 
            'number': '+81 3-6262-3439',
        }, 
    ]

    return render_template("locations.html",
        locations=locations, 
    )



""" Form Classes """ 
class ContactForm(FlaskForm): 
    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = StringField("Message")
    submit = SubmitField("Submit")

class ReviewForm(FlaskForm): 
    name = StringField("Name")
    review = StringField("Review")
    submit = SubmitField("Add Review")


